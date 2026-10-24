playlists = [
    [210, 180, 240],
    [150, 200],
    [300, 120, 90]
]

long_songs = [
    duration
    for playlist in playlists
    for duration in playlist
    if duration > 200
]

print(long_songs)