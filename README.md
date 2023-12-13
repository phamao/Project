# Popular Songs and Their Lyrics

This is a Python script that takes a collection of Spotify's top songs, collects their lyrics, and tokenizes it.

**This README was last updated on 12/13/2023**.


## Installation & Usage

You will need to install the following libraries:

    pip install lyricsgenius
    pip install nltk
    pip install wordcloud
    pip install gensim
    pip install dotenv
    pip install sklearn
    pip install scikit-learn
    pip install plotly
    pip install networkx[default]


### Data Acquisiton & Enabling Genius Search

The source data is **NOT INCLUDED** in this directory due to its size. To download the data (991 MB zip, 3.26 GB file) from Kaggle, use the link in the Sources section below, or download it from [this link](https://www.kaggle.com/datasets/dhruvildave/spotify-charts). They are the same link. Extract the contents of `archive.zip` into the `data/` directory.

Create a [Genius API Client](https://genius.com/api-clients). Create an account if necessary, then fill in the App Name and App Website URL. You can use [localhost:6000](http://localhost:6000/) or another domain. You should now see an option to generate a Client Access Token. Click it to generate a token and copy it.

In the `data/` directory, create a file called `.env`. Within this file, create a variable called `CLIENT_TOKEN`. Paste the token you got as its value.

Contents of `.env`:

    CLIENT_TOKEN = 'YOUR CLIENT ACCESS TOKEN'


### Data Collection

This repository has already collected a large amount of data, as seen in the `lyrics/` directory.

To collect more data, run `functions/collect_data.py` as many times as desired. This will save the song lyrics to `lyrics/`.

If you wish to begin collecting data from the first song, it is recommended to delete the following files:

- `known_songs.txt`: This text file tracks all the songs that have already been searched so that they will not be searched on subsequent runs. If it is not deleted, the search will begin midway through `charts.csv`, which may or may not cause issues depending on your purposes.

- `lyrics/*`: Deleting all the files in the `lyrics/` directory will ensure that future searches are actually saving each song. If you do not, each file will be overwritten, and it will be harder to confirm if songs are being saved.

- `20XX/*`: The year directories contain the songs in `known_songs.txt`; therefore, if `known_songs.txt` has been deleted and you wish to run `songs_by_year.py`, these directores should be empty.

You can now begin collecting data from scratch with `functions/collect_data.py`.


### Data Processing

Run `clean_lyrics.py` once all desired lyrics have been collected or more lyrics have been added. **This should be run before `songs_by_year.py` as it copies directly from `lyrics/`. Any analysis should be done after as well for the same reason.**

Since `sorted_years.txt` is too large to include in the repository, **you must run `year_sort.py` before running `songs_by_year.py`.** This is because `songs_by_year.py` directly draws from `sorted_years.txt`.

`megalist.py` and `prepare_lyrics.py` both only contain helper functions and are only called by other files in the `functions/analysis/` directory, so these do not need to be individually run. Nothing will happen if you do.


### Data Analysis

These files can be run in any order, as they all perform separate, independent analyses.

`all_bigrams.py`, `all_collocations.py`, and `bigrams_collocations.py` all output directly to the terminal.

`cosine_similarity.py` redirects you to a page on your web browser.

`top20_freq.py` and `word_cloud.py` both save images to the `visualizations/` directory.


## Authors

This project was a collaboration between [Andrew Pham](https://github.com/phamao), [Yao Yan Jiang](https://github.com/yaoyan01), and [Tommy Chen](https://github.com/chenafb).


## Sources

This project uses data collected and published on [Kaggle](https://www.kaggle.com/datasets/dhruvildave/spotify-charts). It also uses the [Genius API](https://docs.genius.com/) to acquire song lyrics.


## To Do

- **Solved 12/12/2023:** ~~Regex to remove any \[...\] from songs that announces verses/intros/outros~~ 

- **Solved 12/12/2023:** ~~Remove embeds at the end of every set of lyrics~~

- **Solved 12/12/2023:** ~~Remove first lines from every set of lyrics, since it contains the song title and useless text~~

- **Solved 12/12/2023:** ~~`clean_lyrics.py` documentation~~

- **Solved 12/12/2023:** ~~Lemmatize only wordclouds~~

- **Solved 12/13/2023:** ~~Refactor any Python files that directly access `charts.csv` to path to `data/charts.csv` (should just be `collect_data.py` and `year_sort.py`), change any README instances where it says 'export to main directory' to 'export to the `data/` directory, update README~~

- **ADDED 12/12/2023:** Fix some stop words not being detected (vocalizations)

- **ADDED 12/13/2023:** Merge `songs_by_year.py` and `year_sort.py` into 1 file, update documentation as needed


## File Hierarchy

This is an overview of the files and directories in this repository.

### `2017/`

Directory containing the lyrics of songs published in 2017.

### `2018/`

Directory containing the lyrics of songs published in 2018.

### `2019/`

Directory containing the lyrics of songs published in 2019.

### `2020/`

Directory containing the lyrics of songs published in 2020.

### `2021/`

Directory containing the lyrics of songs published in 2021.


### `data/`

Directory containing all necessary data.

#### `archive.zip` and `charts.csv`

Data source from Kaggle. Although these files are not included in this repository, they are **REQUIRED**. `archive.zip` can be downloaded from the links provided in the Data Acquisiton & Enabling Genius Search and Sources sections. Extract `charts.csv` from `archive.zip` and place it in the `data/` directory.


### `functions/analysis`

Directory that contains all the code involved with the analysis of data.

#### `all_bigrams.py`

Python script that combines all the tokenized lyrics lists into one list, then creates bigrams.

#### `all_collocations.py`

Python script that combines all the tokenized lyrics lists into one list, then creates collocations.

#### `bigrams_collocations.py`

Python script that sorts the song/lyric list of tuples into bigrams and collocations.

#### `cosine_similarity.py`

Python script that visualizes the cosine similarities in all the songs in the `lyrics/` directory.

#### `top20_freq.py`

Python script that creates a bar graph showing the frequencies of the top 20 words in all the songs in the `lyrics/` directory. Has parameters for minimum word length or sorted by year.

#### `word_cloud.py`

Python script that lemmatizes the lyrics and creates a wordcloud.


### `functions/collection`

Directory that contains all the code involved with the collection of data.

#### `collect_data.py`

Python script that calls `save_lyrics.py` repeatedly to increase search capabilities. (Could be completely unecessary, based on the algorithm of me feeling like it searched more in a separate file)

#### `save_lyrics.py`

Python script that, given `charts.csv`, searches every song title contained in the file using the Genius API. It then saves the lyrics to a text file named after the song in the `lyrics/` directory.


### `functions/processing`

Directory that contains all the code involved with the processing of data.

#### `clean_lyrics.py`

Python script that cleans all the text files in the `lyrics/` directory of unecessary text.

#### `megalist.py`

Python script that combines all the tokenized lyrics lists into one list.

#### `prepare_lyrics.py`

Python script that tokenizes and removes stop words from the lyric text files, then organizes them into a list of tuples, where the first value is the song name and second value is the tokenized lyrics.

#### `songs_by_year.py`

Python script that copies the songs from `lyrics/` to their respective year directory using `sorted_years.txt`.

#### `year_sort.py`

Python script that sorts all the songs in `charts.csv` by year, then saves them to `sorted_years.txt`. You will need to run the script yourself if you want to generate the text file.


### `lyrics/`

Directory containing text files for the lyrics of individual songs.

### `visualizations/`

Directory containing various data visualizations.

### `known_songs.txt`

Text file that stores the names of all songs that have been searched already; this is done to work around the request limitations of Genius's API.

### `sorted_years.txt`

Text file contains each song in `charts.csv` by year. It is **NOT** contained in this repository due to its size and must be generated using `song_years.py`.
