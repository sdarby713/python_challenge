import csv

bankcsv = "budget_data.csv"

# initialize our tracking/reporting variables
# gincramt should initially be set lower than any expected monthly amount we might find
# likewise gdecramt should initially be set higher than any monthly amnount
totmonths = 0
totprofit = 0
gincrmo = ""
gincramt = -9999999
gdecrmo = ""
gdecramt = 9999999

with open(bankcsv, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # skip the headers
    
    # cycle through the rest of the records
    for row in csvreader:
        totmonths += 1

        monthamt = int(row[1])
        totprofit += monthamt

        if monthamt > gincramt:
            gincrmo = row[0]
            gincramt = monthamt

        if monthamt < gdecramt:
            gdecrmo = row[0]
            gdecramt = monthamt

# format and write the summary report, both to the terminal and a text file

outfile = 'output.txt'
ofile = open(outfile,"w")

outputline = ("Financial Analysis")
print (outputline)
ofile.write(outputline + "\n")   # need a newline character for file writes
    
outputline = ("----------------------------------")
print (outputline)
ofile.write(outputline + "\n")   
    
outputline = ("Total Months:   "  + str(totmonths))
print (outputline)
ofile.write(outputline + "\n")   

outputline = ("Total:          $" + str(totprofit))  
print (outputline)
ofile.write(outputline + "\n")  
    
outputline = ("Average Change: $" + '{:04.2f}'.format(totprofit/totmonths))
print (outputline)
ofile.write(outputline + "\n")   
    
outputline = ("Greatest Increase in Profits:  "  + gincrmo + "  ($" + str(gincramt) + ")")
print (outputline)
ofile.write(outputline + "\n")   
    
outputline = ("Greatest Decrease in Profits:  "  + gdecrmo + "  ($" + str(gdecramt) + ")")
print (outputline)
ofile.write(outputline + "\n")   

ofile.close()







