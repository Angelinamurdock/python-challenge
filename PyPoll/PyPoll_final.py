# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_vote_count = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    csvreader = csv.reader(election_data, delimiter= ",")

    # Skip the header row
    header = next(csvreader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Find total vote count 
        total_vote_count += 1

        # Set candidate name to everything in column 3
        candidate_name = row[2]

        # If the candidate is not already in the candidate dictionary, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidates count
        candidate_votes[candidate_name] += 1


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    election_results = (
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_vote_count}\n"
        "-------------------------\n"
    )

    # Print election results(total vote) to terminal and write to text file
    print(election_results)
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    # Get the vote count and calculate the percentage
    for candidate_name, votes in candidate_votes.items():
        vote_percentage = (votes / total_vote_count) * 100  # Calculate the percentage

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate_name

        # Print the candidate and their votes to terminal and write it in the text file
        candidate_result = (
            f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n"
        )
        print(candidate_result)
        txt_file.write(candidate_result)

    # Generate the winning candidate summary
    winning_summary = (
        "-------------------------\n"
        f"Winner: {winning_candidate}\n"
        "-------------------------\n"
    )

    # Print the winning candidate summary to terminal and add it to the text file
    print(winning_summary)
    txt_file.write(winning_summary)