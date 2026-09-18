# Define a Python class called Song with attributes title, artist, 
# and duration (in seconds), and use the __init__() constructor 
# to initialize these values when creating an object.

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        
song = Song("Jhol","Maanu", 234)

print(song.title)
print(song.artist)
print(song.duration)