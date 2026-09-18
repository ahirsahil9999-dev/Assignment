# Use open() in write mode to create a file called my_playlist.txt
# and write the names of 5 songs you listened to this week, each on 
# a new line.

with open("my_playlist.txt","w") as f:
    f.write("Jhol\n")
    f.write("Duniyaa\n")
    f.write("Sahiba\n")
    f.write("Heeriye\n")
    f.write("Pardesiya\n")

print("Songs Written Successfully !!")