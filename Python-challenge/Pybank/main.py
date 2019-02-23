#-----------------
# SCOPE:  
# Define lists with Months, Total Profit and Losses(PL) and Change of profit and losses, each one by itself so we can work on them separely and then with the index method, being able to analize the results. 
#-----------------


# Importing modules (OS to create file paths across operating systems // CSV for reading CSV files // SYS to export the summary to an output file 
import os
import csv
import sys

# Path to collect data from the Resources folder
csvpath = os.path.join("..","Resources","budget_data.csv")

# Export the summary into a text file 
sys.stdout = open('PyBank_Summary.txt', 'w')

# Define the lists that we will use
total_months=[]
total_PL=[]
change_PL=[] #this list will be usefull for the Average of Change 


# Read using CSV module
with open(csvpath,newline="", encoding="utf-8") as budget_data:

    # Split the data on commas
    csvreader = csv.reader(budget_data,delimiter=",")

    # To skip the first row (header in this case) of the file  
    header = next(csvreader)

    # Create a list of months and a list of total Proffit & Losses (from now on PL) 
    for row in csvreader:

       total_months.append(row[0])
       total_PL.append(int(row[1]))

   # Average of change. first we will obtain a list of the change of PL 
    for i in range(len(total_PL)-1):

       change_PL.append(total_PL[i+1]-total_PL[i])

# To obtain the maximum and minimum values the change_PL list made above 
max_increase_profits = max(change_PL)
max_decrease_profits = min(change_PL)

# To obtain the maximum increase month -and maximum decrease-, we need to know the index of the maximum increase in profits form it's list so we can use it in the months list (because will have te same index number)
Index_increase_months = change_PL.index(max(change_PL)) + 1
Index_decrease_months = change_PL.index(min(change_PL)) + 1

max_increase_month = total_months[Index_increase_months]
max_decrease_month = total_months[Index_decrease_months]

# Average of change! (rounded with two decimals)
Average_change = round(sum(change_PL)/len(change_PL),2)

# Print the Summary in an external text file called "PyBank_Summary.txt" (see line 16)
print(" ")
print("Financial Analysis")
print("---------------------------------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_PL)}")
print(f"Average Change: {Average_change}")
print(f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_profits))})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_profits))})")
print("---------------------------------------------------")

# Print the Summary in the interactive shell 
print(" ",file = sys.stderr)
print("Financial Analysis",file = sys.stderr)
print("---------------------------------------------------",file = sys.stderr)
print(f"Total Months: {len(total_months)}",file = sys.stderr)
print(f"Total: ${sum(total_PL)}",file = sys.stderr)
print(f"Average Change: {Average_change}",file = sys.stderr)
print(f"Greatest Increase in Profits: {max_increase_month} (${(str(max_increase_profits))})",file = sys.stderr)
print(f"Greatest Decrease in Profits: {max_decrease_month} (${(str(max_decrease_profits))})",file = sys.stderr)
print("---------------------------------------------------",file = sys.stderr)