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
                       'go', 'na', 'one', 'yeah', 'um', 'u', 'oh-oh'])
    
    # Adding 'oh-oh' moved 'oh oh' down one spot in the word cloud; I think the lemmatizer is condensing all the different variations of 'oh oh' (hyphens, multiple 'o's and 'h's)
    # into 'oh oh' with a space, explaining why it doesn't show up in the lryics_list of word_cloud.py but appears anyways? This is confusing me so much
    
    '''
    Vocalization Removal Attempt 1:
    Basic implementation using .update(). Failed to remove any vocalizations.
    
    # Vocalizations: This was the first iteration of trying to remove vocalizations.
    # stop_words.update(['yeah', 'yeah yeah', 'nah nah', 'oh oh', 'la la', 'uh uh', 'na na', 'hey hey', 'eh eh',
    #                    'ha ha', 'ah ah', 'um', 'ay ay']) # Most of these don't work? Copying output straight from print(wordcloud.words_.keys()) but still doesn't catch a lot
    '''

    '''
    Vocalization Removal Attempt 2 (1st Section):
    Attempted to use Regex more to ensure words actually matched. Failed.

    # Vocalizations
    # # Stores the regex for the vocalizations
    # regex_vocals = ['yeahyeah', 'nahnah', 'ohoh', 'lala', 'uhuh', 'nana', 'heyhey', 'eheh', 'haha', 'ahah', 'ayay']
    # stop_words.update(regex_vocals)
    '''

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            title = os.path.splitext(filename)[0]  # Remove the file extension to get the title
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()

                text = re.sub('\'', '', text)
                text = re.sub('\d', '', text)

                # print(text) # debug

                tokens = nltk.word_tokenize(text)

                '''
                Vocalization Removal Attempt 2 (2nd Section):
                
                # # Stores vocals to be removed after searching this file to prevent unecessary searches
                # to_remove = []

                # # For each file (parent loop), check if re.search(vocal, text) finds a match. If it finds a match, adds it to the stop words and to_remove
                # # For each vocalization in regex_vocals, check if it finds a match in text
                # for vocalization in regex_vocals:

                #     # Stores the regex search
                #     vocal_search = re.search(vocalization, text)

                #     # If the vocal matches, update the stop words and add it to to_remove
                #     if vocal_search:
                #         stop_words.update(vocal_search.group())
                #         to_remove.append(vocalization)

                # # Removes each vocalization from regex_values
                # for vocalization in to_remove:
                #     regex_vocals.remove(vocalization)
                '''
                
                # Remove stop words
                tokens = [token for token in tokens if re.sub(' ', '', token.lower()) not in stop_words and 'Contributors' not in token]

                all_lyrics.append((title, tokens))

    return all_lyrics