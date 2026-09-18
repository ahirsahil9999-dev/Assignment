# Write a script that lists all files in your current directory using
# the os module, and prints only those files with a .jpg or .png
# extension.<br><br><em><strong>Hint:</strong> Use os.listdir() and 
# string methods to filter file names.</em>

import os

files = os.listdir()

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        print(file)
        
# thier a no file like endwith .jpg and .png in folder