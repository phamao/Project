from wordcloud import WordCloud
import matplotlib.pyplot as plt

def wordcloudgenerator(lists):
    text = [" ".join(t) for t in lists]
    alltext = " ".join(text)

    wordcloud = WordCloud(max_font_size=40).generate(alltext)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig("allwordcloud.png")


