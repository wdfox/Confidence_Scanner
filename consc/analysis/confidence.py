"""LIWC Confidence Method"""

import pkg_resources as pkg
from consc.data import load_folder

##
##

def load_corpus_words(file_name):
    """   """

    f_name = 'corpus/' + file_name + '.txt'
    f_path = pkg.resource_filename('consc', f_name)

    corpus_file = open(f_path, 'r')
    corpus_words = corpus_file.read().splitlines()

    return corpus_words


HIGH_CON_WORDS = load_corpus_words('positive')
LOW_CON_WORDS = load_corpus_words('negative')


def doc_confidence(document):

    confidence = 0

    for i in document.words:

        for j in HIGH_CON_WORDS:
            if j in i:
                confidence += 1

        for k in LOW_CON_WORDS:
            if k in i:
                confidence -= 1

    return confidence


def folder_confidence(data_type, search_term):

    docs = load_folder(data_type, search_term)

    confidence = [doc_confidence(doc) for doc in docs]

    return confidence
