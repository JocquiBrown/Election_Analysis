# Add our depednencies
import csv
import os

# Assign a variable toload a file from a path.
file_to_load = os.path.join("Resources_Election_Analysis", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the elction results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
# Create a filename variable to a direct or indirect path to the file.

# Use the open statement to open the file as a text file
with open(file_to_save, "w") as txt_file:

# Write some data to the file
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# Close the file

#To Do: Perform Analysis.

    
    # 1. The total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
    # 5. The winner of the election based on popular vote.
    # Close the file.
