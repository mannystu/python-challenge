##What up. its me ya boi PyBank
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# make the variable budget_data pull from the correct directory
budget_data_path = os.path.join('Resources', 'budget_data.csv')


# opening mah data
with open(budget_data_path) as budget_data:


# CSV reader specifies delimiter and variable that holds contents
    budget_data_read = csv.reader(budget_data, delimiter=',')

# Read the header row first (skip this step if there is no header)
    budget_data_header = next(budget_data_read)

# Read initialize counters at 0
    month_counter=0
    total_profit=0
    change = 0
    run_tot_of_change = 0
    h_change=0
    l_change=0
    last_pl_store=0
    avg_change=0

    
    # traverse through rows in CSV file
    for row in budget_data_read:

        #saving first row value
        if month_counter == 0:
            first_pl=int(row[1])

        # storing the change
        change = int(row[1]) - int(last_pl_store)
      
      # keep a running total of the changes
        run_tot_of_change += change

      # how high can the change be?
        if change > h_change:
            h_change = change
            h_date = row[0]
      
      #how low can the change be?
        if change < l_change:
            l_change = change
            l_date = row[0] 

       # count up the rows / months
        month_counter += 1
       
       # keep a running tally of the profits
        total_profit += int(row[1])

       #stores profit or loss
        last_pl_store = row[1] 

        

# calculate avaerage monthly change 
    avg_change = ((run_tot_of_change - first_pl)/ (month_counter - 1))   


 

print(f' it has this many rows:  {month_counter}')
print(f' the total profit:  {total_profit}')
print(f' biggest gain: {h_date} {h_change}')
print(f' biggest loss: {l_date} {l_change}')
print(f' average monthly change:  {avg_change}')


