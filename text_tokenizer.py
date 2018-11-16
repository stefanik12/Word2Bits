import nltk
from nltk.tokenize import word_tokenize

text_f = "text8"

text = open(text_f).read()
for w_tup in nltk.pos_tag(word_tokenize(text)):
    print("%s_%s" % w_tup, end=' ')
