# Election_Analysis

## Project Overview
In this project we worked with the Colorado Board of Elections to complete the following tasks regarding election audit results from a recent election:

1. Calculate the total number of votes cast
2. Get a complete list of candidates who receive votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on popular vote
6. Get the voter turnout for each county
7. Calculate the percentage of votes from each county
8. Determine the county with the highest turnout

## Resources
- Data Source: election_results.csv
- Software: Python 3.7, Visual Studio Code 

## Audit Results
A brief analysis of the election shows the following results and includes an image below:

- There were 369,711 votes cast in the election
    * This was determined by initializing a total vote counter to zero, creating a for loop to read each row of the election_results.csv file, and adding each row to         the total vote counter (with the exception of the header row which was skipped using the next() function. 

- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
    * We were able to go through all of the rows and find each unique candidate name by initializing a list to hold the name of each candidate, writing a script to get       the candidate's name in each row, creating a decision statement with the logical operator "not in" to see whether or not a candidate's name exists in our list,         if not the candidate's name is added.

- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
    * To obtain the number of votes each candidate received we initialized a dictionary to hold the candidate's name as the key and the votes cast for each candidate         as the values. After initializing the dictionary, we write a script to initialize a candidate's vote count to zero followed by another script that adds a vote to       the candidate's vote count all within the for loop that goes through all the rows in the file.
    * To find the percentage of votes each candidate won we use the following formula for each candidate, where the vote_percentage is the percent of the vote each           candidate earned, votes is equal to the number of votes that candiate received and total_votes is equal to the total number of votes cast in the election.             "float" changes the variable types from integers to floating point decimals. 
    * vote_percentage = float(votes) / float(total_votes) * 100 

- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.
    * The winner of the election was determined by initializing variables that hold the number of votes the winning candidate received, as well as who the winning           candidate is and their vote percentage. Next, we create a decision statement to determine the winner of the election as well as the winning count and winning           percentage and assign the variables we previously initialized to those values. "votes" represents the vote count of a candidate. 
    * if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

- The county results were:
  - 38,855 votes (10.5% of the vote) came from Jefferson County
  - 306,055 votes (82.8% of the vote) came from Denver County
  - 24,801 votes (6.7% of the vote) came from Arapahoe County
    * County results were determined in the same manner as the candidate results with initializing a dictionary to track the vote count for each county, wriitng a           script that initializes the county vote to zero, creating another script that adds a vote to the county's vote as we loop through the rows, and writing a for           loop to pull the county from our dictionary and retrieving the vote count. The vote percentage for each county was found with the same formula that was used for       finding the candidate's vote percentages.  

- The county with the largest number of votes was: Denver
    * Determining the county with the largest number of votes was set up in a similar way to determining the winning candidate, with variables initialized for tracking       the county with the largest turnout and the corresponding number of votes along with a decision statement listed below that looks to see which county has the           highest vote count.
    * if (vote_count > largest_county_votes):
            largest_county_votes = vote_count
            largest_county_turnout = county_name

![Election_results_screenshot](https://user-images.githubusercontent.com/120291854/212815146-46ba6803-20d2-4502-bcb1-777e530b793b.png)

## Summary
In this audit the script was used to answer various questions such as determining the total number of votes cast in the election, the winner of the election, as well as vote counts and vote percentages for each candidate and each county. For our analysis, much of the script used for obtaining candidate information was also used for obtaining county information from our election results file and with some modifications, our script could be used for analyzing other election results. For example, if we wanted to find the breakdown of candidate vote percentages by county we could modify our candidate tracker statement to include an if statement for each candidate, where the vote count only increases for that candidate if the vote was from the county in the if statement. We could repeat this for every county in the file, and then proceed to obtain the percentage of the vote a candidate won in each county by replacing the total vote in our formula with the total county vote as well as replacing the vote each candidate won, with the total number of votes the candidate won in that specific county. If we wanted to use the script for a different type of election, such as a runoff, then we could modify the winning candidate statement with an additional condition, that states the winning percent must be greater than or equal to 50%, else the candidates with the most votes and second most votes will go to a runoff election. 

