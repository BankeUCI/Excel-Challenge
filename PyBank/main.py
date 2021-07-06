import os
import csv
#  set path for file
budget_csv= os.path.join("Resources", "budget_data.csv")

# Lists to store data
total_months=[]
total_profit_losses=[]          
monthly_profit_losses_change=[]
# Greatest_increase_profits=[]
# Greatest_decrease_losses=[] 

#  Open csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        # Append the total months and total profit to lists
        total_months.append(row[0])
        total_profit_losses.append(int(row[1]))

for i in range(len(total_profit_losses)-1):
    
# append monthly profit/loss change to monthly change in profit
    monthly_profit_losses_change.append(total_profit_losses[i+1]-total_profit_losses[i])

# To get max and min change in monthly profit/loss
max_increase_value = max(monthly_profit_losses_change)
max_decrease_value = min(monthly_profit_losses_change)

max_increase_month = monthly_profit_losses_change.index(max(monthly_profit_losses_change))+1
max_decrease_month = monthly_profit_losses_change.index(min(monthly_profit_losses_change))+1

print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {len(total_months)}")
print((f"Total: ${sum(total_profit_losses)}"))
print((f"Average Change: {round(sum(monthly_profit_losses_change)/len(monthly_profit_losses_change),2)}"))
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Losses:  {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Set variable for output file
output_file=os.path.join("Analysis")

#  Open output file to write Analysis in a file that contains results for Financial Analysis
with open(output_file, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("---------------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit_losses)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_losses_change)/len(monthly_profit_losses_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Losses:  {total_months[max_decrease_month]} (${(str(max_decrease_value))})")



