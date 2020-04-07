#Your task is to create a Python script that analyzes the records to calculate each of the following
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

# import dependencies
import csv
import os

# file to load
## create a file path to the source csv
pybank_csv = os.path.join("Resources", "PyBank_data.csv")

# create variables to store financial analysis
## total number of months --> number
total_month_count = 0
## net change --> list
profit_list = []
## greatest increase --> list
greatest_inc = ["", 0]
## greatest decrease  --> list
greatest_dec = ["", 9999999999999]
## total net -- > number
total_net = 0.0

# read the csv and covnert it into a list of dictionaries
    ## csv.reader(file name variable)
with open(pybank_csv) as puppies:
    csv_reader = csv.reader(puppies, delimiter=",")

    ## skip the header row
    csv_header = next(csv_reader)

    print(f"Header: {csv_header} ")
    ## extract the first row as starting point to make comparisons

    # local scoped variable
    first_row = next(csv_reader)
    prev_net = int(first_row[1])

    # global scope variables
    total_month_count += 1
    total_net += int(first_row[1])

    ## loop through the file and do some maths
    for row in csv_reader:
        ## track the total
        total_month_count += 1
        total_net += int(row[1])

        ## track net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        profit_list.append(net_change)
        

        # Calculate the greatest increase
        if net_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = net_change

# calculate averate net change
avg_change = sum(profit_list) / len(profit_list)

# generate the output summary
row1 = (f"Total Months: {total_month_count}")  
row2 = (f"Average Change: {avg_change}")
row3 = (f"Greatest Increase In Profits: {greatest_inc}")
row4 = (f"Greatest Decrease In Profits: {greatest_dec}")

# print to terminal
print(f"Summary Title: Financial Analysis")
print(f"-----------------")
print(row1)  
print(row2)
print(row3)
print(row4)

# file to export
## create a file path to output csv
output_path = os.path.join("OutputPyBank.txt")
# export the output file
cleaned_csv = zip([row1, row2, row3, row4])
with open(output_path, "w") as datafile:
  # datafile.write(cleaned_csv)
  writer = csv.writer(datafile)
  # Write the header row
  writer.writerow(["Summary Title: Financial Analysis"])
  # Write in zipped rows
  writer.writerows([cleaned_csv])