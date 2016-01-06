from runCrawler import search_by_domain
from runCrawler import search_by_qa
import sys

def main(argv):
	if(argv[0] == 'qa'):
		print "Question: What is a pointer?"
		print "Answer: A variable that contains the address in memory of another variable."
		search_by_qa('What is a pointer?', 'A variable that contains the address in memory of another variable.')
	elif(argv[0] == 'domain'):
		print "Domain: Art History"
		search_by_domain('Art History')
	else:
		print "Usage: python crawlerCaller.py <qa/domain>"

if __name__ == "__main__":
   main(sys.argv[1:])