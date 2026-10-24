def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    user_playlists = playlists.setdefault(user, {})
    songs = user_playlists.setdefault(playlist_name, [])

    songs.append({
        "title": song_title,
        "artist": artist
    })

    return playlists


playlists = {}

add_song_to_playlist(
    playlists, "raj", "Favourites", "Kesariya", "Arijit Singh"
)

add_song_to_playlist(
    playlists, "raj", "Favourites", "Believer", "Imagine Dragons"
)

add_song_to_playlist(
    playlists, "simran", "Chill", "Perfect", "Ed Sheeran"
)

print(playlists)