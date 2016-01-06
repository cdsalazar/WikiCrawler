from config import *
from coreNlpUtil import *

def find_content_words(sentence):
	sentence_parse_result = parseText(sentence)
	sentence_lemmatized = lemmatize(sentence_parse_result)
	sentence_words = [item[2] for item in sentence_lemmatized]
	sentence_content_words = [item for item in sentence_words \
									if item.lower() not in stop_words+punctuations]
	return sentence_content_words


# sentence = "What is the main difference between a string of characters that is read into a variable of type string versus a variable of type char?"
# print find_content_words(sentence)