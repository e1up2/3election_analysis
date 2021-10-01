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


# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze data here
    # Read the file with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)