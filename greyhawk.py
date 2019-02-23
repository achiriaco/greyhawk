Input_Month = "Readying"
Input_Day = "5"

print ("The Month is " + Input_Month)
print ("The Day is " + Input_Day) 

import csv

with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)