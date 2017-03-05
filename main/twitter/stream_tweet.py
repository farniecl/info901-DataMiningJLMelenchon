#!/usr/bin/python3

#Import des methodes depuis la bibliothèque tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import os
import json

# Méthode qui lit une donnée reçue et l'affiche dans la console
class StreamTweet(StreamListener):
    def __init__(self,time_limit=60):
        self.__start_time = time.time()
        self.__limit = time_limit
        self.__tweets = []
        super(StreamTweet, self).__init__()

    def on_data(self, data):
        if (time.time() - self.__start_time) < self.__limit:
            self.__tweets.append(json.loads(data))
            return True
        else:
            return False

    def on_error(self, status):
        print(status)

    def get_tweets(self):
        tmp_tweets = []
        for tweet in self.__tweets:
            tmp_tweets.append({"tweet":tweet["text"]})
        return tmp_tweets