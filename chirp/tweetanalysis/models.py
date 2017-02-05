from django.db import models

class AnalyzedTweetModel(models.Model):

    POSITIVE = 'pos'
    NEGATIVE = 'neg'
    NEUTRAL = 'neutral'

    SENTIMENT_CHOICES = (
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative'),
        (NEUTRAL, 'Neutral')
    )

    twitID = models.IntegerField()
    label = models.CharField(choices=SENTIMENT_CHOICES, max_length=15)
    longitude = models.FloatField()
    latitude = models.FloatField()
    time = models.CharField(max_length=200)
    prob_pos = models.FloatField()
    prob_neg = models.FloatField()
    prob_neu = models.FloatField()
