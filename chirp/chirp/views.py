from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import analyzer


@api_view(['GET'])
def analyzed_tweet_list(request):
    print(request)
    serializer = serializers.AnalyzedTweetSerializer(analyzer.runSearchAnalysis(["trump"], count=1), many=True)
    return Response(serializer.data)
