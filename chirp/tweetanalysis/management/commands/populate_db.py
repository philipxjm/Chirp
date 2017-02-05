from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from ... import analyzer
from ...models import AnalyzedTweetModel

class Command(BaseCommand):
    help = 'Populate database with sample data'


    def handle(self, *args, **options):

        tweets = analyzer.runSearchAnalysis(["trump"], count=1000)

        for tweet in tweets:
            tweet_with_id = AnalyzedTweetModel.objects.filter(twitID=tweet.twitID)
            print(tweet_with_id)
            if(not tweet_with_id):
                print("get a tweet")
                analyzed_tweet = AnalyzedTweetModel()
                analyzed_tweet.search_string = "trump"
                analyzed_tweet.twitID = tweet.twitID
                analyzed_tweet.label = tweet.label
                if(tweet.location != None):
                    analyzed_tweet.longitude = tweet.location[1]
                    analyzed_tweet.latitude = tweet.location[0]
                    analyzed_tweet.state = tweet.location[2]
                analyzed_tweet.time = tweet.time
                analyzed_tweet.prob_pos = tweet.prob_pos
                analyzed_tweet.prob_neg = tweet.prob_neg
                analyzed_tweet.prob_neu = tweet.prob_neu
                analyzed_tweet.save()

        self.stdout.write(self.style.SUCCESS('Added 1000 tweets related to the keyword trump the database'))
