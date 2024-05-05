import os
import csv
#path to csv
election_data = os.path.join("Resources", "election_data.csv")
#Set variables
total_votes = 0
candidates = {}
# open and read csv
with open(election_data) as csv_file:  
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader) #this skips the header row
    #loop data for each row
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2] #using row[2] because first row is considered 0 and candidate is in row 3

        #if else statements, provide conditionals as we want to identify complete list of candidates who received votes
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1
#calculate total votes to determine winner and set variables
results = []
winner = None #this is used because it confirms no winner has been identified at this point yet
max_votes = 0

#create new for loop
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))
    if votes > max_votes:
        max_votes = votes
        winner = candidate
#Print outcomes
print("election results")
print(f"Total Votes: {total_votes}")
for result in results:
    print(f"{results[0]}: {result[2]:.3f}% ({result[1]})")
print(f"Winner: {winner}")
          
    
