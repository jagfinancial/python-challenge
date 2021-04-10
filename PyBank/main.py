
#import file
import os
import csv

#path to csv resources/budget_data.csv

file_name = os.path.join('Resources','budget_data.csv')

#input variables
total_months = 0
total_profit_loss = 0
variances = []
date_counter = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#Open budget_data.csv
with open(file_name, newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	next(csvreader, None)
	row = next(csvreader)

	#The total number of months included in the dataset
	past_profit = int(row[1])
	total_months = total_months + 1
	total_profit_loss = total_profit_loss + int(row[1])
	greatest_increase = int(row[1])
	greatest_increase_month = row[0]

	for row in csvreader:
		total_months = total_months + 1
		total_profit_loss = total_profit_loss + int(row[1])

	#The net total amount of "Profit/Losses" over the entire period
		variance = int(row[1]) - past_profit
		variances.append(variance)
		past_profit = int(row[1])
		date_counter.append(row[0])

	#The greatest increase in profits (date and amount) over the entire period
		if int(row[1]) > greatest_increase:
			greatest_increase = int(row[1])
			greatest_increase_month = row[0]

	#The greatest decrease in losses (date and amount) over the entire period
		if int(row[1]) < greatest_decrease:
			greatest_decrease = int(row[1])
			greatest_decrease_month = row[0]


	#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
		average_variance = sum(variances)/len(variances)

		increase = max(variances)
		decrease = min(variances)

#Financial Analysis
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

	print("Financial Analysis")
	print(f"Total Months:   {total_months}")
	print(f"Total Amount:   ${total_profit_loss}")
	print(f"Average Change:  ${round(average_variance,2)}")
	print(f"Greatest Increase in Profits:  {greatest_increase_month} (${increase})")
	print(f"Greatest Decrease in Profits:  {greatest_decrease_month} (${decrease})")


#Analysis Files
	Pybank = open("analysis.txt","w+")
	Pybank.write("Financial Analysis")
	Pybank.write('\n' + "Total Months " + str(total_months))
	Pybank.write('\n' + "Total Amount $" + str(total_profit_loss))
	Pybank.write('\n' + "Average Change $" + str(round(average_variance,2)))
	Pybank.write('\n' + "Greatest Increase in Profits: " + str(greatest_increase_month) + "($" + str(increase) + ")")
	Pybank.write('\n' + "Greatest Decrease in Profits: " + str(greatest_decrease_month) + "($" + str(decrease) + ")")
