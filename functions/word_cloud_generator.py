from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import pathlib

def wordcloudgenerator(lists, name):

    wordcloud_directory = os.path.abspath('.') + '/'

    # Creates the lyrics directory, if it does not currently exist
    pathlib.Path(wordcloud_directory).mkdir(exist_ok=True)

    text = [" ".join(t) for t in lists]
    alltext = " ".join(text)

    wordcloud = WordCloud(max_font_size=40).generate(alltext)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(wordcloud_directory + name + '_wordcloud.txt')
