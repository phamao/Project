from prepare_lyrics import prepare_lyrics
from word_cloud_generator import wordcloudgenerator
import numpy as np
import matplotlib.pyplot as plt
import gensim
import re
import nltk
from gensim.models import Word2Vec
from sklearn.decomposition import PCA

lemmatized_words = prepare_lyrics('lyrics')
#wordcloudgenerator(lemmatized_words)

model = Word2Vec(lemmatized_words, vector_size=100, window=5, min_count=3, workers=4)
print("model built!")

#print(model.wv.most_similar('que'))


#have to get this word2vec thing working, will do tmr


## REPLACE THE WORD PAIRS BELOW WITH YOUR OWN WORD PAIRS

wordpairs = {"Que":"el"}

# Go get the word vectors for these words and
# then store them so you can use them later on.
vecwords = []  # stores the words above
vecs = []      # stores the vectors for each word
for k,v in wordpairs.items():
    kvec = model.wv[k]
    vvec = model.wv[v]
    vecs.append(kvec)
    vecwords.append(k)
    vecs.append(vvec)
    vecwords.append(v)

# PCA is a way to project multiple dimensions down to
# fewer dimensions, which we are doing here so we can
# visualize the word vectors.
pca = PCA(n_components=2, whiten=True)
vectors2d = pca.fit(vecs).transform(vecs)


# This is just some ugly matplotlib code for plotting
# the 2-D vectors and visualizing them with different colors.
i = 2
for point, word in zip(vectors2d, vecwords):
    if i%2 == 0:
        plt.scatter(point[0], point[1], c='r')
    else:
        plt.scatter(point[0], point[1], c='b')
    i += 1

    plt.annotate(
            word,
            xy=(point[0], point[1]),
            xytext=(7, 6),
            textcoords='offset points',
            ha='left' ,
            va='top',
            size="medium"
            )