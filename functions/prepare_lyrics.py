import os 
import nltk
import sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt



# Given a directory, prepares its contents and returns the list of tokens after removing stop words and lemmatizing.
def prepare_lyrics(directory):

    # Create a list for all the tokens to be held 
    alltokens = []

   # First for loop to tokenize text from all of the files
    for filename in os.listdir(directory):
        if '.txt' in filename:
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()
                tokens = nltk.word_tokenize(text)
                alltokens.append(tokens)


    # Creating stop words 
    # EXTEND MORE LATER, MAKE SURE TO REMOVE ALL STOP WORDS EVEN IN DIFFERENT LANGUAGES
    stop_words = stopwords.words('english')
    stop_words.extend(['[', ']', ':', ';', "''", '(', ')', '&', ',', '?', '``', '-', ',', '!', "'"])

    # Second for loop to remove the stop words from the tokenized text of all of the files 
    alltokens_nostopwords = []
    for tokenlist in alltokens:
        nostopwords = [token for token in tokenlist if token.lower() not in stop_words]
        alltokens_nostopwords.append(nostopwords)


    # Creating the lemmatizer
    lemmatizer = WordNetLemmatizer() 

    # Third for loop to lemmatize the words 
    lemmatized = []
    for tokenlist in alltokens_nostopwords:
        all_lemmas = [lemmatizer.lemmatize(token) for token in tokenlist]
        lemmatized.append(all_lemmas)

    return lemmatized


# Outputs the list of tokens of the inputted text file
prepare_lyrics("lyrics")