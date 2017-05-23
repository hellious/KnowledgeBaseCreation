import re
import unittest

NOUNS = '(NN|NNS|NNP|NNPS)'
VERBS = '(VB|VBD|VBG|VBN|VBP|VBZ)'
NN_VB = '(NN|NNS|NNP|NNPS|VB|VBD|VBG|VBN|VBP|VBZ)'
NN_ADJ = '(NN|NNS|NNP|NNPS|JJ|JJR|JJS)'
PR_VB = '(PRP|PRP\$|VB|VBD|VBG|VBN|VBP|VBZ)'
PR_ADJ = '(PRP|PRP\$|JJ|JJR|JJS)'
PR_NN = '(PRP|PRP\$|NN|NNS|NNP|NNPS)'
PR_NN_VB = '(PRP|PRP\$|NN|NNS|NNP|NNPS|VB|VBD|VBG|VBN|VBP|VBZ)'
PR_NN_ADJ = '(PRP|PRP\$|NN|NNS|NNP|NNPS|JJ|JJR|JJS)'
PRONOUN = '(PRP|PRP\$)'
ADJ = '(JJ|JJR|JJS)'

PR_SYN = {	'he' : set(['he','him','his','himself']),
			'him' : set(['he','him','his','himself']),
			'his' : set(['he','him','his','himself']),
			'himself' : set(['he','him','his','himself']),
			'she' : set(['she','her','hers','herself']),
			'her' : set(['she','her','hers','herself']),
			'hers' : set(['she','her','hers','herself']),
			'herself' : set(['she','her','hers','herself']),
			'it' : set(['she','her','hers','herself']),
			'its' : set(['she','her','hers','herself']),
			'itself' : set(['she','her','hers','herself']),
			'they' : set(['they','them','their','theirs', 'themselves']),
			'them' : set(['they','them','their','theirs', 'themselves']),
			'their' : set(['they','them','their','theirs', 'themselves']),
			'theirs' : set(['they','them','their','theirs', 'themselves']),
			'themselves' : set(['they','them','their','theirs', 'themselves']) }

def verbose(check, str):
	if check:
		#print str
		pass

def checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	print sentence1Words, sentence1POSs, sentence2Words, sentence2POSs
	result = False
	#try:
	check1 = checkNVNAndNV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check1, 'checkNVNAndNV')
	check2 = checkNVNAndVN(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check2, 'checkNVNAndVN')
	check3 = checkPVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check3, 'checkPVPAndPV')
	check4 = checkPVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check4, 'checkPVPAndVP')
	check5 = checkPVNAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check5, 'checkPVNAndPV')
	check6 = checkPVNAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check6, 'checkPVNAndVP')
	check7 = checkNVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check7, 'checkNVPAndPV')
	check8 = checkNVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check8, 'checkNVPAndVP')
	check9 = checkNVNAndNA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check9, 'checkNVNAndNA')
	check10 = checkNVNAndAN(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check10, 'checkNVNAndAN')
	check11 = checkPVPAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check11, 'checkPVPAndPA')
	check12 = checkPVPAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check12, 'checkPVPAndAP')
	check13 = checkPVNAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check13, 'checkPVNAndPA')
	check14 = checkPVNAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check14, 'checkPVNAndAP')
	check15 = checkNVPAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check15, 'checkNVPAndPA')
	check16 = checkNVPAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs)
	verbose(check16, 'checkNVPAndAP')

	result = check1 or check2 or check3 or check4 or check5 or check6 or check7 or check8 or check9 or check10 or check11 or check12 or check13 or check14 or check15 or check16
	# except Exception as e:
	# 	print ">>Exception :", e
	print result
	return result

def checkNVNAndNV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	#print 'here'
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS +'(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*'+ VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	#print searchObj1 , searchObj2
	if searchObj1 and searchObj2:
		val = list(set(NOUNS[1:len(NOUNS)-1].split('|')).intersection(sentence1POSs))[0]
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if nounWordinSentence2.strip() == i.strip()]
		if len(multiple) == 1:
			return True

	return False

def checkNVNAndVN(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(NOUNS[1:len(NOUNS)-1].split('|')).intersection(sentence1POSs))[0]
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if nounWordinSentence2.strip() == i.strip()]
		if len(multiple) == 1:
			return True

	return False

def exists(sentenceWord, pronounWordinSentence2):
	sentenceWord = sentenceWord.strip()
	pronounWordinSentence2 = pronounWordinSentence2.strip()
	if sentenceWord in PR_SYN:
		if pronounWordinSentence2 in PR_SYN[sentenceWord]:
			return True
	return False

def checkPVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False

def checkPVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False

def checkPVNAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False

def checkPVNAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' +  VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False

def checkNVPAndPV(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False

def checkNVPAndVP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' +  VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False


def checkNVNAndNA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS +'(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*'+ ADJ + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(NOUNS[1:len(NOUNS)-1].split('|')).intersection(sentence1POSs))[0]
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]
		multiple = [1 for i in sentence1Words if nounWordinSentence2.strip() == i.strip()]
		if len(multiple) == 1:
			return True

	return False

def checkNVNAndAN(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + ADJ + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(NOUNS[1:len(NOUNS)-1].split('|')).intersection(sentence1POSs))[0]
		nounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if nounWordinSentence2.strip() == i.strip()]
		if len(multiple) == 1:
			return True

	return False

def checkPVPAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + ADJ + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False

def checkPVPAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + ADJ + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False

def checkPVNAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + ADJ + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False

def checkPVNAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' +  ADJ + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False

def checkNVPAndPA(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + ADJ + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False

def checkNVPAndAP(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs):
	sentence1Pattern = '^' + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + NOUNS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + VERBS + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|JJ|JJR|JJS|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	sentence2Pattern = '^' + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' +  ADJ + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + PRONOUN + '(IN|DT|LS|MD|PDT|POS|RB|RBR|RBS|RP|SYM|TO|UH|WDT|WP|WP\$|WRB|\s)*' + '$'
	searchObj1 = re.search(sentence1Pattern, " ".join(sentence1POSs))
	searchObj2 = re.search(sentence2Pattern, " ".join(sentence2POSs))
	if searchObj1 and searchObj2:
		val = list(set(['PRP','PRP$']).intersection(sentence2POSs))[0]
		pronounWordinSentence2 = sentence2Words[sentence2POSs.index(val)]

		multiple = [1 for i in sentence1Words if exists(pronounWordinSentence2, i)]
		if len(multiple) == 1:
			return True

	return False


class TestSentences(unittest.TestCase):

    def test_case_1(self):
    	sentence1Words = ['kevin', 'yelled', 'at', 'john']
    	sentence1POSs = ['NNP', 'VBD', 'IN', 'NN']
    	sentence2Words = ['john', 'upset']
    	sentence2POSs = ['NN', 'JJ']
    	self.assertTrue(checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs))

    def test_case_2(self):
    	sentence1Words = ['kevin', 'yelled', 'at', 'john']
    	sentence1POSs = ['NNP', 'VBD', 'IN', 'NN']
    	sentence2Words = ['john', 'ran']
    	sentence2POSs = ['NN', 'VBD']
    	self.assertTrue(checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs))

    def test_case_3(self):
    	sentence1Words = ['he', 'yelled', 'at', 'him']
    	sentence1POSs = ['PRP', 'VBD', 'IN', 'PRP']
    	sentence2Words = ['he', 'upset']
    	sentence2POSs = ['PRP', 'JJ']
    	self.assertFalse(checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs))

    def test_case_4(self):
    	sentence1Words = ['he', 'yelled', 'at', 'him']
    	sentence1POSs = ['PRP', 'VBD', 'IN', 'PRP']
    	sentence2Words = ['he', 'ran']
    	sentence2POSs = ['PRP', 'VBD']
    	self.assertFalse(checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs))

    def test_case_5(self):
    	sentence1Words = ['kevin', 'yelled', 'at', 'him']
    	sentence1POSs = ['NN', 'VBD', 'IN', 'PRP']
    	sentence2Words = ['he', 'ran']
    	sentence2POSs = ['PRP', 'VBD']
    	self.assertTrue(checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs))

    def test_case_6(self):
    	sentence1Words = ['the', 'sculpture', 'rolled', 'off', 'the', 'shelf']
    	sentence1POSs = ['DT', 'NN', 'VBD', 'RP', 'DT', 'NN']
    	sentence2Words = ['it', 'not', 'anchored']
    	sentence2POSs = ['PRP', 'RB', 'VBN']
    	self.assertFalse(checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs))

    def test_case_7(self):
    	sentence1Words = ['the', 'sculpture', 'rolled', 'off', 'the', 'shelf']
    	sentence1POSs = ['DT', 'NN', 'VBD', 'RP', 'DT', 'NN']
    	sentence2Words = ['the','sculpture', 'not', 'anchored']
    	sentence2POSs = ['DT', 'NN', 'RB', 'VBN']
    	self.assertTrue(checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs))

    def test_case_8(self):
    	sentence1Words = ['trophy', 'not', 'fit', 'in', 'brown', 'suitcase']
    	sentence1POSs = ['NN', 'RB', 'VB', 'IN', 'JJ', 'NN']
    	sentence2Words = ['trophy', 'too', 'big']
    	sentence2POSs = ['NN', 'RB', 'JJ']
    	self.assertTrue(checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs))

    def test_case_9(self):
    	sentence1Words = ['trophy', 'not', 'fit', 'in', 'brown', 'suitcase']
    	sentence1POSs = ['NN', 'RB', 'VB', 'IN', 'JJ', 'NN']
    	sentence2Words = ['suitcase', 'too', 'small']
    	sentence2POSs = ['NN', 'RB', 'JJ']
    	self.assertTrue(checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs))

    def test_case_10(self):
    	sentence1Words = ['trophy', 'not', 'fit', 'in', 'brown', 'suitcase']
    	sentence1POSs = ['NN', 'RB', 'VB', 'IN', 'JJ', 'NN']
    	sentence2Words = ['it', 'too', 'small']
    	sentence2POSs = ['PRP', 'RB', 'JJ']
    	self.assertFalse(checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs))

    # def test_case_11(self):
    # 	sentence1Words = ['I', 'like', 'Tom']
    # 	sentence1POSs = ['NN', 'RB', 'VB', 'IN', 'JJ', 'NN']
    # 	sentence2Words = ['it', 'too', 'small']
    # 	sentence2POSs = ['PRP', 'RB', 'JJ']
    # 	self.assertFalse(checkIfUnambigous(sentence1Words, sentence1POSs, sentence2Words, sentence2POSs))


if __name__ == '__main__':
    unittest.main()
