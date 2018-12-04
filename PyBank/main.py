import csv
import os

def sum(values):
    total = 0
    for value in values:
        total += int(value)
    return(total)

def average(numbers):
    length = len(numbers)
    return sum(numbers) / length

filepath = os.path.join('budget_data.csv')

with open("budget_data.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader, None)
    count = 0
    maxProfit = 0.0
    maxLoss = 0.0
    monthList = []
    totalProfit = []
    changeList = []

# goes through csv file and counts rows, appending empty lists with months and revenue.
    for row in reader:
        count = count + 1
        totalProfit.append(int(row[1]))
        monthList.append(row[0])
    

    # creating a new list of differences between a month and the month before. range has -1 value because last value will have nothing to compare to.
    changeList = [totalProfit[i+1] - totalProfit[i] for i in range(len(totalProfit)-1)]
    # average function rounded to 2 decimal places
    meanChange = round(average(changeList), 2)

    # created a default comparison number of maxProfit and set it to 0. While iterating through list, if the number is greater than maxProfit, it gets saved.
    for maxChange in changeList:
        if maxChange > maxProfit:
            maxProfit = maxChange
        else:
            maxProfit = maxProfit
    
    for minChange in changeList:
        if minChange < maxLoss:
            maxLoss = minChange
        else:
            maxLoss = maxLoss

    # Zipping together changeList and monthList after index 1. This is because the first month is irrelevant information when comparing profit.
    mapped = zip(changeList, monthList[1::])
    
    for profit, date in mapped:
        if profit == maxProfit:
            profDate = date
        elif profit == maxLoss:
            lossDate = date
        

    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${sum(totalProfit)}")
    print(f"Average Change: ${meanChange}")
    print(f"Greatest Increase in Profits: {profDate} (${maxProfit})")
    print(f"Greatest Decrease in Profits: {lossDate} (${maxLoss})")

with open("output.txt", 'w', newline='') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("-----------------------------\n")
    textfile.write(f"Total Months: {count}\n")
    textfile.write(f"Total: ${sum(totalProfit)}\n")
    textfile.write(f"Average Change: ${meanChange}\n")
    textfile.write(f"Greatest Increase in Profits: {profDate} (${maxProfit})\n")
    textfile.write(f"Greatest Decrease in Profits: {lossDate} (${maxLoss})")


    
    
                
    
    

# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period