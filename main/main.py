#!/usr/bin/python3

#Import des methodes depuis la bibliothèque tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import os
import json
from pprint import pprint
from twitter.stream_tweet import StreamTweet
from twitter.classifieur import Classifieur

json_file = './ressource/tweets.json'

def update_json(tweets):
    fr = open(json_file,'r')
    file_tweets = json.load(fr)
    fr.close()
    file_tweets.extend(tweets)
    fw = open(json_file, 'w')
    fw.write(json.dumps(file_tweets,indent=4,separators=(',',':')))
    fw.close()

def stream_tweets(tweets):
     # Cles et Access Token pour se connecter à twitter
    access_token = "517636552-0dHeUg75oHdKmLaO2RjFjKlSF5ZJQtcDW7tHfLl3"
    access_token_secret = "QoCIwz8ziMj7NABzxRQqQHGuHlDIdXppJJYdzpV001aWj"
    consumer_key = "Xsd9vLsEmQLqqswUrt0fTOYun"
    consumer_secret = "kIinFrugN04pqNG2DfonwAylbzNmjzFpGVAdwBDxEca1S975Q2"
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StreamTweet(time_limit=20)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['@JLMelenchon'])
    tweets.extend(l.get_tweets())

def pos_neg_app(tweets):
    cl = Classifieur('./ressource/tweets.json')
    for tweet in tweets:
        tweet["sentiment"] = cl.apprentissage(tweet["tweet"])

def pos_neg_ana(tweets):
    cl = Classifieur('./ressource/tweets.json')
    for tweet in tweets:
        tweet["sentiment"] = cl.analyse(tweet["tweet"])

if __name__ == '__main__':
    tweets = []
    stream_tweets(tweets)
    pos_neg_app(tweets)
    update_json(tweets)