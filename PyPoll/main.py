##everybody in the house say PYYYYYPOOOOLLLLL

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# make the variable budget_data pull from the correct directory
budget_data_path = os.path.join('Resources', 'election_data.csv')


# opening mah data
with open(budget_data_path) as budget_data:


# CSV reader specifies delimiter and variable that holds contents
    election_data_read = csv.reader(budget_data, delimiter=',')

# Read the header row first (skip this step if there is no header)
    election_data_header = next(election_data_read)

#initialize counters

    cand_count=0
    vote_count=0
    highvote = 0
    winner = ''

#create first dictionary

    candidates = {}


# traverse through rows in CSV file
# adds to the dicitonary if it needs to or creates new keys in the dictionary
    for row in election_data_read:
   
        candidate_list = candidates.keys()
        vote_count += 1

        if row[2] in candidate_list:
            current_votes = candidates[row[2]] + 1
            candidates [row[2]] = current_votes
        else:
            cand_count =+ 1
            candidates [row[2]] = 1

# print stuff to the screen
print(f'                 ')
print(f'                 Election Results ')
print(f' -------------------------------------------------- ')
print(f'     Total Number of votes cast:  {vote_count}')
print(f'                 ')
 
candidate_list = candidates.keys()
#Prints Candidate Summary Data to screen
for name in candidate_list:
    votes = candidates[name]
    vote_percent = round ((votes * 100)/vote_count, 2)
    if votes > highvote:
        highvote = votes
        winner = name
    print(f'{name}:  {vote_percent}%  with {votes} votes  ')
print(f'---------------------------------------------')
print(f'                 ')
print(f'    That means that the winner is {winner}')
print(f'---------------------------------------------')


#This code came straight from the lesson ya'll
# Specify the file to write to
output_path = os.path.join("Analysis", "My_Analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open('My_Analysis.txt', 'w') as f:
    
    # write mah Election Results

    f.write('     Election Results:\n')
    f.write('------------------------------\n')
    

    for name in candidate_list:
        votes = candidates[name]
        vote_percent = round ((votes * 100)/vote_count, 2)
        if votes > highvote:
            highvote = votes
            winner = name
        f.write(f'{name}:  {vote_percent}%  with {votes} votes \n ')

    f.write(f'---------------------------------------------\n')
    f.write(f'                 \n')
    f.write(f'    That means that the winner is {winner}\n')
    f.write(f'---------------------------------------------\n')
