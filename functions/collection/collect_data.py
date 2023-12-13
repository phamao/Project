from save_lyrics import save_lyrics

###################################################
# Continuously run this to gather more song lyrics.
###################################################

while True:
    try:
        save_lyrics('data/charts.csv')
    except:
        break