# -*- coding: utf-8 -*-
import os
import nltk

def get_words_in_tweets(tweets):
        all_words = []
        for (words, sentiment) in tweets:
            all_words.extend(words)
        return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

class Classifieur():
    def __init__(self):
        self.pos_tweets = []
        self.neg_tweets = []
        self.tweets = []
        f = open('ressource/positive.txt','r')
        for line in f:
            self.pos_tweets.append((line,'positive'))
        f.close()
        f2 = open('ressource/negative.txt','r')
        for line in f2:
            self.neg_tweets.append((line,'negative'))
        f2.close()
        for (words, sentiment) in self.pos_tweets + self.neg_tweets:
            words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
            self.tweets.append((words_filtered, sentiment))
        self.word_features = get_word_features(get_words_in_tweets(self.tweets))

    def init_classifier(self):
        def extract_features(self,document):
            document_words = set(document)
            features = {}
            for word in self.word_features:
                features['contains(%s)' % word] = (word in document_words)
            return features
        training_set = nltk.classify.apply_features(extract_features, self.tweets)
        self.classifier = nltk.NaiveBayesClassifier.train(training_set)

    def apprentissage(self,string_a_tester):
            result = self.classifier.classify(self.extract_features(string_a_tester.split()))
            append_pos = open('ressource/positive.txt','a')
            append_neg = open('ressource/negative.txt','a')
            print (string_a_tester + " semble " + result)
            verif = raw_input("Comment est le texte? P(positif)/N(négatif)/I(inclassable)")
            if str(verif)=="p":
                print ("texte positif")
                append_neg.write('\n')
                append_pos.write(string_a_tester)
            elif str(verif)=="n":
                print ("texte negatif")
                append_neg.write('\n')
                append_neg.write(string_a_tester)
            else:
                print ("texte passé")
            append_pos.close()
            append_neg.close()
            return result

    def analyse(self,string_a_tester):
            result = self.classifier.classify(self.extract_features(string_a_tester.split()))
            append_pos = open('ressource/positive.txt','a')
            append_neg = open('ressource/negative.txt','a')
            if result=='positive':
                append_pos.write(string_a_tester)
                append_neg.write('\n')
            else:
                append_neg.write(string_a_tester)
                append_neg.write('\n')
            append_pos.close()
            append_neg.close()
            return result
    
# texte de test
