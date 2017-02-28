#!/usr/bin/python3

#Import des methodes depuis la bibliothèque tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Cles et Access Token pour se connecter à twitter
access_token = "517636552-0dHeUg75oHdKmLaO2RjFjKlSF5ZJQtcDW7tHfLl3"
access_token_secret = "QoCIwz8ziMj7NABzxRQqQHGuHlDIdXppJJYdzpV001aWj"
consumer_key = "Xsd9vLsEmQLqqswUrt0fTOYun"
consumer_secret = "kIinFrugN04pqNG2DfonwAylbzNmjzFpGVAdwBDxEca1S975Q2"


# Méthode qui lit une donnée reçue et l'affiche dans la console
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['@JLMelenchon'])