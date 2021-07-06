# Import dependencies

import os
import csv

# Path to read data from resources folder
elections_csv=os.path.join("Resources", 'election_data.csv')

# Variables to store data
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
o_tooley_votes = 0

# Open and read election data file
with open(elections_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

# using for loop to loop through each row in the election data file
    for row in csvreader:

        # counting unique Voter Id 
        total_votes +=1
        #Results of the this conditional will be used to calculate each candidate's votes and percentage of votes each candidate won
        if row[2]=="Khan":
            khan_votes +=1
        elif row[2]=="Correy":
            correy_votes +=1
        elif row[2]=="Li":
            li_votes +=1
        elif row[2]=="O'Tooley":
            o_tooley_votes +=1


    # Find winner, make a dictionary from candidates and votes lists

    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    votes = [khan_votes, correy_votes, li_votes, o_tooley_votes]

    # zip candidates and votes together

    dict_candidates_and_votes = dict(zip(candidates,votes))
    key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

    #  Analysis summary
    khan_percent = (khan_votes/total_votes)*100
    correy_percent = (correy_votes/total_votes)*100
    li_percent = (li_votes/total_votes)*100
    o_tooley_percent = (o_tooley_votes/total_votes)*100

    print(f"Election Result")
    print(f"----------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------------")
    print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    print(f"Correy: {correy_percent: .3f}% ({correy_votes})")
    print(f"Li: {li_percent:.3f}% ({li_votes})")
    print(f"O'Tooley: {o_tooley_percent:.3f}% ({o_tooley_votes})")
    print(f"----------------------------------")
    print(f"Winner: {key})")
    print(f"----------------------------------")

# output Analysis file
output_file=os.path.join("Analysis")

with open(output_file, "w") as file:
    
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"--------------------------------------")
    file.write("\n")
    file.write(f"Total_Votes: {total_votes}")
    file.write("\n")
    file.write(f"---------------------------------------")
    file.write("\n")
    file.write(f"khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {o_tooley_percent:.3f}% ({o_tooley_votes})")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"------------------------------------------")


    




