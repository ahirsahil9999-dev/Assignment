playlist_prices = {
    "Top Hits": 100,
    "Chill Vibes": 80,
    "Workout Mix": 120,
    "Bollywood Beats": 90,
    "Lo-Fi Study": 70
}

def update_playlist_price(playlist,new_price):
    playlist_prices[playlist] = new_price

update_playlist_price("Top Hits",125)
print(playlist_prices)