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
if __name__ == '__main__':
    # Cles et Access Token pour se connecter à twitter
    access_token = "517636552-0dHeUg75oHdKmLaO2RjFjKlSF5ZJQtcDW7tHfLl3"
    access_token_secret = "QoCIwz8ziMj7NABzxRQqQHGuHlDIdXppJJYdzpV001aWj"
    consumer_key = "Xsd9vLsEmQLqqswUrt0fTOYun"
    consumer_secret = "kIinFrugN04pqNG2DfonwAylbzNmjzFpGVAdwBDxEca1S975Q2"
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StreamTweet("ressource/tweets.json",time_limit=20)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['@JLMelenchon'])
    with open("ressource/tweets.json", 'r') as f:
        tweets = json.load(f)
        for tweet in tweets:
            pprint(tweet["text"])
        #test = Classifieur()
        #test.init_classifier()
        #test.apprentissage()
    #for line in f:
    #tweets.append(json.loads(line))
    #f = json.load(open("ressource/tweets.json").read())
    #test = Classifieur()
    #test.init_classifier(),indent=4, separators=(',',,indent=4, separators=(',',':'),indent=4, separators=(',',':')':')
    #for tweet in f:
    #print(tweet.text)   
    #f.close()
    #tweet = 'Bruno Lauret'
    #print (analyse(tweet))