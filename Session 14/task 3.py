# Download a sample CSV file of IPL cricket match scores
# (or create your own with columns: Match, Team1, Team2, Winner),
# then write Python code to read the CSV and print the name of 
# the winning team for each match.

import csv

with open("ipl_matches.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["Match", "Team1", "Team2", "Winner"])
    writer.writerow(["Match 1", "CSK", "MI", "CSK"])
    writer.writerow(["Match 2", "RCB", "KKR", "KKR"])
    writer.writerow(["Match 3", "GT", "RR", "GT"])
    writer.writerow(["Match 4", "DC", "SRH", "SRH"])
    writer.writerow(["Match 5", "MI", "RCB", "MI"])

print("CSV file created successfully!")