from rest_framework import serializers, viewsets
from . import models
# from chirp.tweetanalysis.models import AnalyzedTweetModel

# class AnalyzedTweetSerializer(serializers.Serializer):
#
#     twitID = serializers.IntegerField()
#     label = serializers.ChoiceField(["pos", "neg", "neutral"])
#     location = serializers.ListField(child=serializers.FloatField())
#     time = serializers.CharField(max_length=200)
#     prob_pos = serializers.DecimalField(None, decimal_places=3, coerce_to_string=False)
#     prob_neg = serializers.DecimalField(None, decimal_places=3, coerce_to_string=False)
#     prob_neu = serializers.DecimalField(None, decimal_places=3, coerce_to_string=False)

class AnalyzedTweetModelSerializer(serializers.ModelSerializer):
     class Meta:
        model = models.AnalyzedTweetModel
        fields = ('twitID', 'label', 'latitude', 'longitude', 'time', 'prob_pos', 'prob_neg', 'prob_neu')

