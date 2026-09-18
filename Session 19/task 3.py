# Add a method play_preview(self) to your Song class that prints 
# 'Playing 30-second preview of [title] by [artist]'. Call this 
# method for your Song object.

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        
    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")
    
song = Song("Jhol", "Maanu")

song.play_preview()