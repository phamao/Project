# Popular Songs and Their Lyrics

This is a Python script that takes a collection of Spotify's top songs, scrapes its lyrics, and tokenizes it.

## Installation

Download the data from Kaggle in the Sources section below. Extract the contents of `archive.zip` into this directory.

You will need to install the following libraries.

    pip install lyricsgenius
    pip install nltk
    pip install wordcloud
    pip install gensim
    pip install dotenv
    pip install sklearn
    pip install scikit-learn
    pip install plotly
    pip install networkx[default]

If you want to run the script for yourself, you will need to create a [Genius API Client](https://genius.com/api-clients). Create an account if necessary, then fill in the App Name and App Website URL. You can use [localhost:6000](http://localhost:6000/). You should now see an option to generate a Client Access Token. In this directory, create a file called `.env`, containing the following:

    CLIENT_TOKEN = 'YOUR CLIENT ACCESS TOKEN'

You should now be able to run the script.

## Usage

If you are going to collect a new set of data, it is highly recommended that you delete `known_songs.txt`, as the file is meant for subsequent runs to keep track of what songs have been searched already. You should also delete all files in the `lyrics/` directory.

## Authors

This project was a collaboration between [Andrew Pham](https://github.com/phamao), [Yao Yan Jiang](https://github.com/yaoyan01), and [Tommy Chen](https://github.com/chenafb).

## Sources

This project uses data collected and published on [Kaggle](https://www.kaggle.com/datasets/dhruvildave/spotify-charts). It also uses the [Genius API](https://docs.genius.com/) to acquire song lyrics.

## To Do

Regex to remove any \[...\] from songs that announces verses/intros/outros.
Remove embeds at the end of every set of lyrics.
Remove first lines from every set of lyrics, since it contains the song title and useless text.
Lemmatize only wordclouds.

## Files

This is an overview of the files and directories in this repository.

### `2017/`

`2017/` is a directory containing the lyrics of songs published in 2017.

### `2018/`

`2018/` is a directory containing the lyrics of songs published in 2018.

### `2019/`

`2019/` is a directory containing the lyrics of songs published in 2019.

### `2020/`

`2020/` is a directory containing the lyrics of songs published in 2020.

### `2021/`

`2021/` is a directory containing the lyrics of songs published in 2021.

### `archive.zip` and `charts.csv`

Although these files are not included in this repository, they are required. `archive.zip` can be downloaded [here](https://www.kaggle.com/datasets/dhruvildave/spotify-charts). Extract `charts.csv` from `archive.zip` and place it in this directory.

### `functions/`

`functions/` is a directory containing all functions used for this project.

#### `bigrams_collocations.py`

`bigrams_collocations.py` is a Python script that sorts the song/lyric list of tuples into bigrams and collocations.

#### `collect_data.py`

`collect_data.py` is a Python script that calls `save_lyrics.py` repeatedly to increase search capabilities.

#### `lyrics_by_year.py`

`lyrics_by_year.py` is a Python script that sorts the songs in `lyrics/` into their respective directories.

#### `megalist.py`

`megalist.py` is a Python script that combines all the tokenized lyrics lists into one list.

#### `megalistbigrams.py`

`megalistbigrams.py` is a Python script that combines all the tokenized lyrics lists into one list, then creates bigrams.

#### `megalistcollocation.py`

`megalist.py` is a Python script that combines all the tokenized lyrics lists into one list, then creates collocations.

#### `prepare_lyrics.py`

`prepare_lyrics.py` is a Python script that organizes the lyric text files in `lyrics/` into a list of tuples, where the first value is the song name and second value is the tokenized lyrics.

#### `save_lyrics.py`

`save_lyrics.py` is a Python script that, given `charts.csv`, searches every song title contained in the file using the Genius API. It then saves the lyrics to a text file named after the song in the `lyrics/` directory.

#### `similar_lyrics.py`

`similar_lyrics.py` is a Python script that creates a vectorized visualization of word similarities in all the songs in the `lyrics/` directory.

#### `song_years.py`

`song_years.py` is a Python script that sorts all the songs in `charts.csv` by year. You will need to run the script yourself if you want to generate the text file.

#### `top20_freq.py`

`top20_most_freq.py` is a Python script that creates a bar graph showing the frequencies of the top 20 words in all the songs in the `lyrics/` directory. Has parameters for minimum word length or sorted by year.

#### `word_cloud.py`

`word_cloud.py` is a Python script that creates a wordcloud given a list of tokens.

### `lyrics/`

`lyrics/` is a directory containing text files for the lyrics of individual songs.

### `visualizations/`

`visualizations/` is a directory containing various data visualizations.

### `known_songs.txt`

`known_songs.txt` is a text file that stores the names of all songs that have been searched already; this is done to work around the request limitations of Genius's API.

### `songs_by_year.txt`

`songs_by_year.txt` is a text file contains each song in `charts.csv` by year. It is NOT contained in this repository due to its size and must be generated using `song_years.py`.