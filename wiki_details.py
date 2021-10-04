import sys
from wiki_extractor import WikiExtractor

"""
Main entry point of the script file. Simply
run this script to determine the most common
words in wikiepedia corpus as well as the most
important words in wikipedia document '56572679'
"""

def display_help():
    print('Please specify the folder which contains the cleaned xml files')
    print('The typical usage is as follows :')
    print("python3 wiki_details.py 'text/AA'")

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        display_help()
        exit()
    folder_name = sys.argv[1]
    w = WikiExtractor(folder_name= folder_name)
    random_doc = '56572679'
    net_word_list, doc_word_dict = w.tokenize()
    print()
    print('100 Most common words with count in Wikipedia Corpus is as follows')
    print()
    f = (w.get_frequency_dist(net_word_list))
    print(w.get_most_common_words(f, 100))
    print()
    words_importance_dict = w.get_words_importance(doc_word_dict, random_doc)
    #threshold_list = [0.0001, 0.001, 0.01, 0.1]
    threshold_list = [0.001]
    for threshold in threshold_list:
        important_words_list = w.get_most_important_words(words_importance_dict, threshold)
        print(f'Threshold set is {threshold}.\n\n The most imporant words in the doc with doc_id {random_doc} are ', important_words_list)
