"""
Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, 
and the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. 
Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
"""

import sys
import csv

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit(f"Could not read {sys.argv[1]}")

try:
    with open(sys.argv[1],"r") as before, open(sys.argv[2],"w",newline="") as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(",")
            writer.writerow({"first":first.strip(), "last":last.strip(), "house":row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
