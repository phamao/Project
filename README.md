# Popular Songs and Their Lyrics

This is a Python script that takes a collection of Spotify's top songs, scrapes its lyrics, and tokenizes it.

## Installation

Download the data from Kaggle in the Sources section below. Extract the contents of archive.zip into this directory.

You will need to install the following libraries.

    pip install lyricsgenius
    pip install nltk

If you want to run the script for yourself, you will need to create a [Genius API Client](https://genius.com/api-clients). Create an account if necessary, then fill in the App Name and App Website URL. You can use [localhost:6000](http://localhost:6000/). You should now see and option to generate a Client Access Token. In this directory, create a file called '.env', containing the following:

    CLIENT_TOKEN = 'YOUR CLIENT ACCESS TOKEN'

You should now be able to run the script.

## Authors

This project was a collaboration between Tommy Chen, Andrew Pham, and Yao Yan.

## Sources

This project uses data collected and published on [Kaggle](https://www.kaggle.com/datasets/dhruvildave/spotify-charts).