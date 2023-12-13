from prepare_lyrics import prepare_lyrics

# Given a list of tuples from prepare_lyrics.py, combines all the lyrics into one big list.
def megalist(tuple_list):

    token_megalist = []

    # For each tuple in the tuple_list
    for song_tuple in tuple_list:

        # Adds the lyrics to the megalist
        for token in song_tuple[1]:
            token_megalist.append(token)

    return token_megalist

print('Word Count: {count}'.format(count=len(megalist(prepare_lyrics('lyrics/')))))