import sys
import os
from os import listdir
from os.path import isfile, join
from stopWordRemove.removeStopWords import find_content_words
from google import search

def googleSearch(query, stop):
	for url in search(query, stop=5):
		with open('domains.txt', 'ab') as f:
			f.write(url + '\n')

def search_by_domain(domain):
	url = 'https://en.wikipedia.org/wiki/' + '_'.join(domain.split(' '))
	with open('domains.txt', 'ab') as f:
		f.write('DOMAIN' + '\n')
		f.write('_'.join(domain.split(' ')) + '\n')
		f.write(url + '\n')
	os.system('mkdir ' + '_'.join(domain.split(' ')))
	os.system('scrapy crawl wiki')

def search_by_qa(question, answer):
	question_content = find_content_words(question)
	answer_content = find_content_words(answer)
	all_content = ' '.join(question_content) + ' ' + ' '.join(answer_content)
	query = all_content + ' site:wikipedia.org'
	with open('domains.txt', 'ab') as f:
			f.write('QA' + '\n')
	googleSearch(query, 5)
	os.system('mkdir pages')
	os.system('scrapy crawl wiki')

def data_as_string():
	result = ''
	data_dir = './pages/'
	file_names = \
        [f for f in listdir(data_dir) if isfile(join(data_dir, f))]
	for file_name in file_names:
	    file_name = data_dir + file_name
	    f = open(file_name)
	    for line in f.readlines():
	    	result += line
	os.system('rm -rf pages')
	# print result
	return result

#--------------------------Exmaple Function Calls---------------------------------
# search_by_domain('history')
# search_by_qa('How many constructors can be created for a class?', 'Unlimited number.')
# data_as_string()


#--------------------------Old Main---------------------------------
# def main(argv):
# 	all_dict = defaultdict(list)
# 	all_input_string = ' '.join(argv[1:])
# 	query = ''

# 	if(argv[0] == '-d'):
# 		url = 'https://en.wikipedia.org/wiki/' + ' '.join(argv[1:])
# 		print url
# 		with open('domains.txt', 'ab') as f:
# 			f.write(url + '\n')

# 	elif(argv[0] == '-q'):
# 		question = all_input_string.split('?')[0].strip()
# 		answer = all_input_string.split('?')[1].strip()
# 		question_content = find_content_words(question)
# 		answer_content = find_content_words(answer)
# 		all_content = ' '.join(question_content) + ' ' + ' '.join(answer_content)
# 		query = all_content + ' site:wikipedia.org'
# 		print query
# 		googleSearch(query)

# 	else:
# 		"Please specify the type of input using the '-d' or '-q' flag."

# 	os.system('scrapy crawl wiki')

# if __name__ == "__main__":
#    main(sys.argv[1:])


#--------------------------Print Question,Answer,Content Words---------------------------------
# questions = argv[0]
# answers = argv[1]
# for line in open(questions, 'r').readlines():
# 	all_dict[line.split(' ')[0]].append(' '.join(line.split(' ')[1:]))
# for line in open(answers, 'r').readlines():
# 	all_dict[line.split(' ')[0]].append(' '.join(line.split(' ')[1:]))

# for item in all_dict:
# 	print item
# 	question_content_words = find_content_words(all_dict[item][0].strip())
# 	answer_content_words = find_content_words(all_dict[item][1].strip())		
# 	content_words_string = ' '.join(question_content_words) + ' ' + ' '.join(answer_content_words) 
# 	all_dict[item].append(content_words_string)
        
# for item in all_dict:
# 	for output in all_dict[item]:
# 		with open('question-answer-content', 'ab') as f:
# 			f.write(output)
# 	with open('question-answer-content', 'ab') as f:
# 			f.write('\n\n')