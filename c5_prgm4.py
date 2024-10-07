from nltk import ngrams
setence ='I reside in India'
n=3
trigrams=ngrams(setence.split(),n)
for grams in trigrams:
    print(grams)