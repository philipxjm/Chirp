from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import analyzer


@api_view(['GET'])
def analyzed_tweet_list(request, search_arg):
    serializer = serializers.AnalyzedTweetSerializer(analyzer.runSearchAnalysis([search_arg], count=10), many=True)
    return Response(serializer.data)
