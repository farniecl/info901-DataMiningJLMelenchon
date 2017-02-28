'''
pos_tweets = [('j\'adore cette voiture', 'positive'),
              ('La vue est superbe', 'positive'),
              ('je me sens superbement bien', 'positive'),
              ('je suis excité à propos de ce concert', 'positive'),
              ('Il est mon meilleur ami', 'positive')]

neg_tweets = [('je hais cette voiture', 'negative'),
              ('cette vue est horrible', 'negative'),
              ('je me sens fatigué ce matin', 'negative'),
              ('Ce concert est détestable', 'negative'),
              ('Il est mon ennemi', 'negative')]

print pos_tweets
file = open('positive.txt','w') 
for line in pos_tweets:
     file.write(line[0])
     file.write('\n')
file.close() 
file = open('negative.txt','w') 
for line in neg_tweets:
     file.write(line[0])
     file.write('\n')
file.close() 
'''
