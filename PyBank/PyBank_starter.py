# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change = 0
greatest_increase_month = ""
greatest_decrease_month = ""

# Add more variables to track other necessary financial data
average_change = 0
net_change_list = []
months_list = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    prev_net = int(first_row[1])
    total_months += 1
    total_net += prev_net

    # Go through the rows of the csv file
    for row in reader:

        # Track the net total and the total number of months
        total_net += int(row[1])
        total_months += 1
        
        # Calculate change between months and add to net_change_list
        net_change = int(row[1]) - prev_net
        net_change_list.append(net_change)
        months_list.append(row[0])

        #update previous net value for the next iteration
        prev_net = int(row[1])

    #Calculate average change
    average_change = round(sum(net_change_list) / len(net_change_list),2)

    # Calculate the greatest increase and decrease in profits
    greatest_increase = max(net_change_list)
    greatest_decrease = min(net_change_list)

    #Find the location in the net_change_list of the greatest increase and decrease
    greatest_increase_index = net_change_list.index(greatest_increase)
    greatest_decrease_index = net_change_list.index(greatest_decrease)

    #Find which months the greatest increase and decrease happened in
    greatest_increase_month = months_list[greatest_increase_index]
    greatest_decrease_month = months_list[greatest_decrease_index]

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
