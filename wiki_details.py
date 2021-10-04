from wiki_extractor import WikiExtractor

if __name__ == '__main__':
    folder_name = 'text/AA'
    w = WikiExtractor(folder_name= folder_name)
    random_doc = '56572679'
    net_word_list, doc_word_dict = w.tokenize()
    print('100 Most common words in Wikipedia Corpus is as follows')
    print()
    f = (w.get_frequency_dist(net_word_list))
    print(w.get_most_common_words(f, 100))
    print()
    words_importance_dict = w.get_words_importance(doc_word_dict, random_doc)
    #threshold_list = [0.0001, 0.001, 0.01, 0.1]
    threshold_list = [0.001]
    for threshold in threshold_list:
        important_words_list = w.get_most_important_words(words_importance_dict, threshold)
        print(f'Threshold set is {threshold}\n\n. The most imporant words in the doc with doc_id {random_doc} are ', important_words_list)
