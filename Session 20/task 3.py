# Build a class called Playlist that has a private attribute _songs 
# (a list of song names). Write methods to add a song, remove a song,
# and get the current list of songs using proper encapsulation.

class Playlist:
    def __init__(self):
        self._songs = []
        
    def add_song(self, song):
        self._songs.append(song)
        
    def remove_song(self, song):
        if song in self._songs:
            self._songs.remove(song)
            
    def get_songs(self):
        return self._songs
    
playlist = Playlist()

playlist.add_song("Jhol")
playlist.add_song("Sahiba")
playlist.add_song("Heeriye")

print("Songs: ", playlist.get_songs())

playlist.remove_song("Sahiba")

print("After Removing Song: ", playlist.get_songs())