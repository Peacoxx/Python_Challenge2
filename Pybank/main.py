import os
import csv

# Construct the file path - tried using the same code from Cereal CSV, but could not figure out why the csv was not pulling. Had to get help via chat gpt
csvpath = os.path.join('/', 'Users', 'pamala', 'Documents', 'GitHub', 'python_challenge', 'Pybank', 'Resources', 'budget_data.csv')

# Initialize variables - received help via chat gpt 
total_months = 0
Total_Profit_Losses = 0
profit_changes = []  # List to store the changes in profit/losses
previous_month_profit = None  # To store the profit/loss of the previous month
greatest_increase = ["", 0]  # To store the date and amount of the greatest increase in profits
greatest_decrease = ["", 0]  # To store the date and amount of the greatest decrease in profits

# Open the file and read the contents
try:
    with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Skip the header row
        header = next(csvreader)
        
        # Read the first row to initialize previous_month_profit
        first_row = next(csvreader)
        previous_month_profit = int(first_row[1])
        total_months = 1
        Total_Profit_Losses += previous_month_profit
        
        # Process each row in the CSV file
        for row in csvreader:
            # Increment the total months count
            total_months += 1
           
            # Current month's profit/loss
            current_month_profit = int(row[1])
            Total_Profit_Losses += current_month_profit
            
            # Calculate change from previous month
            change = current_month_profit - previous_month_profit
            profit_changes.append(change)
            
            # Check for greatest increase
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change
            
            # Check for greatest decrease
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change
            
            # Update previous_month_profit to current month
            previous_month_profit = current_month_profit

        # Calculate the average change in "Profit/Losses"
        average_change = sum(profit_changes) / len(profit_changes) if profit_changes else 0

        print(f"Total Months: {total_months}")
        print(f"Total Profit/Losses: ${Total_Profit_Losses}")
        print(f"Average Change in Profit/Losses: ${average_change:.2f}")
        print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
        print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
#coding help from Chat GPT due to file error generated and tried various ways to code it and it would not work. 
except FileNotFoundError:
    print(f"File not found: {csvpath}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
