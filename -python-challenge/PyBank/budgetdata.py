import os
import csv
budget_data = os.path.join("budget_data.csv")
Total_months = 0
Total_pl = 0
Value = 0
Change = 0
Dates = []
Profits = []
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    first_row = next(csvreader)
    Total_months += 1
    Total_pl += int(first_row[1])
    Value = int(first_row[1])

    for row in csvreader:
        Dates.append(row[0])
        Change = int(row[1])-Value
        Profits.append(Change) 
        Value = int(row[1])

        Total_months += 1
        Total_pl = Total_pl +int(row[1])

    Greatest_increase = max(Profits)
    Greatest_index = Profits.index(Greatest_increase)    
    Greatest_date = Dates[Greatest_index]

    Greatest_decrease = min(Profits)
    bad_index = Profits.index(Greatest_decrease)
    bad_date = Dates[bad_index]

    avg_change = sum(Profits)/len(Profits)

print("Financial Analysis")
print("----------------------")
print(f"Total Months: {str(Total_months)}")
print(f"Total: ${str(Total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {Greatest_date} (${str(Greatest_increase)})")
print(f"Greatest Decrease in Profits: {bad_date} (${str(Greatest_decrease)})")

output = open("output.txt", "w")
line1 = "Financial Analysis"
line2 = "--------------------------"
line3 = (f"Total months: {str(total_months)}")
line4 = (f"Total: ${str(total_revenue)}")
line5 = (f"Average Change: ${str(round(avg_change,2))}")
line6 = (f"Greatest Increase in Profits: {Greatest_date} (${str(Greatest_increase)})")
line7 = (f"Greatest Decrease in Profits: {loss_date} (${str(Greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))