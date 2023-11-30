import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from collections import Counter
from prepare_lyrics import prepare_lyrics

# Given an integer num_letters, creates a bar graph with the top 20 words in all of lyrics/ with at least num_letters letters.
# If num_letters is 0, does not discriminate by word length
def top20_words_frequency(num_letters):
        
    all_lyrics = prepare_lyrics("lyrics/") # list of tuples, whose values are song name and list of tokens (list in tuple in list)

    sorted_lyrics = []

    # Checks the word length limit for the graph
    if num_letters != 0:   

        # For each tuple (song) in the list (all_lyrics)...
        for song in all_lyrics:

            # Stores words that are long enough
            checked_words = []

            # Checks every token in tuple[1] (song lyrics) against num_letters
            for token in song[1]:

                # If the word length is greater than or equal to num_letters, add it to checked_words
                if len(token) >= num_letters:
                    checked_words.append(token)

            # After all tokens have been checked, adds the song and its passing lyrics to sorted_lyrics as a tuple
            sorted_lyrics.append((song[0], checked_words))
    
    elif num_letters == 0:
        sorted_lyrics = all_lyrics

    # Aggregate word frequencies
    word_counts = Counter()
    for _, lemmas in sorted_lyrics:
        word_counts.update(lemmas)

    # Select top N most common words for the histogram
    top_n = 21
    most_common_words = word_counts.most_common(top_n)

    # # Display all words
    # if num_letters == 0:

    #     # Removes the unknown line character, TEST WITH AND WITHOUT THIS LINE
    #     del most_common_words[0]    

    words, counts = zip(*most_common_words)

    # Plotting the histogram
    plt.figure(figsize=(10, 10))
    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 20 Most Frequent Words in Popular Songs')
    plt.xticks(rotation=45)
    # plt.show()

    if num_letters == 0:
        plt.savefig('visualizations/top20freq_all.jpg')
    else:
        plt.savefig('visualizations/top20freq_' + str(num_letters) +'.jpg')


for i in range(15):
    top20_words_frequency(i)
    print('Completed i = %i' % (i))

print('\nDone!\n')