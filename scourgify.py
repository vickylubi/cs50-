import sys
import csv

#Check if the argv is not equal 3
if len(sys.argv) < 3: 
    sys.exit("Too few command-arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-arguments")

#Check if it is not a csv file 
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Could not read this file")

# Try to open the file before to read
try:
    with open(sys.argv[1], "r") as before, open(sys.argv[2], "w") as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames = ["first", "last", "house"] )
        writer.writeheader()
        for row in reader:
            writer.writerow(
                {
                    "first": row["name"].split(",")[1].strip(),
                    "last": row["name"].split(",")[0],
                    "house": row["house"]
                }
            )
        
     
#Create after file to write 
except FileNotFoundError:
    sys.exit("File does not exist")
