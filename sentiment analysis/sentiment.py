# -*- coding: utf-8 -*-
import os
import nltk

pos_tweets = []
neg_tweets = []

f = open('positive.txt','r')
for line in f:
    pos_tweets.append((line,'positive'))
f.close()

f2 = open('negative.txt','r')
for line in f2:
    neg_tweets.append((line,'negative'))
f2.close()

tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
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
        append_pos = open('positive.txt','a')
        append_neg = open('negative.txt','a')
        if result=='positive':
            append_pos.write(string_a_tester)
            append_neg.write('\n')
        else:
            append_neg.write(string_a_tester)
            append_neg.write('\n')
        append_pos.close()
        append_neg.close()
        return result

def apprentissage(string_a_tester):
        result = classifier.classify(extract_features(string_a_tester.split()))
        append_pos = open('positive.txt','a')
        append_neg = open('negative.txt','a')
        print (string_a_tester + " semble " + result)
        verif = raw_input("Comment est le texte? P(positif)/N(négatif)/I(inclassable)")
        if str(verif)=="p":
            print ("texte positif")
            append_pos.write(string_a_tester)
            append_neg.write('\n')
        elif str(verif)=="n":
            print ("texte negatif")
            append_neg.write(string_a_tester)
            append_neg.write('\n')
        else:
            print ("texte passé")
        append_pos.close()
        append_neg.close()
        return result
    
# texte de test

tweet = 'Larry est un enfoiré détestable'
print (analyse(tweet))

test = 'Il est fabuleux'
apprentissage(test)
