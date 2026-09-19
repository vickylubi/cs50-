import sys

#Check if the argv is not equal 2
if len(sys.argv) < 2: 
    sys.exit("Too few command-arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-arguments")

#Check if it is not a python file 
if not sys.argv[1].endswith(".py"):
    sys.exit("Could not read this file")

# Try to open the file 
try:
    with open(sys.argv[1]) as file:
        count = 0
#Go through lines and count
        for line in file:
            if line.strip() == "" or line.strip().startswith("#"):
                continue
            else: 
                count+=1
        print(count)
except FileNotFoundError:
    sys.exit("File does not exist")

