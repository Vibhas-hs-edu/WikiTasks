from genericpath import isdir
import os
from os import listdir
from os.path import isfile, join, exists
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import xml.etree.ElementTree as ET
from typing import Counter, Dict
from math import log
import numpy as np
import math

class WikiExtractor:
    def __init__(self, folder_name) -> None:
        self.folder_name = folder_name
        self.temp_folder_name = 'Temp'
        if not exists(self.folder_name):
            raise FileNotFoundError(f"{self.folder_name} doesn't exists")
        print('Init')

    def tokenize(self):
        wiki_files = [f for f in listdir(self.folder_name)]
        net_word_list = []
        doc_word_dict = {}
        for wiki_file in wiki_files:
            docs = self.parseXML(self.folder_name + '/' + wiki_file)
            for doc in docs:
                tokenized_word = word_tokenize(doc.text)
                net_word_list.extend(tokenized_word)
                doc_word_dict[doc.attrib['id']] = tokenized_word
        return (net_word_list, doc_word_dict)
    
    def get_frequency_dist(self, word_list):
        fdist = FreqDist(word_list)
        return fdist
    
    def get_most_common_words(self, f : FreqDist, n : int) -> Dict:
        return f.most_common(n = n)

    def make_xml_valid(self, wiki_file):
        parent = os.path.dirname(wiki_file)
        file_name =os.path.basename(wiki_file)
        temp_folder = os.path.join(os.path.dirname(parent), self.temp_folder_name)
        xml_temp = os.path.join(temp_folder, file_name)
        if not exists(temp_folder):
            os.mkdir(temp_folder)
        old = open(wiki_file, 'r')
        old_file_contents = old.read()
        new = open(xml_temp, 'w')
        new.write('<root>' + old_file_contents + '</root>')
        new.close()
        return xml_temp

    def parseXML(self, xmlfile):
        new_xml = self.make_xml_valid(xmlfile)
        tree = ET.parse(new_xml)
        root = tree.getroot()
        return root.findall('doc')
    
    def get_words_importance(self, doc_word_dict : dict, id : int) -> list:
        word_list = doc_word_dict[id]
        word_importance = {}
        for word in word_list:
            word_importance[word] = log(len(doc_word_dict) / self.inverse_document_frequency(word, doc_word_dict))
        return word_importance

    def inverse_document_frequency(self, word : str, doc_word_dict : dict) -> float:
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
        important_words = []
        softmax_word_importance_dict = self.softmax(word_importance_dict)
        for word in softmax_word_importance_dict:
            if softmax_word_importance_dict[word] > threshold:
                important_words.append(word)
        return important_words
    
    def softmax(self, word_importance_dict : dict) -> dict:
        normalized_sum = np.sum(np.exp(list(word_importance_dict.values())))
        softmax_word_importance = {}
        for word in word_importance_dict:
            softmax_word_importance[word] = (math.e**word_importance_dict[word])/normalized_sum
        return softmax_word_importance


        