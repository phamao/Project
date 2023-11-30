import os 
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

# Prepares all lyrics in lyrics/ directory, separating it into tuples
def prepare_lyrics(directory):
    all_lyrics = []

    # Load stop words
    stop_words = set(stopwords.words('english'))
    stop_words.update(['[', ']', ':', ';', "''", '(', ')', '&', ',', '?', '``', '-', ',', '!', '\'', '.', '/'])
    
    # Song specific stop words
    stop_words.update(['feat', 'chorus', 'verse', 'pre-chorus', 'post-chorus'])

    # Lemmatizer
    lemmatizer = WordNetLemmatizer() 

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            title = os.path.splitext(filename)[0]  # Remove the file extension to get the title
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()

                text = re.sub('\'', '', text)
                text = re.sub('\d', '', text)

                tokens = nltk.word_tokenize(text)

                # Remove stop words
                tokens = [token for token in tokens if token.lower() not in stop_words and 'Contributors' not in token]

                # Lemmatize
                lemmas = [lemmatizer.lemmatize(token) for token in tokens]

                all_lyrics.append((title, lemmas))

    return all_lyrics