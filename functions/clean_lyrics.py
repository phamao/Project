import re
import os

# Given a lyric text file, removes the following for formatting:
# The first line (contains useless text like contributors, languages, etc.)
# Any text in [...] (announces verses, intros, outros, etc.)
# "XEmbed", where X is any number (attached to the end of every lyric file)

def clean_lyrics(filename):

    # Opens the file to extract lyrics
    with open(filename, 'r', encoding='utf-8') as file:

        # Stores the lyrics
        lyrics = []

        # Saves lyrics to a list with each line as an element
        for line in file:
            
            lyrics.append(line)

    # print(lyrics) #debug

    # Some files are empty (BehindTheLyrics, Videographie)
    try:

        # Removes the first line
        lyrics.remove(lyrics[0])

    except:
        print('Failed to clean the first line in {filename}'.format(filename=filename))

    # This should work no matter what file is inputted since it doesn't index, but this is here just in case
    try:

        # For every line in the lyrics list, remove any text in [...] and any text in format "XEmbed"
        for line in lyrics:

            # Removes any text in [...]
            if re.search('^\[.*\]\n', line): # Returns None if no match
                lyrics.remove(line)
    
    except:
        print('Failed to clean [...] in {filename}'.format(filename=filename))

    # Some files don't work for this (ChuckNorris(RadioEdit).txt)
    try:
        # Removes XEmbed at the end of each file
        for i in range(len(lyrics[-1])-1, -1, -1):

            # print(lyrics[-1][i]) #debug
            # print(lyrics[-1][i-1]) #debug

            current_char = lyrics[-1][i]
            left_char = lyrics[-1][i-1]

            # If the current character is numeric and the character to the left is not, removes from the numeric character to the end
            # lyric lyric lyric66Embed, looks for the spot between 'c' and the first '6'
            if current_char.isnumeric() and not left_char.isnumeric():
                lyrics[-1] = lyrics[-1][0:i]

    except:
        print('Failed to clean [...] in {filename}'.format(filename=filename))

    # print(lyrics) #debug

    # Opens the file to write cleaned lyrics
    with open(filename, 'w', encoding='utf-8') as file:

        # For each lyric line, write it to the file
        for line in lyrics:
            file.write(line)

# For each file in the lyrics/ directory...
for filename in os.listdir('lyrics/'):

    # print(filename) #debug

    # Creates the filepath
    filepath = os.path.join('lyrics/', filename)
    
    # Runs clean_lyrics
    print('\n*****\nCleaning {filename}...'.format(filename=filename))
    clean_lyrics(filepath)
    print('Successfully cleaned {filename}!\n*****\n'.format(filename=filename))