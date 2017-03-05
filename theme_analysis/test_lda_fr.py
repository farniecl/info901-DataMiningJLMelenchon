from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('fr')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

# create sample documents
doc_travail="retraite 35 heures emplois salaire salaires chomage Le compte pénibilité est une escroquerie Notre programme prévoit la retraite à 60 ans à taux plein avec 40 annuités Les femmes ont les tâches les moins payées et les plus morcelées plusieurs syndicats appellent à la grève contre les inégalités entre hommes et femmes Pour faire de la relocalisation, il faut des circuits courts, notamment dans le domaine agricole et alimentaire Le cluster maritime dit qu'on peut doubler les emplois en mer Toute notre méthode pousse à la relocalisation. Dans  agriculture avec le bio et les circuits courts. On n'a pas à choisir entre l'esclavage et le chômage"
doc_europe="La Commission européenne juncker Juncker euro Euro europe Europe À bas le CETA, je ne signerai pas ! Si on laisse faire TAFTA et CETA, c'est la fin des normes de notre pays Le seul horizon de l'Europe, c'est l'euro et la Défense.La monnaie et la guerre, tu parles d'un horizon On ne peut pas mettre en place la politique que je propose dans le cadre des traités européens actuels Après 2005, les représentants politiques ont fait comme si on avait voté oui. Alors qu'on avait voté non Les partis sociaux-démocrates d'Europe ont désormais intégré les règles du capitalisme.Moi, je crois au travail. Nous avons besoin de gens hautement qualifiés. J'ai voté pour Maastricht. Mais j'ai voté contre la #BCE, contre l'#euro, et contre le #TCE de 2005.essayé de renégocier les traités.À l'issue des négociations que je mènerai au niveau européen, je soumettrai le texte de l'accord à référendum.qui peut passer sur le vieux continent PAC"



# compile sample documents into a list
doc_set = [doc_europe,doc_travail]

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:

    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=50)

print(ldamodel.print_topics(num_topics=2, num_words=4))
