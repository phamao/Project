import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec
from wordcloud import WordCloud
import pathlib
import os
import sys
import re

# Necessary for import from sister directories
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'processing')))
from prepare_lyrics import prepare_lyrics # This warning is fine
from megalist import megalist # This warning is fine

def wordcloudgenerator(lyrics_list):

    file_path = os.path.abspath('.') + ('/')

    # Creates the visualizations directory, if it does not currently exist
    pathlib.Path(file_path + 'visualizations').mkdir(exist_ok=True)

    '''
    Vocalization Removal Attempt 3 (Incomplete):
    Attempts to remove vocalizations directly in the word_cloud.py, using both regex and update(). update() failed, and regex has also not been successful for the reasons described
    on lines 27-28 in prepare_lyrics.py

    # Manually removes vocalizations since adding them to stop words did not work
    # regex_vocals = ['yeah yeah', 'nah nah', 'oh oh', 'la la', 'uh uh', 'na na', 'hey hey', 'eh eh', 'ha ha', 'ah ah', 'ay ay']
    # for vocal in regex_vocals:
    #     lyrics_list.remove(vocal)
    '''

    alltext = " ".join(lyrics_list)

    # print('oh oh' in lyrics_list) # debug
    # print(re.search('oh\soh', alltext)) #debug
    # print('oh-oh' in lyrics_list) # debug
    # print(re.search('oh-oh', alltext)) #debug
    
    #????????????????????????
    # 'oh oh' isn't in lyrics_list but 'oh-oh' is, yet both forms show up in alltext? And then when you add 'oh-oh' to the stop words it still appears in alltext???
    # alltext drwas directly from lyrics_list; if those words aren't in it, how the hell are they showing up in alltext??
    #????????????????????????

    wordcloud = WordCloud(width=1600, height=800).generate(alltext)
    plt.figure(figsize=(20,10), facecolor='k')
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig('visualizations/wordcloud.jpg', facecolor='k', bbox_inches='tight')

    # Prints the words in the wordcloud to add to stop words (debug)
    # print(wordcloud.words_.keys()) #debug

    # for key in wordcloud.words_: #debug
    #     print(key == 'oh oh')
    #     print(lyrics_list.index(key))
    #     break

all_lyrics = megalist(prepare_lyrics('lyrics'))

# Lemmatizes all_lyrics
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token) for token in all_lyrics]

wordcloudgenerator(lemmas)

# Why is this here? We're not doing anything with it
model = Word2Vec(lemmas, vector_size=100, window=5, min_count=3, workers=4)

print("model built!")