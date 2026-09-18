# You received a dataset of ratings as strings from Spotify: 
# ['4.5', '3.0', '5', '4.2']. Use type casting to convert these to 
# floats, then find and print the highest rating.<br><br><em><strong>Hint:
# </strong> Use the float() function inside a loop or list comprehension.
# </em>

spotify_rating = ['4.5', '3.0', '5', '4.2']

new_spotify_rating = [float(rating) for rating in spotify_rating]
print(new_spotify_rating)

higest_rating = max(new_spotify_rating)
print(higest_rating)