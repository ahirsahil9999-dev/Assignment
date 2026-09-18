# Read the my_playlist.txt file you created and print each song 
# name in uppercase using Python file handling.

with open("my_playlist.txt","r") as f:
    for song in f:
        print(song.strip().upper())
        
print("Songs name Successfully uppercase !")