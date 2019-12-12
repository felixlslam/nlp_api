import nltk
import contractions
import string
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

input_str = sys.argv[1]

stop_words = set(stopwords.words('english'))

lowered_input_str = input_str.lower()

translate_table = dict((ord(char), None) for char in string.punctuation)
word_tokens=word_tokenize(contractions.fix(lowered_input_str).translate(translate_table))

filtered_words = [w for w in word_tokens if not w in stop_words]
filtered_words = list(dict.fromkeys(filtered_words))

print(filtered_words)

