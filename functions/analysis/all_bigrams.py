import nltk
from nltk.collocations import *
import os
import sys

# Necessary for import from sister directories
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'processing')))
from prepare_lyrics import prepare_lyrics # This warning is fine
from megalist import megalist # This warning is fine

def print_common_bigrams(tokenlist):
    pentgrams = nltk.ngrams(tokenlist, 2)
    pentgrams_freq = nltk.FreqDist(pentgrams)
    most_freq_bigrams = pentgrams_freq.most_common(30)

    for pair in most_freq_bigrams:
        bigram_string = " ".join(pair[0])
        print(bigram_string)
    print()


# Assuming lyrics_data is a list of tuples (title, tokenlist) returned from prepare_lyrics
lyrics_data = megalist(prepare_lyrics("lyrics"))
print_common_bigrams(lyrics_data)