# Data I need to retrieve
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of the election based on the popular vote


# Add our dependicies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save a file from a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate options
candidate_options = []

# Candidate votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze data here
    # Read the file with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            
            # Add the candidate option name to the candidate list
            candidate_options.append(candidate_name)
            
            # Track specific candidates vote count
            candidate_votes[candidate_name] = 0

        # Add votes to specific candidates vote count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate list
for candidate_name in candidate_votes:
            
    # Get vote count of a candidate
    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes
    vote_percentage = (float(votes) / float(total_votes)) * 100

    # to do: Print each candidates name, vote count, and  vote percentage
    print(f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")
    
    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count
    if(votes > winning_count) and (vote_percentage > winning_percentage):

        winning_count = votes

        winning_percentage = vote_percentage

        winning_candidate = candidate_name

# Print winning candidates name, count, and percentage of votes
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.2f}%\n"
    f"---------------------------\n")
print(winning_candidate_summary)





# Print total votes
# print(candidate_votes)