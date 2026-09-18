# read a csv file
import csv

with open("ipl_matches.csv","r") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        print(row["Winner"])