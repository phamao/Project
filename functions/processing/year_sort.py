import os
import pathlib
import re
import shutil
import csv

#######################################################
# FYI: This script takes a couple minutes to fully run.
#######################################################

# Sorts all the songs in charts.csv into songs_by_year.txt
# You will need to run this yourself to generate the text file.
def song_years():
    print('\nGenerating sorted dictionary...')

    # Stores the songs per year {year:name}
    songs_per_year = {}

    # Opens charts.csv
    charts = open('data/charts.csv', encoding='utf-8')

    # Initializes the csv reader
    csvreader = csv.reader(charts, delimiter=',')

    # For each row in charts...
    for row in csvreader:
        
        # If the year is not tracked yet, initializes it
        if row[2][0:4] not in songs_per_year:
            songs_per_year[row[2][0:4]] = [row[0]]

        # If the year has been tracked, appends the song
        elif row[2][0:4] in songs_per_year:
            songs_per_year[row[2][0:4]].append(row[0]) 

    charts.close()
    print('Successfully generated sorted dictionary!\n')

    # Returns the dictionary
    return songs_per_year

# Loops through all songs in known_songs.txt, using songs_by_year.txt.
# Then copies the lyrics files of each song in known_songs.txt to a directory respective of its year.
def lyrics_by_year(year, dictionary):
    print('\nBeginning sort...')

    # years go 2017, 2018, 2020, 2019, 2021

    # Create the year's directory if it doesn't exist
    pathlib.Path(os.path.abspath('.') + '/' + str(year) + '/').mkdir(exist_ok=True)

    # Strips quotes from songs
    stripped_list = [songname.strip('\'') for songname in dictionary[str(year)]]

    file = open('known_songs.txt', 'r', encoding='utf-8')

    # Goes through each line in known_songs.txt and checks if that song is in stripped_list
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
    print('Successfully sorted!\n')

# Generates the year dictionary necessary for lyrics_by_year
year_dict = song_years()

# Calls lyrics_by_year for each year
for i in range(2017, 2022):
    lyrics_by_year(i, year_dict)

# Note: some songs are listed multiple times, so they may appear in multiple year lists