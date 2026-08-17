spotify_rating = ['4.5', '3.0', '5', '4.2']

new_spotify_rating = [float(rating) for rating in spotify_rating]
print(new_spotify_rating)

higest_rating = max(new_spotify_rating)
print(higest_rating)