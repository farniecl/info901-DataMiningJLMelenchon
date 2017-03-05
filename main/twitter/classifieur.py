# -*- coding: utf-8 -*-
import os
#import sys
import nltk
import json

class Classifieur():
    def __init__(self,path):
        def get_words_in_tweets(tweets):
            all_words = []
            for (words, sentiment) in tweets:
                all_words.extend(words)
            return all_words
        def get_word_features(wordlist):
            wordlist = nltk.FreqDist(wordlist)
            word_features = wordlist.keys()
            return word_features    
        f = open(path,'r')
        tmp_tweets = json.load(f)
        f.close()
        self.__tweets = []
        for tweet in tmp_tweets:
            words_filtered = [e.lower() for e in tweet["tweet"].split() if len(e) >= 3] 
            self.__tweets.append((words_filtered, tweet["sentiment"]))        
        self.__word_features = get_word_features(get_words_in_tweets(self.__tweets))

    def __classifieur_analyse(self,string_a_tester):
        def extract_features(document):
            document_words = set(document)
            features = {}
            for word in self.__word_features:
                features['contains(%s)' % word] = (word in document_words)
            return features
        training_set = nltk.classify.apply_features(extract_features, self.__tweets)
        classifier = nltk.NaiveBayesClassifier.train(training_set)
        return classifier.classify(extract_features(string_a_tester.split()))

    def analyse(self,string_a_tester):
            result = self.__classifieur_analyse(string_a_tester)
            if result=='positive':
                return 'positive'
            elif result=='positive':
                return 'negative'
            else:
                return 'neutre'

    def apprentissage(self,string_a_tester):
            if self.__tweets:
                result = self.__classifieur_analyse(string_a_tester)
                print (string_a_tester + " semble " + result)
            else:
                print (string_a_tester)     
            verif = input("Comment est le texte? P(positif)/N(négatif)/I(inclassable)")
            if str(verif)=="p":
                print ("texte positif")
                return 'positive'
            elif str(verif)=="n":
                print ("texte negatif")
                return 'negative'
            else:
                print ("texte inclassable")
                return 'neutre'