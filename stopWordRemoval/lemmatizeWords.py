import sys
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# create a new list of tokens, alllemmas by lemmatizing allcontenttokens                                        
def lemmatizeWords(fileName):
    
    with open(fileName, encoding="utf-8") as file:
        text = file.read()
        
    for words in text:
        lemmatized = [lemmatizer.lemmatize(word) for word in words]

    print(lemmatized)

lemmatizeWords("tokenswithoutStopWords.txt")