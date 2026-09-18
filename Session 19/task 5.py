# Refactor your Song class so that it also tracks a play_count
# attribute (starting at 0), and add a method increment_play_count
# (self) that increases play_count by 1 each time it's called. 
# Show how you would use this to count how many times a user 
# plays a song.<br><br><em><strong>Hint:</strong> Call increment_play_count() 
# multiple times and print play_count to see the update.</em>

class Song:
    def __init__(self, title):
        self.title = title
        self.play_count = 0
        
    def increment_play_count(self):
        self.play_count += 1
        
song = Song("Jhol")

song.increment_play_count()
song.increment_play_count()
song.increment_play_count()
song.increment_play_count()

print("Title: ", song.title)
print("Play Count: ", song.play_count)