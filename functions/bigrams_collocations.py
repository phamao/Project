import nltk
from prepare_lyrics import prepare_lyrics 


def print_common_bigrams(tokenlist):
    
    # get bigrams|
    bigrams = nltk.ngrams(tokenlist, 2)
    bigramlist = list(bigrams)

    # print out most frequent bigrams
    print("** Most frequent bigrams **")
    bigramfreq = nltk.FreqDist(bigramlist)
    mostFreqTen = bigramfreq.most_common(10)
    for pair in mostFreqTen:
        string = pair[0][0] + " " + pair[0][1]
        print(string)

    print()


# import statement
from nltk.collocations import *

# Create the object you need to get collocations.
bigram_measures = nltk.collocations.BigramAssocMeasures()

# Write a function that prints out the top 10 collocations in
# a list of tokens using PMI for the ranking metric and 
# a frequency filter of 2.
# Argument: a list of tokens


def print_collocations(tokenlist):
    finder = BigramCollocationFinder.from_words(tokenlist, window_size=10)
    finder.apply_freq_filter(2)

    print("** Common Collocations **")
    tupleList = finder.nbest(bigram_measures.pmi, 10)
    for tuple in tupleList:
        print(tuple[0]+ " " + tuple[1])

    print()


lemmatized = prepare_lyrics('lyrics')
for tokenlist in lemmatized:
    print_collocations(tokenlist)

