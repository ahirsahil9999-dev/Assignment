# You have a list of favorite song names: ['Kesariya', 'Believer', 'Shape of You', 'Blinding Lights', 'Excuses']. 
# Use the enumerate() function in a for loop to print each song 
# with its playlist position (starting from 1).

songs = ['Kesariya', 'Believer', 'Shape of You', 'Blinding Lights', 'Excuses']

for position, song in enumerate(songs, start=1):
    print(position, song)