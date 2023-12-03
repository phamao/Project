import os
import pathlib
import re
import shutil

# Loops through all songs in known_songs.txt, using songs_by_year.txt.
# Then copies the lyrics files of each song in known_songs.txt to a directory respective of its year.
def lyrics_by_year(year):

    # years go 2017, 2018, 2020, 2019, 2021

    # Create the year's directory if it doesn't exist
    pathlib.Path(os.path.abspath('.') + '/' + str(year) + '/').mkdir(exist_ok=True)

    # Open songs_by_year.txt in read mode
    file = open('songs_by_year.txt', 'r', encoding='utf-8')

    # Goes through each line and checks if its key = year
    for line in file:

        line_year = line[0:4]

        # If line_year == year, converts that line into a list
        if line_year == str(year):

            # Stores all the songs in that year and makes it into a list
            songs = line[6:-2]
            song_list = songs.split(', ')
            break

    file.close()

    # Strips quotes from songs
    stripped_list = [s.strip('\'') for s in song_list]

    file = open('known_songs.txt', 'r', encoding='utf-8')

    # Goes through each line in known_songs.txt and checks if that song is in song_list
    for line in file:

        # Removes the \n at the end of the line
        song = line[0:-1]

        # If the song is in the year's stripped_list, format its name and copy its lyrics in lyrics/
        if song in stripped_list:
                # print('FOUND')
                
            # Stores the filename
                name = song + '.txt'

                # Removes incompatible characters
                name = re.sub(' ', '', name)
                name = re.sub('/', '', name)

                # Creates filepaths
                source = './lyrics/{name}'.format(name=name)
                destination = './{year}/{name}'.format(year=year, name=name) 

                try:
                    # Copies the file from lyrics/ to the year directory
                    shutil.copyfile(source, destination)

                except:
                    continue

    file.close()

lyrics_by_year(2017)
lyrics_by_year(2018)
lyrics_by_year(2019)
lyrics_by_year(2020)
lyrics_by_year(2021)

# Note: some songs are listed multiple times, so they may appear in multiple year lists