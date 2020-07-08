#----------------------------------------------------------------------------------------
#Create a Python script that analyzes the records in the \Resources\election_data.csv file
#----------------------------------------------------------------------------------------

# Import modules
import os
import csv

#Set the CSV path
csvpath = os.path.join("Resources", "election_data.csv")

#Set the file path to write to
output_path = os.path.join("Analysis", "PyPoll_Analysis.txt")

# Create the file
output_file = open(output_path, "w")

#Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    #Print header of the Python output to screen
    print("Election Results")
    output_file.write("Election Results"+"\n")
    print("----------------------------")
    output_file.write("----------------------------"+"\n")

    #Declare variables and set to zero before iterating through the for loop
    candidateOneCount = 0
    candidateTwoCount = 0
    candidateThreeCount = 0
    candidateFourCount = 0
    totalVotes = 0
    candidate_Array = []

    # Read each row of data after the header and analyze the different tasks in a for loop
    for row in csvreader:
        #Keeps a running tally of the total votes in the csv file 
        totalVotes = totalVotes + 1
    
        #Creates a unique list of candidates who received votes
        if row[2] not in candidate_Array:
            candidate_Array.append(row[2])

        #Increments each candidates vote count if the name in the row matches their name
        if row[2] == candidate_Array[0]:
            candidateOneCount = candidateOneCount + 1
        elif row[2] == candidate_Array[1]:
            candidateTwoCount = candidateTwoCount + 1
        elif row[2] == candidate_Array[2]:
            candidateThreeCount = candidateThreeCount + 1
        elif row[2] == candidate_Array[3]:
            candidateFourCount = candidateFourCount + 1
    
    #Calculates and formats the vote percentages
    candidateOnePercent = '{0:.3f}'.format((candidateOneCount/totalVotes)*100)
    candidateTwoPercent = '{0:.3f}'.format((candidateTwoCount/totalVotes)*100)
    candidateThreePercent = '{0:.3f}'.format((candidateThreeCount/totalVotes)*100)
    candidateFourPercent = '{0:.3f}'.format((candidateFourCount/totalVotes)*100)
    
    #Output the candidates with their vote count and vote percentage
    print("Total Votes: "+ str(totalVotes))
    output_file.write("Total Votes: "+ str(totalVotes)+"\n")
    print("----------------------------")
    output_file.write("----------------------------"+"\n")
    print(candidate_Array[0] + ": " + candidateOnePercent + "% (" + str(candidateOneCount) + ")")
    output_file.write(candidate_Array[0] + ": " + candidateOnePercent + "% (" + str(candidateOneCount) + ")"+"\n")
    print(candidate_Array[1] + ": " + candidateTwoPercent + "% (" + str(candidateTwoCount)+ ")")
    output_file.write(candidate_Array[1] + ": " + candidateTwoPercent + "% (" + str(candidateTwoCount)+ ")"+"\n")
    print(candidate_Array[2] + ": " + candidateThreePercent + "% (" + str(candidateThreeCount)+ ")")
    output_file.write(candidate_Array[2] + ": " + candidateThreePercent + "% (" + str(candidateThreeCount)+ ")"+"\n")
    print(candidate_Array[3] + ": " + candidateFourPercent + "% (" + str(candidateFourCount)+ ")")
    output_file.write(candidate_Array[3] + ": " + candidateFourPercent + "% (" + str(candidateFourCount)+ ")"+"\n")

    #The winner of the election based on popular vote
    #Determine the highest voter count and set the winner to that candidate
    winnerCount = candidateOneCount
    winner = candidate_Array[0] 

    if candidateTwoCount > winnerCount:
            winnerCount = candidateTwoCount
            winner = candidate_Array[1] 
    elif candidateThreeCount > winnerCount:
            winnerCount = candidateThreeCount
            winner = candidate_Array[2] 
    elif candidateFourCount > winnerCount:
            winnerCount = candidateFourCount
            winner = candidate_Array[3] 

    #Output the winner information to the console
    print("----------------------------")
    output_file.write("----------------------------"+"\n")
    print("Winner: " + str(winner))
    output_file.write("Winner: " + str(winner))