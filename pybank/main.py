import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

date_count = 0
total_profit_loss = 0
total_profit_loss_change = 0
previous_profit_loss = 867884
average_profit_loss_change = 0
profit_loss_change_list = []
profit_loss_date_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        date_count = date_count + 1
        total_profit_loss = float(row[1]) + total_profit_loss
        profit_loss_change = float(row[1]) - previous_profit_loss
        previous_profit_loss = float(row[1])
        date_change = row[0]
        profit_loss_change_list.append(profit_loss_change)
        profit_loss_date_list.append(date_change)
        total_profit_loss_change = sum(profit_loss_change_list)

        min_profit_loss = min(profit_loss_change_list)
        max_profit_loss = max(profit_loss_change_list)
        min_date = profit_loss_date_list[profit_loss_change_list.index(min_profit_loss)]
        max_date = profit_loss_date_list[profit_loss_change_list.index(max_profit_loss)]
        
average_profit_loss_change = round(total_profit_loss_change / (date_count - 1), 2)

print ("Financial Analysis")
print ("----------------------------------")
print ("Total Months:" + " " + str(date_count))
print ("Total:" " " + "$"+ str(int(total_profit_loss)))
print ("Average Change:" + " " + "$"+ str(average_profit_loss_change))
print ("Greatest Increase in Profits:" + " " + str(max_date) + " " + "$" + str(int(max_profit_loss)))
print ("Greatest Decrease in Profits:" + " " + str(min_date) + " " + "$" + str(int(min_profit_loss)))
    
output_file = os.path.join('Analysis', 'budget_data.txt')

writer= open(output_file, "w") 

writer.write("Financial Analysis\n")
writer.write("----------------------------------\n")
writer.write(f"Total Months: {date_count}\n")
writer.write(f"Total: ${int(total_profit_loss)}\n")
writer.write(f"Average Change: ${average_profit_loss_change}\n")
writer.write(f"Greatest Increase in Profits: {max_date} (${int(max_profit_loss)})\n")
writer.write(f"Greatest Decrease in Profits: {min_date} (${int(min_profit_loss)})\n")
    



