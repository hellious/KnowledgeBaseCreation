# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join
import os
import re
from nltk import pos_tag, word_tokenize
import nltk
#imoport standford pos tag

file = 'sentences.txt'

with open(file) as f :
	sen = []
	sen_tags = []
	for line in f :
		#tag(line)
		#print in wiki format
		output = open("sentences_tagged.txt", "a")
		output.write()