from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from ... import analyzer
from ...models import AnalyzedTweetModel

class Command(BaseCommand):
    help = 'Populate database with sample data'


    def handle(self, *args, **options):

        tweets = analyzer.runSearchAnalysis(["trump"], count=1000)

        for tweet in tweets:
            obj, created = AnalyzedTweetModel.objects.get_or_create(
                twitID=tweet.twitID,
                label=tweet.label,
                longitude=tweet.location[1],
                latitude=tweet.location[0],
                time=tweet.time,
                prob_pos=tweet.prob_pos,
                prob_neg=tweet.prob_neg,
                prob_neu=tweet.prob_neu
            )

            obj.save()

        self.stdout.write(self.style.SUCCESS('Added 1000 tweets related to the keyword trump the database'))
