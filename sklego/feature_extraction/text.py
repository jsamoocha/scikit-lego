import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class WordyTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, word_list):
        self.word_list = word_list
        self.good_words = ['gemakkelijk', 'fijn', 'handig', 'super', 'veel',
                           'snel', 'heel', 'gemak', 'goed', 'service', 'makkelijk']
        self.bad_words = ['minder', 'terug', 'erg', 'vind', 'leverbaar',
                          'keer', 'voorraad', 'steeds', 'slecht']

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        goods = [sum([w in s for w in self.good_words]) for s in X]
        bads = [sum([w in s for w in self.bad_words]) for s in X]
        return np.array([goods, bads]).T