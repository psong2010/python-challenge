import csv
import os

filepath = os.path.join('election_data.csv')

def votePercent(part, whole):
    return 100 * (part / whole)

with open(filepath, newline = '') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)

    count = 0
    khanCounter = 0
    correyCounter = 0
    liCounter = 0
    tooleyCounter = 0
    candidateList = []
    voteCounter = 0
    

    for row in csv_reader:
        count += 1
        if row[2] not in candidateList:
            candidateList.append(row[2])
        if row[2] == "Khan":
            khanCounter += 1
        if row[2] == "Correy":
            correyCounter += 1
        if row[2] == "Li":
            liCounter += 1
        if row[2] == "O'Tooley":
            tooleyCounter += 1
    
    khanPercent = round(votePercent(khanCounter, count), 3)
    correyPercent = round(votePercent(correyCounter, count), 3)
    liPercent = round(votePercent(liCounter, count), 3)
    tooleyPercent = round(votePercent(tooleyCounter, count), 3)


    totalVotes = [khanCounter, correyCounter, liCounter, tooleyCounter]
    percentVotes = [khanPercent, correyPercent, liPercent, tooleyPercent]

    mapped = list(zip(candidateList, totalVotes, percentVotes))
    
    for candidate, votes, percent in mapped:
        if votes > voteCounter:
            voteCounter = votes
            Winner = candidate

    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {count}")
    print("--------------------------")
    print(f"{candidateList[0]}: {khanPercent}% ({khanCounter})")
    print(f"{candidateList[1]}: {correyPercent}% ({correyCounter})")
    print(f"{candidateList[2]}: {liPercent}% ({liCounter})")
    print(f"{candidateList[3]}: {tooleyPercent}% ({tooleyCounter})")
    print("--------------------------")
    print(f"Winner: {Winner}")
    print("--------------------------")

with open('output.txt', 'w', newline= '') as textfile:
    textfile.write("Election Results\n")
    textfile.write("--------------------------\n")
    textfile.write(f"Total Votes: {count}\n")
    textfile.write("--------------------------\n")
    textfile.write(f"{candidateList[0]}: {khanPercent}% ({khanCounter})\n")
    textfile.write(f"{candidateList[1]}: {correyPercent}% ({correyCounter})\n")
    textfile.write(f"{candidateList[3]}: {tooleyPercent}% ({tooleyCounter})\n")
    textfile.write("--------------------------\n")
    textfile.write(f"Winner: {Winner}\n")
    textfile.write("--------------------------")


