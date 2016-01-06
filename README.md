# A Wikipedia Web Crawler

This is a Wikipedia web crawler with two different functions:
(1) Given a domain word ('Computer Science', 'Art History', 'Literature', etc.), it will retrieve the wikipedia page for the given domain and use it as a start url. It will then crawl to all other pages linked in the page. It will create a directory inside of a previously created directory, "Domain_Docs", then fill it with all crawled pages.

(2) Given a question and an answer, it will query google.com with content words of both sentences, while limiting the results to only Wikipedia domains. It will collect the top 5 urls and use them as starting urls from which it will crawl to further Wikipedia pages. It will create and fill a directory called 'pages/' with nicely formatted text files of each Wikipedia page it crawls.

(2.5) There is a small function which will turn all text files in the 'pages/' directory into a single string and return that string.


## Requirements

1) Python **NLTK** 
2) The [Python wrapper for Stanford CoreNLP](https://github.com/dasmith/stanford-corenlp-python) 
3) Scrapy
4) BeautifulSoup
5) Google (pip install google)


## Installation and Usage

1) Install the above tools. 
2) Change line 100 of corenlp.py, from "rel, left, right = map(lambda x: remove_id(x), split_entry)" to "rel, left, right = split_entry". 
3) Download the NLTK stopword corpus: 

	python -m nltk.downloader stopwords
4) Install jsonrpclib: 

	sudo pip install jsonrpclib
5) Download the aligner: 

	  git clone https://github.com/ma-sultan/monolingual-word-aligner.git  
6) Run the corenlp.py script to launch the server: 

	  python corenlp.py  
7) Open new terminal and cd into wikiCrawler directory, then run:
	  
	  python callerCrawler.py qa
	  ------------or------------
	  python callerCrawler.py domain