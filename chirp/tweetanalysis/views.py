from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers
from . import models

# Create your views here.
@api_view(['GET'])
def analyzed_tweet_list_trump(request):
    tweets = models.AnalyzedTweetModel.objects.all()
    serializer = serializers.AnalyzedTweetModelSerializer(tweets, many=True)
    return Response(serializer.data)
