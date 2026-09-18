# Create a playlist of 6 songs (as a list of strings) and use 
# enumerate() to print each song with its position like Spotify's 
# tracklist (e.g., '1. Kesariya').

playlist = [
    "Kesariya",
    "Tum Hi Ho",
    "Apna Bana Le",
    "Chaleya",
    "Heeriye",
    "Tere Vaaste"
]

for position, song in enumerate(playlist, start=1):
    print(f"{position}. {song}")