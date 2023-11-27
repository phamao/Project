import csv
from lyricsgenius import Genius
from dotenv import load_dotenv
import os
import pathlib
import re
import time

load_dotenv()

client_token = os.getenv("CLIENT_TOKEN")

# Creates the lyrics directory, if it does not currently exist
pathlib.Path('./lyrics/').mkdir(exist_ok=True)

# Given a csv file, takes each song title and saves its lyrics as a text file, named the title.
def save_lyrics(filename):

    # Opens the csv file 
    f = open(filename, encoding='utf8')

    # Opens the text file containing all songs gone through so far
    known = open('known_songs.txt', 'a+', encoding='utf-8')

    # Moves file pointer to beginning for reading
    known.seek(0, 0)

    # Stores all raw song titles
    raw_songs = known.readlines()

    # Stores formatted song titles
    known_songs = []

    # Strips \n from songs
    for song in raw_songs:
        known_songs.append(song.strip())

    known.seek(0, 2)

    # Initializes the csv reader
    csvreader = csv.reader(f, delimiter=',')

    # Initializes the Genius search
    genius = Genius(client_token)

    for row in csvreader:

        # If the song is not known... (This is a workaround for being limited by API request timeouts. All songs searched are stored in known_songs.txt, which is used to check is a song needs to be searched.)
        if row[0] not in known_songs:
            
            # Adds the title to the known_songs.txt
            known.write(row[0] + '\n')

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
    known.close()

save_lyrics('charts.csv')