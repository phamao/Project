import csv
from lyricsgenius import Genius
from dotenv import load_dotenv
import os
import pathlib
import re

load_dotenv()

client_token = os.getenv("CLIENT_TOKEN")

# Creates the lyrics directory, if it does not currently exist
pathlib.Path('./lyrics/').mkdir(exist_ok=True)

# Given a csv file, takes each song title and saves its lyrics as a text file, named the title.
def save_lyrics(filename):

    # Stores the song names and their lyrics
    songs_and_lyrics = {}

    # Opens the csv file and intializes each song name as a key in songs_and_lyrics 
    f = open(filename, encoding='utf8')

    csvreader = csv.reader(f, delimiter=',')

    # Initializes the Genius search
    genius = Genius(client_token)

    for row in csvreader:

        # Gets the song info based on the title
        song = genius.search_song(title=row[0])

        # If the search is successful...
        if song:

            # Stores the name of the song
            title = song.title

            # Stores the lyrics of the song
            lyrics = song.lyrics

            # Stores the filename
            name = title + '.txt'

            # Removes incompatible characters
            name = re.sub(' ', '', name)
            name = re.sub('/', '', name)

            # Creates the save path
            save_path = './lyrics/'
            final_path = os.path.join(save_path, name)

            # Creates the file and writes the lyrics to it
            file = open(final_path, 'w', encoding='utf8')
            file.write(lyrics)

            file.close()

    f.close()

save_lyrics('charts.csv')