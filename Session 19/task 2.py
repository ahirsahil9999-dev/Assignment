# Create an object of the Song class for your favorite track from 
# Spotify, and print out its title and artist using object attributes.

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        
song = Song("Jhol", "Maanu")

print("Title: ",song.title)
print("Artist: ",song.artist)