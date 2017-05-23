import re
import check_ambiguity as ca
from nltk.tag.stanford import StanfordPOSTagger
import os

aux_verbs = ['am', 'is', 'are' ,'was' ,'were', 'being', 'been', 'does', 'do', 'did' , 'has', 'have', 'had' , 'having' , 'can', 'could', 'may', 'might', 'must', 'ought to', 'shall', 'should', 'will', 'would']
connectors = ['therefore', 'as a consequence', 'for this reason', 'for all these reasons', 'thus', 'because', 'because of', 'since', 'on account of', 'due to', 'for the reason', 'so, that', 'so that']

def getTags(sen_arr):
	tag_arr = []
	st = StanfordPOSTagger('english-left3words-distsim.tagger')
	res = st.tag(sen_arr)
	for i in res:
		tag = i[1].encode("utf-8")
		tag_arr.append(tag)

	return tag_arr

def isValid(sen1_arr, sen2_arr):
	sen1_arr_t = []
	sen1_tags_t = []
	sen2_arr_t = []
	sen2_tags_t = []

	sen1_tags = []
	sen2_tags = []
	sen1_tags = getTags(sen1_arr)
	sen2_tags = getTags(sen2_arr)

	for i,v in enumerate(sen1_arr):
		if v in aux_verbs :
			continue
		sen1_arr_t.append(v)
		sen1_tags_t.append(sen1_tags[i])

	for i,v in enumerate(sen2_arr):
		if v in aux_verbs :
			continue
		sen2_arr_t.append(v)
		sen2_tags_t.append(sen2_tags[i])

	#sen1_tags_t = ' '.join(sen1_tags_t).strip()
	#sen2_tags_t = ' '.join(sen2_tags_t).strip()


	result = ca.checkIfUnambigous(sen1_arr_t, sen1_tags_t, sen2_arr_t, sen2_tags_t)

	if result:
		return True

	return False

def formSen(sen_arr, sen_tags):
	sen = ""
	for i,v in enumerate(sen_arr):
		sen += " " + v
	return sen

def printCheck(sentence):
	for i in connectors:
		if i in sentence:
			sentences = sentence.split(i.strip())
			sen1_arr  = sentences[0].strip().split(' ')
			sen2_arr  = sentences[1].strip().split(' ')

			if isValid(sen1_arr, sen2_arr) == False:
				continue
			return True
	return False

def crawlFilesAndCreateTaggedSentences():
	output = open("wiki_sentences.txt", "a")
	paths = ['./corpus/manually_created']
	for path in paths :
		for root, directories, filenames in os.walk(path):
			for filename in filenames:
				if filename.endswith(".txt"):
					with open(os.path.join(root,filename)) as f :
						for line in f :
							line = line.replace('\n','')
							if(line[len(line)-1] == '.'):
								line = line[0:len(line)-1]
							if printCheck(line):
								line = line.replace(',','').replace('-', '').replace('"', '').replace(':', '').strip()
								output.write(line)

if __name__ == '__main__':
    crawlFilesAndCreateTaggedSentences()
