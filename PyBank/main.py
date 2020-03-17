import os
import csv

#link to the data
PyBank_csv_path = os.path.join("..", "Resources", "PyBank_data.csv")

#read the data, but omit the headers in row 1
with open("PyBank_csv_path") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

 # Read through each row of data after the header
    for row in csv_reader:

    # Convert row to float and compare to grams of fiber
        if float(row[1]) >= 0:
            print(row)

#that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
    #define what a month is
    #count the total number of months
    #print it to a summary
    # then we need to define what a profit is
    # what a loss is
    # then perform calculations
    # and print out:     
#       The net total amount of "Profit/Losses" over the entire period
#       The average of the changes in "Profit/Losses" over the entire period
#       The greatest increase in profits (date and amount) over the entire period
#       The greatest decrease in losses (date and amount) over the entire period
# your final script should both print the analysis to the terminal 
# and export a text file with the results.
#should look like this: 
#Summary Title: Financial Analysis
  
  #----------------------------
  #Total Months: 86
  #Total: $38382578
 # Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)