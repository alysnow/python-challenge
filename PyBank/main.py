import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('PyBank','Resources','budget_data.csv')

# Create blank lists to iterate through rows
total_months = []
total_profit = []
profit_change = []

# Open csv
with open(budget_data_csv, 'r') as budget:

    # Create CSV variable
    csvreader = csv.reader(budget,delimiter=",") 

    # Skip the headers and iterate through the values
    header = next(csvreader)  

    # Iterate through the rows
    for row in csvreader: 

        # Append the total months and total profit to list
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Calculate difference between months and append to profit change
        profit_change.append(total_profit[i+1]-total_profit[i])
        
# Get the max and min of the profit change list
max_increase_value = max(profit_change)
max_decrease_value = min(profit_change)

# Compare the max and min using month list and index
max_increase = profit_change.index(max(profit_change)) + 1
max_decrease = profit_change.index(min(profit_change)) + 1 

# Print summary table
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease]} (${(str(max_decrease_value))})")

# Output file
output_file = os.path.join('PyBank','Analysis','Financial_Analysis.txt')

with open(output_file,"w") as file:
    
# Print Financial_Analysis txt file
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease]} (${(str(max_decrease_value))})")