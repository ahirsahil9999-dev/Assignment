# Create a function get_playlist_duration(songs) that takes a list
# of song durations (in seconds) and returns the total duration in 
# minutes. Raise a custom exception InvalidDurationError if any duration
# in the list is negative.<br><br><em><strong>Hint:</strong> Define your
# own exception class by subclassing Exception.</em>

class InvalidDurationError(Exception):
    pass

def get_playlist(songs):
    try:
        for duration in songs:
            if duration < 0:
                raise InvalidDurationError
            
        result = sum(songs) / 60
        return result
        
    except InvalidDurationError:
        return "Enter A Positive Number"
    
songs = list(map(int, input("Enter A Song Durations In Second: ").split()))

print("Total Minutes:", get_playlist(songs))