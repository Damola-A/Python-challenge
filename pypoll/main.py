import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

votes_num = 0
candidates = []
votes_count = []
percentages = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        candidate = row[2]
        votes_num = votes_num + 1

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            votes_count[candidate_index] = votes_count[candidate_index] + 1

        else:
            candidates.append(candidate)
            votes_count.append(1)

    max_votes = votes_count [0]
    max_no = 0

    for count in range(len(candidates)):
        votes_percentage = '{:.3f}'.format((votes_count[count]/votes_num)*100)
        percentages.append(votes_percentage)

        if votes_count[count] > max_votes:
            max_votes = votes_count[count]
            max_no = count

    winner = candidates[max_no] 
        
    print ("Election Results")
    print ("----------------------------------")
    print ("Total votes:" + str(votes_num))
    print ("----------------------------------")
    for count in range(len(candidates)):
        print (f"{candidates[count]}: {percentages[count]}% ({votes_count[count]})")
    print ("----------------------------------")
    print (f"Winner: {winner}")
    print ("----------------------------------")

    output_file = os.path.join('Analysis', 'election_data.txt')

    writer= open(output_file, "w") 

    writer.write("Election Results\n")
    writer.write ("----------------------------------\n")
    writer.write (f"Total votes: {votes_num}\n")
    writer.write ("----------------------------------\n")
    for count in range(len(candidates)):
        writer.write (f"{candidates[count]}: {percentages[count]}% ({votes_count[count]})\n")
    writer.write ("----------------------------------\n")
    writer.write (f"Winner: {winner}\n")
    writer.write ("----------------------------------\n")