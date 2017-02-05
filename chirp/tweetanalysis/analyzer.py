from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json
import requests
from TwitterAPI import TwitterAPI

class AnalyzedTweet(object):
	"""docstring for AnalyzedTweet"""
	def __init__(self, twitID, location, time, label, prob_pos, prob_neg, prob_neu):
		self.twitID = twitID
		self.location = location
		self.time = time
		self.label = label
		self.prob_pos = prob_pos
		self.prob_neg = prob_neg
		self.prob_neu = prob_neu

	def __str__(self):
		return "{twitID: " + str(self.twitID) + ", location: " + str(self.location) + ", label: " + str(self.label) + ", prob_pos: " + str(self.prob_pos) + ", prob_neg: " + str(self.prob_neg) + ", prob_neu: " + str(self.prob_neu) + "}"

def geocode(locStr):
	api = "AIzaSyBZ68_Iz3U1Wpdo18viv0lV4X0PGO79jhg"
	url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + locStr + "&key= " + api
	# print(url)
	r = requests.get(url)
	if r.json()["status"] == "OK":
		# print(r.json())
		address = r.json()["results"][0]["address_components"]
		for x in range(0, len(address)):
			state = address[x]["types"][0]
			if state == "administrative_area_level_1":
				return [r.json()["results"][0]["geometry"]["location"]["lat"], r.json()["results"][0]["geometry"]["location"]["lng"], r.json()["results"][0]["address_components"][x]["long_name"]]
	else:
		return "BAD. DISCARD."

def analyze(tweets):
	analyzedTweets = []
	url = "http://text-processing.com/api/sentiment/"
	for tweet in tweets:
		post_fields = {'text': tweet[1]}
		request = Request(url, urlencode(post_fields).encode())
		result = json.loads(urlopen(request).read().decode())
		analyzedTweet = AnalyzedTweet(tweet[0],
			tweet[2],
			tweet[3],
			result["label"],
			result["probability"]["pos"],
			result["probability"]["neg"],
			result["probability"]["neutral"])
		print(analyzedTweet)
		analyzedTweets.append(analyzedTweet)
	return analyzedTweets

def search(keyword, count):
	tweets = []
	api = TwitterAPI("sNjj2O9xgtclg2l4Y3batJNmD", "iKMk9pye8bBZLPzGBupCco2cEVKG8buESq4m2UUuaI5Br7c1RH", "2382398376-zmcPodEblLN3v3aiJ1uHoEAAJp2XJQ5lDO7xc5a", "17X7Dk2LrWY4BEUhsBsjtciSCGJXdslNSRqk4hmWfebhg")

	for i in range(0,4):
		if i != 0:
			max_id = tweets[-1][4]
			r = api.request('search/tweets', {'q':keyword, 'count': count, 'lang': 'en', 'max_id': max_id})
		else:
			r = api.request('search/tweets', {'q':keyword, 'count': count, 'lang': 'en'})

		total = 0
		tossed = 0
		for tweet in r:
			# print(tweet)

			geo = geocode(tweet["user"]["location"])
			if geo != "BAD. DISCARD.":
				total += 1
				tweets.append([tweet["id_str"], 
					tweet["text"], 
					geo,
					tweet["created_at"],
					tweet["id"]])
			else:
				total += 1
				tossed += 1
				print("total: " + str(total) + " tossed: " + str(tossed))

		print(tweets[-1])

	return tweets

def runSearchAnalysis(keyword, count):
	return analyze(search(keyword, count))

#runSearchAnalysis(["trump"], 1000)
# print(geocode("new york city"))
