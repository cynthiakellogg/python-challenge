import os
import csv

#link to the data
pybank_csv = os.path.join("Resources", "PyBank_data.csv")


#list to store the data
profitList = []
changeList = []
averacgeChange = []
dateList = []


#read the data, but omit the headers in row 1
with open(pybank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

 #Read the header row first
    csv_header = next(csvfile)
    #print(f"Header: {csv_header} ")
    count = 0

 # Read through each row of data after the header
    for row in csv_reader: 
        profitList.append(row[1])
        dateList.append(row[0])
        count+= 1
        if count == 1:
           previous = float(row[1])
        elif count > 1:
           change = float(row[1]) - previous
           changeList.append(change)
           previous = float(row[1])        
    
    total_change = sum(changeList)
    averageChange = (total_change/ (count - 1))
    greatest_increase = max(changeList) 
    greatest_decrease = min(changeList)
    #print it to a summary
    print(f"Summary Title: Financial Analysis")
    print(f"Total Months: {count}")  
    print(f"Average Change: {averageChange}")
    print(f"Greatest Increase In Profits: {greatest_increase}")
    print(f"Greatest Decrease In Profits: {greatest_decrease}") 
    row1 = (f"Total Months: {count}")  
    row2 = (f"Average Change: {averageChange}")
    row3 = (f"Greatest Increase In Profits: {greatest_increase}")
    row4 = (f"Greatest Decrease In Profits: {greatest_decrease}")
    
    output_path = os.path.join("OutputPyBank.txt")
    cleaned_csv = zip([row1, row2, row3, row4])
    #  Open the output file
    with open(output_path, "w") as datafile:
      writer = csv.writer(datafile)

    # Write the header row
      writer.writerow(["Summary Title: Financial Analysis"])

    # Write in zipped rows
      writer.writerows([cleaned_csv])