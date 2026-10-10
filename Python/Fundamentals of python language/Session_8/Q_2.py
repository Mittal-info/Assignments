def extract_artist(song_title):
    dash_position = song_title.index("-")
    artist = song_title[dash_position + 2:]
    return artist


result = extract_artist("Kesariya - Arijit Singh")
print(result)