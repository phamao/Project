from prepare_lyrics import prepare_lyrics
from megalist import megalist
import numpy as np
import matplotlib.pyplot as plt
import gensim
import re
import nltk
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from wordcloud import WordCloud
import os
import pathlib

def wordcloudgenerator(list):

    file_path = os.path.abspath('.') + ('/')

    # Creates the visualizations directory, if it does not currently exist
    pathlib.Path(file_path + 'visualizations').mkdir(exist_ok=True)

    alltext = " ".join(list)

    wordcloud = WordCloud(max_font_size=40).generate(alltext)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig('visualizations/wordcloud.jpg')

lemmatized_words = megalist(prepare_lyrics('lyrics'))

wordcloudgenerator(lemmatized_words)

model = Word2Vec(lemmatized_words, vector_size=100, window=5, min_count=3, workers=4)
print("model built!")