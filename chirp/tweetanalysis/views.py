from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models
from . import analyzer


@api_view(['GET'])
def analyzed_tweet_list(request, query):

    tweets = models.AnalyzedTweetModel.objects.filter(search_string=query)

    if(tweets):
        serializer = serializers.AnalyzedTweetModelSerializer(tweets, many=True)
        return Response(serializer.data)
    else:
        tweets = analyzer.runSearchAnalysis([query], count=2)

        for tweet in tweets:
            analyzed_tweet = models.AnalyzedTweetModel()
            analyzed_tweet.search_string = query
            analyzed_tweet.twitID = tweet.twitID
            analyzed_tweet.label = tweet.label
            if(tweet.location != None):
                analyzed_tweet.longitude = tweet.location[1]
                analyzed_tweet.latitude = tweet.location[0]
                analyzed_tweet.state = tweet.location[2]
            analyzed_tweet.time = tweet.time
            analyzed_tweet.prob_pos = tweet.prob_pos
            analyzed_tweet.prob_neg = tweet.prob_neg
            analyzed_tweet.prob_neu =tweet.prob_neu
            analyzed_tweet.save()

        tweets = models.AnalyzedTweetModel.objects.filter(search_string=query)
        serializer = serializers.AnalyzedTweetModelSerializer(tweets, many=True)
        return Response(serializer.data)