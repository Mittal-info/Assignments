import random

songs = [
    "Kesariya",
    "Shape of You",
    "Believer",
    "Perfect",
    "Channa Mereya",
    "Levitating",
    "Apna Bana Le",
    "Tum Hi Ho"
]

daily_playlist = random.sample(songs, 3)

print("Today's Spotify Playlist:")

for song in daily_playlist:
    print(song)