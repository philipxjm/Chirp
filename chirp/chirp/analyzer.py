from urllib.parse import urlencode
from urllib.request import Request, urlopen
from TwitterSearch import *
import json
import pickle

from TwitterAPI import TwitterAPI
api = TwitterAPI("sNjj2O9xgtclg2l4Y3batJNmD", "iKMk9pye8bBZLPzGBupCco2cEVKG8buESq4m2UUuaI5Br7c1RH", "2382398376-zmcPodEblLN3v3aiJ1uHoEAAJp2XJQ5lDO7xc5a", "17X7Dk2LrWY4BEUhsBsjtciSCGJXdslNSRqk4hmWfebhg")
r = api.request('search/tweets', {'q':'pizza'})
for item in r:
        print(item)

class AnalyzedTweet(object):
	"""docstring for AnalyzedTweet"""
	def __init__(self, twitID, location, label, prob_pos, prob_neg, prob_neu):
		self.twitID = twitID
		self.location = location
		self.label = label
		self.prob_pos = prob_pos
		self.prob_neg = prob_neg
		self.prob_neu = prob_neu

	def toString(self):
		return "{twitID: " + str(self.twitID) + ", location: " + str(self.location) + ", label: " + str(self.label) + ", prob_pos: " + str(self.prob_pos) + ", prob_neg: " + str(self.prob_neg) + ", prob_neu: " + str(self.prob_neu) + "}"

def analyze(tweets):
	analyzedTweets = []
	url = "http://text-processing.com/api/sentiment/"
	for tweet in tweets:
		post_fields = {'text': tweet[1]}
		request = Request(url, urlencode(post_fields).encode())
		result = json.loads(urlopen(request).read().decode())
		analyzedTweet = AnalyzedTweet(tweet[0],
			tweet[2],
			result["label"], 
			result["probability"]["pos"], 
			result["probability"]["neg"], 
			result["probability"]["neutral"])
		print(analyzedTweet.toString())
		analyzedTweets.append(analyzedTweet)
	return analyzedTweets

def search(keywords, count=100):
	tweets = []

	api = TwitterAPI("sNjj2O9xgtclg2l4Y3batJNmD", "iKMk9pye8bBZLPzGBupCco2cEVKG8buESq4m2UUuaI5Br7c1RH", "2382398376-zmcPodEblLN3v3aiJ1uHoEAAJp2XJQ5lDO7xc5a", "17X7Dk2LrWY4BEUhsBsjtciSCGJXdslNSRqk4hmWfebhg")
	r = api.request('search/tweets', {'q':'pizza'})

	for tweet in r:
		# print(tweet)
		# tweets.append(tweet)
		tweets.append([tweet["id_str"], 
			tweet["text"], 
			tweet["user"]["location"]])

	pickle.dump(tweets, open("tweets.p", "wb" ) )
	return tweets

def runSearchAnalysis(keywords, count=100):
	return analyze(search(keywords, count))

# runSearchAnalysis(["trump"], 10)
