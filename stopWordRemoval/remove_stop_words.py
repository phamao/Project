import nltk
from nltk.corpus import stopwords
import sys
import re

def remove_stop(fileName):
    # Open, read, and close the file
    with open(fileName, encoding="utf-8") as file:
        text = file.read()

    # Splitting the text into words
    words = text.split()

    # Creating the list of stop words
    stoplist = stopwords.words("english")
    stoplist.extend(['[', ']', '``', '""', "(", ")" '-'])

    # Removing stop words and then punctuation from the list of words
    stop_removed = [word for word in words if word.lower() not in stoplist]
    stop_removed = [re.sub(r"[,.\"\'?!;&()``:\-\\[\]]", "", word) for word in stop_removed]

    # Removing empty strings
    stop_removed = [word for word in stop_removed if word]

    print(stop_removed)

print(remove_stop(sys.argv[1]))


#def lemmatize(fileName)
