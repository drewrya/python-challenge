#----------------------------------------------------------------------------------------
#Create a Python script that analyzes the records in the \Resources\budget_data.csv file
#----------------------------------------------------------------------------------------

# Import modules
import os
import csv

#Set the CSV path
csvpath = os.path.join("Resources", "budget_data.csv")

#Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    #Create variables that will be used in the for loop and set equal to empty or zero
    totalMonths = 0
    total = 0
    greatestIncrease = 0
    greatestIncreaseDate = ""
    greatestDecreaseDate = ""
    previousProfitLoss = 0
    greatestDecrease = 0
    firstProfitLoss = 0
    lastProfitLoss = 0
    actualChange = 0
    totalChange = 0
    isFirstRow = "true"

    #Print header of the Python output to screen
    print("Financial Analysis")
    print("----------------------------")

    # Read each row of data after the header and analyze the different tasks
    for row in csvreader:
        #Set variables to the current working row in the data set
        currentMonth = row[0]
        currentProfitLoss = int(row[1])

        #Keeps a running taly of the total months in the csv file
        totalMonths = totalMonths + 1

        #Adds all of the total profits and losses
        total = total + currentProfitLoss

        #Calculates the current months net profit or loss
        actualChange = currentProfitLoss - previousProfitLoss
        totalChange = totalChange + actualChange

        #Keeps track of the greatest increase and decrease amounts/months
        if actualChange > greatestIncrease:
            greatestIncrease = actualChange
            greatestIncreaseDate = currentMonth
        if actualChange < greatestDecrease:
            greatestDecrease = actualChange
            greatestDecreaseDate = currentMonth

        #Calculates the current months net profit or loss
        #Store the first profit/loss      
        if isFirstRow == "true":
            firstProfitLoss = int(row[1])
            isFirstRow = "false"

        lastProfitLoss = int(row[1])

        previousProfitLoss = currentProfitLoss

    #Calculate the average rate of change
    changeInProfitLoss = lastProfitLoss - firstProfitLoss
    averageRateOfChange = round((changeInProfitLoss / totalMonths), 2)

    # Specify the file path to write to
    output_path = os.path.join("Analysis", "PyBank_Analysis.txt")

    # Create the file
    output_file = open(output_path, "w")

    # Print the total number of months included in the dataset
    print("Total Months: " + str(totalMonths))
    output_file.write("Total Months: " + str(totalMonths) +"\n")

    # The net total amount of "Profit/Losses" over the entire period
    print("Total: $" + str(total))
    output_file.write("Total: $" + str(total) +"\n")

    # The average of the changes in "Profit/Losses" over the entire period
    averageTotalChange = totalChange / totalMonths 
    print("Average Change: $" + str(averageRateOfChange))
    output_file.write("Average Change: $" + str(averageRateOfChange) +"\n")

    # The greatest increase in profits (date and amount) over the entire period
    print("Greatest Increase in Profits: " + str(greatestIncreaseDate) + " ($" + str(greatestIncrease) + ")")
    output_file.write("Greatest Increase in Profits: " + str(greatestIncreaseDate) + " ($" + str(greatestIncrease) + ")" +"\n")

    # The greatest decrease in losses (date and amount) over the entire period
    print("Greatest Decrease in Profits: " + str(greatestDecreaseDate) + " ($" + str(greatestDecrease) + ")")
    output_file.write("Greatest Decrease in Profits: " + str(greatestDecreaseDate) + " ($" + str(greatestDecrease) + ")")



