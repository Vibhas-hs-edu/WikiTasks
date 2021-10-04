from genericpath import isdir
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from typing import Counter, Dict
from math import log
import os
import xml_helper
from math_helper import softmax

class WikiExtractor:
    """Computes the most common words
    in all the documents as well as the most important words
    present in a particular document.

    Attributes:
        folder_name: The folder which contains the wiki_files.
        temp_folder_name: The temporary working folder.
    """
    def __init__(self, folder_name) -> None:
        """
        WikiExtractor constructor. Initialise the
        folder name where wiki_files are present.
        Also initialise temp_folder name.

        :param folder_name: The folder name where wiki_files
        are present
        """
        self.folder_name = folder_name
        self.temp_folder_name = 'Temp'
        if not os.path.exists(self.folder_name):
            raise FileNotFoundError(f"{self.folder_name} doesn't exists")
        print('Init')

    def tokenize(self):
        """
        Convert the list of wikipedia documents to a list of words.
        Essentially like bag of words model.

        :return: returns the list of all words in all of wikipedia documents.
        :return: returns the dictionary of documents associated with its list of words.
        """
        wiki_files = [f for f in os.listdir(self.folder_name)]
        net_word_list = []
        doc_word_dict = {}
        for wiki_file in wiki_files:
            docs = xml_helper.parseXML(self.folder_name + '/' + wiki_file, self.temp_folder_name)
            for doc in docs:
                tokenized_word = word_tokenize(doc.text)
                net_word_list.extend(tokenized_word)
                doc_word_dict[doc.attrib['id']] = tokenized_word
        return (net_word_list, doc_word_dict)
    
    def get_frequency_dist(self, word_list):
        """
        Computes the frequency distribution of all words in all of wikipedia document

        :param word_list: The list of all words in all of wikipedia documents.

        :return: returns the frequency distribution of all the words present in all of wikipedia
        documents
        """
        fdist = FreqDist(word_list)
        return fdist
    
    def get_most_common_words(self, f : FreqDist, n : int) -> Dict:
        """
        Returns the 'n' most common words in the wikipedia document

        :param f: The frequency distribution associated with the list of all words.
        :param n: Number of most common words to return.

        :return: Returns the 'n' most common words in the wikipedia document
        """
        return f.most_common(n = n)

    def get_words_importance(self, doc_word_dict : dict, id : int) -> list:
        """
        Computes the words importance for all the words for a particular document. The word importance
        is measured by how commonly the word is present in other documents. If the word
        is present in a lot of documents, the word is not really unique to the document
        and therefore not important. If words is present in very few documents, then probably
        the word is important and can be used to retrieve other similar documents. Note that
        the numerator is constant but the denominator varies for each word based on the number
        of documents where the word is found.

        :param doc_word_dict: Dictionary of all words associated with the respective document ids.
        :param id: ID of the document .

        :return: Returns a dictionary of all words with it's associated importance.
        """
        word_list = doc_word_dict[id]
        word_importance = {}
        for word in word_list:
            word_importance[word] = log(len(doc_word_dict) / self.get_docs_for_word(word, doc_word_dict))
        return word_importance

    def get_docs_for_word(self, word : str, doc_word_dict : dict) -> float:
        """
        Computes how many docs the word is repeated

        :param word: The specified word.
        :param doc_word_dict: Dictionary of all words associated with the respective document ids.

        :return: Returns a dictionary of all words with it's associated importance.
        """
        n_docs = len(doc_word_dict)
        n_docs_containing_word = 0
        for doc in doc_word_dict:
            if word in doc_word_dict[doc]:
                n_docs_containing_word = n_docs_containing_word + 1
        if n_docs_containing_word == 0:
            print("Safety check. Ideally it shouldn't enter this if condition")
            return 1
        return n_docs_containing_word
    
    def get_most_important_words(self, word_importance_dict : dict, threshold : float) -> list:
        """
        Computes the most important words present in the dictionary. The function first converts the
        raw values associated words to probabilities by passing through softmax function.

        :param word_importance_dict: The dictionary which contains word with it's raw importance values.
        :param threshold: The threshold used to determine the most important words in the dictionary.

        :return: Returns a list of most important words.
        """
        important_words = []
        softmax_word_importance_dict = softmax(word_importance_dict)
        for word in softmax_word_importance_dict:
            if softmax_word_importance_dict[word] > threshold:
                important_words.append(word)
        return important_words
