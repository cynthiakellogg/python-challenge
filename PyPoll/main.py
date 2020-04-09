#import dependencies
import os
import csv

# importing resources for analysis
file = os.path.join("Resources/election_data.csv")

# globaly scoped variables
total_vote_counter = 0
candidate_list = []
candidtate_dict = {}
winning_candidate = ""
winning_count = 0

# open file and start reading it
with open(file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvfile)
    # loop through the array
    for row in csv_reader:
        # count total votes
        total_vote_counter += 1
        # extract the canditate name from each row in column[2]
        cand_name = row[2]
        # check if name is already in canditate list if name is not in array, then do something
        if cand_name not in candidate_list:
            candidate_list.append(cand_name)
            # add canditate list (key) to dict and initialzie that value as 0
            candidtate_dict[cand_name] = 0
            # and we want to add canditate vote count (key to dictionary and initialize that value as 1)
        candidtate_dict[cand_name] = candidtate_dict[cand_name] + 1

# create a new output path
csv_output = os.path.join("election_results.txt")

with open(csv_output, 'w') as export_csv:
    total_votes = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_vote_counter}\n"
        f"-------------------------\n"
    )
    print(total_votes)
    export_csv.write(total_votes)

    for candidate in candidate_list:

        count = candidtate_dict[candidate]
        perc = count / total_vote_counter * 100

        if (count > winning_count):
            winning_count = count
            winning_candidate = candidate

        candidate_output = f"{candidate}: {perc:.3f}% ({count})\n"
        print(candidate_output)
        export_csv.write(candidate_output)

    winner = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winner)

    export_csv.write(winner)

#follow up questions 
# 1. Why did we use a dictionary to store candidates in? vs. a list
# 2. If statements don't need else statements? 