import nltk
import contractions
import string
import sys
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def tokenize(body):
    spacy_nlp = spacy.load("en_core_web_sm")
    stop_words = set().union(set(stopwords.words('english'))).union(spacy_nlp.Defaults.stop_words)
    lowered_input_str = body.lower().decode('utf8')
    translate_table = dict((ord(char), None) for char in string.punctuation)
    word_tokens=word_tokenize(contractions.fix(lowered_input_str).translate(translate_table))
    filtered_words = [w for w in word_tokens if not w in stop_words]
    filtered_words = list(dict.fromkeys(filtered_words))

    return filtered_words, 200

