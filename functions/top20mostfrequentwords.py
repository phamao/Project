import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from collections import Counter
from prepare_lyrics import prepare_lyrics


# Your existing prepare_lyrics function call
all_lyrics = prepare_lyrics("lyrics/")  # Replace with your directory

# Aggregate word frequencies
word_counts = Counter()
for _, lemmas in all_lyrics:
    word_counts.update(lemmas)

# Select top N most common words for the histogram
top_n = 20
most_common_words = word_counts.most_common(top_n)
words, counts = zip(*most_common_words)

# Plotting the histogram
plt.figure(figsize=(10, 6))
plt.bar(words, counts)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 20 Most Frequent Words in Popular Songs')
plt.xticks(rotation=45)
plt.show()
