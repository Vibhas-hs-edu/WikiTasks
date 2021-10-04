import math
import numpy as np

def softmax(word_importance_dict : dict) -> dict:
    """
    Computes softmax value of word_importance_dict values.

    :param word_importance_dict: describe about parameter p1

    :return: replaces raw values of word_importance_dict with
    softmax values
    """
    normalized_sum = np.sum(np.exp(list(word_importance_dict.values())))
    softmax_word_importance = {}
    for word in word_importance_dict:
        softmax_word_importance[word] = (math.e**word_importance_dict[word])/normalized_sum
    return softmax_word_importance
