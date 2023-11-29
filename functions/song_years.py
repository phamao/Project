import csv

# Sorts all the songs in known_songs.txt into songs_by_year.txt
# You will need to run this yourself to generate the text file.
def song_years():

    # Stores the songs per year
    songs_per_year = {}

    # Opens charts.csv
    charts = open('charts.csv', encoding='utf-8')

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

    # Prints the dictionary to songs_by_year.txt
    with open('songs_by_year.txt', 'w', encoding='utf-8') as f:
        for key, value in songs_per_year.items():
            f.write('%s:%s\n' % (key, value))

    charts.close()
    f.close()

    print('\nProcess Completed\n')

song_years()