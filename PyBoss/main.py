import csv
import operator

# a dictionary that will be invaluable for determining state two-letter abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

empcsv = ("employee_data.csv")
#  NOTE: instructions referred to a "employee_data1.csv" and "employee_data2.csv"
#  but all I found in the homework directory was the above
outputcsv = ("new_empoyee_data.csv")
outcsv = open(outputcsv,"w",newline="")

csvwriter = csv.writer(outcsv,delimiter=',')


with open(empcsv, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)  # discard input headers
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])     # ... and write out new headers
    
    # cycle through the rest of the records
    for row in csvreader:
        nameparts = str.split(row[1],sep=" ")       # split the given name into first and last parts
        
        dateparts = str.split(row[2],sep="-")       # split the DOB into YYYY, MM, DD
        newdate   = (dateparts[1] + "/" + dateparts[2] + "/" + dateparts[0])    # recombine them in new order

        ssnparts  = str.split(row[3],sep="-")       # split the ssn into parts
        newssn    = ("***-**-" + ssnparts[2])       # the new file will show only the last four digits

        stateabbr = us_state_abbrev[row[4]]         # finally, replace the state name with its abbreviation

        csvwriter.writerow([row[0],nameparts[0],nameparts[1],newdate,newssn,stateabbr])     

outcsv.close()
                                                                    







