#Election Results
 # -------------------------
 # Total Votes: 3521001
 # -------------------------
 # Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
 # -------------------------
 # Winner: Khan
 # -------------------------

  # A complete list of candidates who received votes

  # The percentage of votes each candidate won

  # The total number of votes each candidate won

  # The winner of the election based on popular vote.
import os
import csv

file = os.path.join("Resources/03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv")
with open(file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#Read the header row first
    csv_header = next(csvfile)
    #print(f"Header: {csv_header} ")
    count = 0
    candidateDict = {}

    for row in csv_reader: 
        count+= 1
        candidateDict
    
    
print (f"Election Results")
print(f"Total Votes:  {count}")
print()
print()
print()
print()
print(f"Winner: ")

