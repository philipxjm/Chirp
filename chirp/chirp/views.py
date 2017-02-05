# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from chirp.tweetanalysis import serializers
# from . import analyzer
# from ..tweetanalysis.models import AnalyzedTweetModel
#
#
# @api_view(['GET'])
# def analyzed_tweet_list(request, search_arg):
#     serializer = serializers.AnalyzedTweetSerializer(analyzer.runSearchAnalysis([search_arg], count=100), many=True)
#     return Response(serializer.data)
#

