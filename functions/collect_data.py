from save_lyrics import save_lyrics

# Greatly extends possible searches in one session
while True:
    try:
        save_lyrics('charts.csv')
    except:
        break