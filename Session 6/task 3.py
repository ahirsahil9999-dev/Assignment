# Remove a playlist from the playlist_prices dictionary using the
# del statement. Print the dictionary after deletion to confirm 
# the change.

playlist_prices = {
    "Top Hits": 100,
    "Chill Vibes": 80,
    "Workout Mix": 120,
    "Bollywood Beats": 90,
    "Lo-Fi Study": 70
}

del playlist_prices["Workout Mix"]

print(playlist_prices)