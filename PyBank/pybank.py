# -*- coding: UTF-8 -*-
"PyBank Homework Starter File."
# Dependencies
import csv
import os
# Files to load and output (update with correct file paths)
file_to_load = os.path.join(“Resources”, “budget_data.csv”)  # Input file path
file_to_output = os.path.join(“analysis”, “budget_analysis.txt”)  # Output file path
# Define variables to track the financial data
total_months = 0
total_net = 0
net_change = 0
average_change = 0
# Add more variables to track other necessary financial data
net_change_list = []
months = []
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    # Skip the header row, not sure if this skips entire header or just date
    header = next(reader)
    # Extract first row to avoid appending to net_change_list
    #first_row = next(reader)
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    # Track the total months and net total
    for row in reader:
        total_net += int(row[1])
        total_months += 1
          #Calculate the monthly change
        net_change = int(row[1]) - prev_net
        net_change_list.append(net_change)
        months.append(row[0])
        # Update previous net
        prev_net = int(row[1])
# Calculates the average change
average_change = sum(net_change_list) / len(net_change_list)
print(total_months)
print(total_net)
print(average_change)












