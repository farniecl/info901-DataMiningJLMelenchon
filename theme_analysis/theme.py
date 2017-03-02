# -*- coding: utf-8 -*-
import os
import nltk

pos_tweets = []
neg_tweets = []

f = open('travail.txt','r')
for line in f:
    pos_tweets.append((line,'travail'))
f.close()

f2 = open('europe.txt','r')
for line in f2:
    neg_tweets.append((line,'europe'))
f2.close()

tweets = []
for (words, theme) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, theme))

def get_words_in_tweets(tweets):
    all_words = []
    for (words, theme) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


word_features = get_word_features(get_words_in_tweets(tweets))

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)

def analyse(string_a_tester):
        result = classifier.classify(extract_features(string_a_tester.split()))
        append_travail = open('travail.txt','a')
        append_europe = open('europe.txt','a')
        if result=='travail':
            append_travail.write(string_a_tester)
            append_travail.write('\n')
        else:
            append_europe.write(string_a_tester)
            append_europe.write('\n')
        append_travail.close()
        append_europe.close()
        return result

def apprentissage(string_a_tester):
        result = classifier.classify(extract_features(string_a_tester.split()))
        append_travail = open('travail.txt','a')
        append_europe = open('europe.txt','a')
        print (string_a_tester + " semble " + result)
        verif = input("Quel est le theme du texte? t(travail)/e(europe)/i(inclassable)")
        if str(verif)=="t":
            print ("texte travail")
            append_travail.write(string_a_tester)
            append_travail.write('\n')
        elif str(verif)=="e":
            print ("texte europe")
            append_europe.write(string_a_tester)
            append_europe.write('\n')
        else:
            print ("texte passé")
        append_travail.close()
        append_europe.close()
        return result

# texte de test

tweet = 'Ce matin nous serons reçus par le Pdt du Senat @gerard_larcher pour exiger un statut, licenciements qualifiés économiques,'
print (analyse(tweet))

# test = 'la retraite de paul'
# apprentissage(test)
