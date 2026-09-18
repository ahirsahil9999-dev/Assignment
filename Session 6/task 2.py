# Write a function update_playlist_price(playlist, new_price) that
# updates the price of a given playlist in the playlist_prices 
# dictionary. Test it by updating the price of any one playlist 
# and printing the updated dictionary.

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