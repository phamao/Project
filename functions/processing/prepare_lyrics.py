import os 
import nltk
from nltk.corpus import stopwords
import re

# Prepares all lyrics in lyrics/ directory, separating it into tuples
def prepare_lyrics(directory):
    all_lyrics = []

    # Load stop words
    stop_words = set(stopwords.words('english'))
    spanish_stop_words = set(stopwords.words('spanish'))
    stop_words.update(spanish_stop_words)
    stop_words.update(['[', ']', ':', ';', "''", '(', ')', '&', ',', '?', '``', '-',
                       ',', '!', '\'', '.', '/', '\'', '"', '...', '*', '--', '—', 
                       '’', '“', '”','–', '//'])
    
    # Song specific stop words
    stop_words.update(['feat', 'chorus', 'verse', 'pre-chorus', 'post-chorus', 'outro', 'verso', 'refrain',
                       'lyrics', 'intro', 'ft', 'et', 'embed', 'remix', 'archivo', 'ft.', 'ep', 'instrumental',
                       'khalil', 'liveget', 'petrusich_donotsell_tx_ptr.indd', 'ticket', ])

    # Extremely common words that appear every time
    stop_words.update(['like', 'im', 'know', 'might', 'dont', 'got', 'also', 'oh', 'aint', 'youre', 'get',
                       'go', 'na', 'one'])
    
    # Vocalizations
    stop_words.update(['yeah', 'yeah yeah', 'nah nah', 'oh oh', 'la la', 'uh uh', 'na na', 'hey hey', 'eh eh',
                       'ha ha', 'ah ah', 'um', 'ay ay']) # Most of these don't work? Copying output straight from print(wordcloud.words_.keys()) but still doesn't catch a lot

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

                all_lyrics.append((title, tokens))

    return all_lyrics