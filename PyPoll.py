# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Assign a variable for the total votes and initialize
total_votes = 0

#declare new list
candidate_options = []

#Declare the empty dictionary
candidate_votes = {}
winning_count = 0
winning_percentage = 0

#winning candidate and winning count tracker
winning_candidate = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)
    
    #Print each row in the csv file
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1

        #Print candidates name from each row
        candidate_name = row[2]

        #If the candidate does not match an existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            #Track candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to candidate's count
        candidate_votes[candidate_name] += 1

#Determine % of votes for each candidate by looping through the counts
#Iterate through the candidate list.
for candidate_name in candidate_votes:
    #retrieve vote count of candidate
    votes = candidate_votes[candidate_name]

    #calculate % of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #print the candidate name of % votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine winning vote count and candidate
    #determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #set winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
    

        