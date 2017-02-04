from urllib.parse import urlencode
from urllib.request import Request, urlopen
from TwitterSearch import *
import json

class AnalyzedTweet(object):
	"""docstring for AnalyzedTweet"""
	def __init__(self, twitID, label, prob_pos, prob_neg, prob_neu):
		self.twitID = twitID
		self.label = label
		self.prob_pos = prob_pos
		self.prob_neg = prob_neg
		self.prob_neu = prob_neu

def analyze(tweets):
	analyzedTweets = []
	url = "http://text-processing.com/api/sentiment/"
	for tweet in tweets:
		post_fields = {'text': tweet[1]}
		request = Request(url, urlencode(post_fields).encode())
		result = json.loads(urlopen(request).read().decode())
		print(result["probability"])
		analyzedTweets.append(AnalyzedTweet(tweet[0],
			result["label"], 
			result["probability"]["pos"], 
			result["probability"]["neg"], 
			result["probability"]["neutral"]))
	return analyzedTweets

def search(keywords, count=100):
	tweets = []
	try:
		tso = TwitterSearchOrder()
		tso.set_keywords(keywords)
		tso.set_language('en')
		tso.set_include_entities(False)
		tso.set_count(count)

		ts = TwitterSearch(
			consumer_key = 
			'A9XcMbJQNoc5UuDDQqYhDIkDi',
			consumer_secret = 
			'cfDMXwwCs3Pf3jyu551dQCIKxpaVQwuDWPsqYtNZ3J4dTfatiI',
			access_token = 
			'2155608048-Tmj6JM6b5KEprwvPsShtpBaL6JiwheWt07qlt7F',
			access_token_secret = 
			'3MnKXHa21eZFmrj8tNKfdhIISJLDN5wprZHTZEAkvsNL6'
		)

		for tweet in ts.search_tweets_iterable(tso):
			# print(tweet['text'])
			tweets.append([tweet["id_str"], tweet["text"]])

	except TwitterSearchException as e:
		print(e)

	return tweets

def runSearchAnalysis(keywords, count=100):
	return analyze(search(keywords, count))

# print(runSearchAnalysis(["trump"], 10))
