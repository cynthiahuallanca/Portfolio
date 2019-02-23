#-----------------
# SCOPE:  
# Obtain the unique list of candidates to display the results. 
# Separate in two lists the votes and candidates so we can know the maximum in the votes list and apply the index of that to the candidates list to know the winner 
#-----------------


# Importing modules (OS to create file paths across operating systems // CSV for reading CSV files // SYS to export the summary to an output file 
import os
import csv
import sys

# Path to collect data from the Resources folder
csvpath = os.path.join("..", "Resources", "election_data.csv")

# Export the summary into a text file 
sys.stdout = open('PyPoll_Summary.txt', 'w')

# Define the lists that we will use
Votes=[]
Total_candidates=[]
Unique_candidates=[]
Candidates=[]
Count_per_candidate=[]

# Read using CSV module
with open(csvpath, newline='', encoding="utf8") as election_data:

    # Split the data on commas
    csvreader = csv.reader(election_data, delimiter=',')

    # To skip the first row (header in this case) of the file  
    header = next(csvreader)

    for row in csvreader:
        
        # To obtain the total count of votes (length)
        Votes.append(row[0])
        length = str(len(Votes))
          
        # To form the list of all candidates 
        Total_candidates.append(row[2])

    # To obtain a unique list of candidates. 
    # Benefit: In further elections we will have different names and numbers of candidates, so this approach will allow us to use the same code, as the list will be automatically update it (no hardcoding!) 
    for i in Total_candidates:
        if i not in Unique_candidates:
            Unique_candidates.append(i)

    # Obtain total count of each candidate, with comprehension list method 
    comprehension_list_total_count = [[x,Total_candidates.count(x)] for x in set(Total_candidates)]

    # Create a dictionary with the comprehension list
    summary_total_candidates = dict((x,Total_candidates.count(x)) for x in set(Total_candidates))

    # Obtain keys and values from the dictionary 
    for key in summary_total_candidates:
        keys = key
    for value in summary_total_candidates.items():
        values = value
    
    # To obtain the winner we need to know the one that recevied more votes 
    # Create a list of candidates and another for the votes. We will use the index of the maximum value in the votes list so we can apply this in the candidates list to know the winner's name 
    for row in comprehension_list_total_count:
       Candidates.append(row[0])
       Count_per_candidate.append(int(row[1]))

    # Obtain the max value of the list of votes, index of it and finally the winner! 
    max_increase_value = max(Count_per_candidate)
    max_increase_value_index = Count_per_candidate.index(max_increase_value)
    winner = Candidates[max_increase_value_index]

# Print the Summary in an external text file called "PyPoll_Summary.txt" (see line 17)
print(" ")
print("Election Results")
print("-----------------------")
print(f"Total votes: {length}")
print("-----------------------")

for key, value in summary_total_candidates.items():
    print(f"{key}: {round((int(value)/int(length))*100),3}% ({value})") 
print("-----------------------") 
print(f"Winner: {winner}")

# Print the Summary in the interactive shell 
print(" ",file = sys.stderr)
print("Election Results",file = sys.stderr)
print("-----------------------",file = sys.stderr)
print(f"Total votes: {length}",file = sys.stderr)
print("-----------------------",file = sys.stderr)

for key, value in summary_total_candidates.items():
    print(f"{key}: {round(((int(value)/int(length))*100),1)}% ({value})",file = sys.stderr) 
print("-----------------------",file = sys.stderr) 
print(f"Winner: {winner}",file = sys.stderr)