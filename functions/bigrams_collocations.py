import nltk
from nltk.collocations import *
from prepare_lyrics import prepare_lyrics

def print_common_bigrams(lyrics_tuple):
    title, tokenlist = lyrics_tuple
    bigrams = nltk.ngrams(tokenlist, 2)
    bigram_freq = nltk.FreqDist(bigrams)
    most_freq_bigrams = bigram_freq.most_common(10)

    print(f"** Most frequent bigrams in '{title}' **")
    for pair in most_freq_bigrams:
        bigram_string = " ".join(pair[0])
        print(bigram_string)
    print()

def print_collocations(lyrics_tuple):
    title, tokenlist = lyrics_tuple
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_words(tokenlist, window_size=10)
    finder.apply_freq_filter(2)
    top_collocations = finder.nbest(bigram_measures.pmi, 10)

    print(f"** Common Collocations in '{title}' **")
    for bigram in top_collocations:
        collocation_string = " ".join(bigram)
        print(collocation_string)
    print()

# Assuming lyrics_data is a list of tuples (title, tokenlist) returned from prepare_lyrics
lyrics_data = prepare_lyrics("lyrics")
for lyrics_tuple in lyrics_data:
    print_common_bigrams(lyrics_tuple)
    print_collocations(lyrics_tuple)