import nltk
import sys

# Given a text file, tokenizes its contents and returns the list of tokens.
def tokenize_lyrics(filename):

    # Opens the file for reading
    f = open(filename, encoding='utf-8')

    # Reads the file and stores the text
    text = f.read()
    f.close()

    # Tokenizes the text
    tokens = nltk.word_tokenize(text)

    return tokens

# Outputs the list of tokens of the inputted text file
print(tokenize_lyrics(sys.argv[1]))