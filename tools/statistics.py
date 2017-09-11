import nltk
import numpy as np
from __future__ import division

def lexical_diversity(text):
    '''Getting the average time that each word be used in the text.'''
    return len(text) / len(set(text))


def percentage(count, total):
    '''Getting the percent of count/total.'''
    return 100 * count / total
