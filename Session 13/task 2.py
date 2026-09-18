# Build a recursive function sum_playlist_durations(durations) that takes 
# a list of song durations (in seconds) and returns the total duration,
# similar to how Spotify totals a playlist.

def sum_playlist_durations(durations):
    if not durations:
        return 0

    return durations[0] + sum_playlist_durations(durations[1:])

durations = list(map(int, input("Enter Song Durations In Seconds: ").split()))

result = sum_playlist_durations(durations)
print("Total Durations:", result)