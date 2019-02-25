import csv
import os
import operator

pollcsv = os.path.join("../Resources", "election_data.csv")

# initialize our tracking/reporting variables
totvotes = 0
candidateList = []
votesList = []


with open(pollcsv, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # skip the headers
    
    # cycle through the rest of the records
    for row in csvreader:
        totvotes += 1

        try:
            listIndex = candidateList.index(row[2])
        except Exception as firstvote:                  # a candidate is only in the list after he has his first vote
            candidateList.append(row[2])
            votesList.append(0)
            listIndex = candidateList.index(row[2])     # having just added it to the list, we should have no trouble finding it

        votesList[listIndex] += 1

# format and write the summary report, both to the terminal and a text file

outfile = 'output.txt'
ofile = open(outfile,"w")

dashline = ("----------------------------------")
outputline = ("Election Results")
print (outputline)
ofile.write (outputline + "\n")    # need a newline character for file writes
    
print (dashline)
ofile.write (dashline + "\n") 
     
outputline = ("Total Votes:   "  + str(totvotes))
print (outputline)
ofile.write (outputline + "\n")  
    
print (dashline)
ofile.write (dashline + "\n") 

topvotegetter = ""
topvotes = 0
numberCandidates = len(candidateList)
for x in range(numberCandidates):
    name = candidateList[x] + ":"
    votePct = 100 * votesList[x] / totvotes
    outputline = ('{0: <16}'.format(name) + '{:6.3f}'.format(votePct) + "%   (" + str(votesList[x]) + ")")
    print (outputline)
    ofile.write (outputline + "\n")  
    if votesList[x] > topvotes:
        topvotes = votesList[x]
        topvotegetter = candidateList[x]
    
print (dashline)
ofile.write (dashline + "\n") 

outputline = ("Winner:  " + topvotegetter)
print (outputline)
ofile.write (outputline + "\n")  

print (dashline)
ofile.write (dashline + "\n") 







