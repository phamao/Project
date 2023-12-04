import nltk
from nltk import ngrams
from nltk.probability import FreqDist
from prepare_lyrics import prepare_lyrics
from megalist import megalist

def print_collocations(tokenlist):
    # Generate 5-grams from the token list
    fivegrams = ngrams(tokenlist, 2)

    # Calculate frequency distribution of 5-grams
    fivegrams_freq = FreqDist(fivegrams)

    # Filter out 5-grams that appear less than a certain number of times
    # You can adjust this threshold as needed
    filtered_fivegrams = {gram: count for gram, count in fivegrams_freq.items() if count >= 2}

    # Sort and get the top 10 5-grams (you can adjust the number)
    top_fivegrams = sorted(filtered_fivegrams, key=filtered_fivegrams.get, reverse=True)[:20]

    for fivegram in top_fivegrams:
        collocation_string = " ".join(fivegram)
        print(collocation_string)

# Example usage
print_collocations(megalist(prepare_lyrics('lyrics')))

