from rest_framework import serializers, viewsets

class AnalyzedTweetSerializer(serializers.Serializer):

    twitID = serializers.IntegerField()
    label = serializers.ChoiceField(["pos", "neg"])
    prob_pos = serializers.DecimalField(None, decimal_places=3, coerce_to_string=False)
    prob_neg = serializers.DecimalField(None, decimal_places=3, coerce_to_string=False)
    prob_neu = serializers.DecimalField(None, decimal_places=3, coerce_to_string=False)
