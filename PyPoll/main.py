

import os
import csv

#path to Resources/PyPoll_Resources_election_data.csv
file_name = os.path.join('Resources','PyPoll_Resources_election_data.csv')

#variables
poll_data = {}
total_votes = 0

#Open budget_data.csv
with open(file_name, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ',')
   next(csvreader, None)
   row = next(csvreader)
   #print(row)

   for row in csvreader:
    total_votes += 1
    if row [2]  in poll_data.keys():
      poll_data[row[2]] = poll_data[row[2]] + 1
    else:
      poll_data[row[2]] = 1

#The total number of votes cast
#A complete list of candidates who received votes

candidates = []
total_number_of_votes = []

for datum, value in poll_data.items():
    candidates.append(datum)
    total_number_of_votes.append(value)


#The percentage of votes each candidate won
percentage_votes = []
for n in total_number_of_votes:
    percentage_votes.append(round(n/total_votes * 100,1))


#The total number of votes each candidate won
#The winner of the election based on popular vote

voting_data = list(zip(candidates, total_number_of_votes, percentage_votes))

winners = []

for winner in voting_data:
   if max(total_number_of_votes) == winner[1]:
        winners.append(winner[0])

winning_candidate = winners[0]


# ```text
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
#```

print("Election Results")
print(f"Total Votes: {total_votes}")
print(f"Candidates: {candidates}")
print(f"Percentage of Candidates Won: {percentage_votes}")
print(f"Total Number of Candidates Won: {total_number_of_votes}")
print(f"Winning Candidate: **{winning_candidate}**")
 

Pypoll = open ('Results/results.txt',"w+")
Pypoll.write('\n'"------------------------------")
Pypoll.write('\n'"Election Results")
Pypoll.write('\n'"------------------------------")
Pypoll.write('\n' + "Total_votes: " + str(total_votes))
Pypoll.write('\n'"----------------------")
Pypoll.write('\n' + str(candidates[1]) + ": " + str(percentage_votes[1]) + "%  " +"("+str(total_number_of_votes[1])+")")
Pypoll.write('\n' + str(candidates[0]) + ": " + str(percentage_votes[0]) + "%  " +"("+str(total_number_of_votes[0])+")")
Pypoll.write('\n' + str(candidates[2]) + ": " + str(percentage_votes[2]) + "%  " +"("+str(total_number_of_votes[2])+")")
Pypoll.write('\n' + str(candidates[3]) + ": " + str(percentage_votes[3]) + "%  " +"("+str(total_number_of_votes[3])+")")
Pypoll.write('\n'"------------------------------")
Pypoll.write('\n'"Winner: " + str(winning_candidate))
Pypoll.write('\n'"------------------------------")