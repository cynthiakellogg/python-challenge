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

#import dependencies
import os
import csv

#importing resources for analysis
file = os.path.join("Resources/election_data.csv")
#file = os.path.join("Resources", "election_data.csv")

#globaly scoped variables
total_vote_counter = 0
candidate_list = []
#collection 
candidtate_dict = {}

# candiate_dict = {
#     name1: 0,
#     name2: 0,
# }

#winner 
winner = ""

#open file and start reading it
with open(file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Read the header row first
    csv_header = next(csvfile)
    #check to make sure it's linked properly 
    #print(f"Header: {csv_header} ")
    #loop through the array
    for row in csv_reader:
        # count total votes
        total_vote_counter += 1
        # extract the canditate name from each row in column[2]
        cand_name = row[2]
        cand_vote_count = 0
        #conditional logic for what to do next 
        #check if name is already in canditate list
        #if name is not in array, then do something
        if cand_name not in candidate_list:
            candidate_list.append(cand_name) 
            #add canditate list (key) to dict and initialzie that value as 0   
            candidtate_dict.update({cand_name: 0,
                                })
            #and we want to add canditate vote count (key to dictionary and initialize that value as 1)
        else:
            candidate_list.append(cand_name)

#now we want to count all the names in the candidate list
khan_count = candidate_list.count("Khan")
correy_count = candidate_list.count("Correy")
li_count = candidate_list.count("Li")
otooley_count = candidate_list.count("O'Tooley")
#now we do some maths
khan_perc = khan_count/total_vote_counter*100
correy__perc = correy_count/total_vote_counter*100
li_perc = li_count/total_vote_counter*100
otooley_perc = otooley_count/total_vote_counter*100
    
print (f"Election Results")
print("------------------")
print(f"Total Votes:  {total_vote_counter}")
print(candidtate_dict)
print(f"Kan vote percent {otooley_perc}")
print(f"Winner: Khan!")

