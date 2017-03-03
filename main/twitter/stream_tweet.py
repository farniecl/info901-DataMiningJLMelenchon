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
    def __init__(self,path,time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open(path, 'a')
        self.tweets = []
        super(StreamTweet, self).__init__()

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            self.tweets.append(json.loads(data))
            return True
        else:
            self.saveFile.write(json.dumps(self.tweets,indent=4, separators=(',',':')))
            self.saveFile.close()
            return False

    def on_error(self, status):
        print(status)