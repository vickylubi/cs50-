import sys
import csv
from tabulate import tabulate


#Expects exactly one command-line argument — the path to a CSV file (columns like Sicilian Pizza,Small,Large with rows of prices).

#Validates that input:
#If there isn't exactly one argument → exit via sys.exit
if len(sys.argv) < 2: 
    sys.exit("Too few command-arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-arguments")
#If the filename doesn't end in .csv → exit via sys.exit
if not sys.argv[1].endswith(".csv"):
    sys.exit("Could not read this file")
#If the file doesn't exist → exit via sys.exit
#Reads the CSV file and extracts its rows (header row + pizza rows).
try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        rows=[]
        for row in reader: 
            rows.append(row)
    #Prints those rows as an ASCII table 
        print(tabulate(rows, headers="firstrow", tablefmt="grid"))
        
except FileNotFoundError:
    sys.exit("File does not exsist")

