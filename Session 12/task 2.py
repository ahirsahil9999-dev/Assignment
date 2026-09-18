# Given a list of song titles from Spotify with extra spaces and inconsistent casing, use map() and a lambda function to clean each title so that it is stripped of spaces and converted to title case (e.g., ' shape OF you ' → 'Shape Of You').

songs = [" shape OF you ", " blinding LIGHTS ", " perfect ", " someone LIKE you "]

result = list(map(lambda song: song.strip().capitalize(), songs))

print(result)