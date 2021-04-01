import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('PyPoll','Resources','election_data.csv')

# Create Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv
with open(election_data_csv, 'r') as elections:

    # Create csvreader variable
    csvreader = csv.reader(elections,delimiter=",")

    # Skip the headers and iterate through the values
    header = next(csvreader)

    # Iterate through the rows
    for row in csvreader:

        # Count Voter ID and save in total_votes variable
        total_votes +=1

        # Count the candidates names in each row and save total count to list
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

# Create dictionary to combine the two lists
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# Zip together list of candidates and the total votes and return the winner using a max function of the dictionary 
combined_candidates_votes = dict(zip(candidates,votes))
key = max(combined_candidates_votes, key=combined_candidates_votes.get)

# Calculate the candidate percent for summary table
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files
output_file = os.path.join('PyPoll','Analysis','Election_Results.txt')

with open(output_file,"w") as file:

# Print Elections_Results text file
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")