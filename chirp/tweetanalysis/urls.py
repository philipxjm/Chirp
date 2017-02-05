from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^', views.analyzed_tweet_list_trump),
]



