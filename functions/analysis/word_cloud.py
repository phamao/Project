import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec
from wordcloud import WordCloud
import pathlib
import os
import sys

# Necessary for import from sister directories
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'processing')))
from prepare_lyrics import prepare_lyrics # This warning is fine
from megalist import megalist # This warning is fine

def wordcloudgenerator(lyrics_list):

    file_path = os.path.abspath('.') + ('/')

    # Creates the visualizations directory, if it does not currently exist
    pathlib.Path(file_path + 'visualizations').mkdir(exist_ok=True)

    alltext = " ".join(lyrics_list)

    wordcloud = WordCloud(width=1600, height=800).generate(alltext)
    plt.figure(figsize=(20,10), facecolor='k')
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig('visualizations/wordcloud.jpg', facecolor='k', bbox_inches='tight')

    # Prints the words in the wordcloud to add to stop words
    print(wordcloud.words_.keys()) #debug

all_lyrics = megalist(prepare_lyrics('lyrics'))

# Lemmatizes all_lyrics
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(token) for token in all_lyrics]

wordcloudgenerator(lemmas)

# Why is this here? We're not doing anything with it
model = Word2Vec(lemmas, vector_size=100, window=5, min_count=3, workers=4)

print("model built!")