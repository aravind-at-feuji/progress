import csv
with open('employees.csv', newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   for row in csvreader:
       print(row)