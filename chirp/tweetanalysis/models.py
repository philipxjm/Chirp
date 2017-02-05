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

    search_string = models.CharField(max_length=200, default="")
    twitID = models.IntegerField(default=0)
    label = models.CharField(choices=SENTIMENT_CHOICES, max_length=15, default='neutral')
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    time = models.CharField(max_length=200, default="")
    prob_pos = models.FloatField(default=0)
    prob_neg = models.FloatField(default=0)
    prob_neu = models.FloatField(default=0)
