import csv
import re
import os

data = []

with open('/Users/tom/Downloads/networks (5).csv', 'r', newline='') as csvfile:
    # Create a reader object
    csv_reader = csv.DictReader(csvfile)

    # If your CSV has a header, you can read it separately
    header = csv_reader.fieldnames
    print(f"Header: {header}")

    # Iterate over each row in the CSV
    for row in csv_reader:
        # Each 'row' is a list of strings representing the columns
        print(row)
        # You can access individual elements by index, e.g., row[0], row[1]
        for key, value in zip(header, row):
    #      for key = 'Comment':
    #          if re.match = ("/ VLAN\s\b\d{3,}")
    #          if re.match = ("/ VLAN\s\b).\d{3,4} (\s/\s VRF\s.)"mg
    #           (/ VLAN)\s\d{3,4}

            data.append(row)
       # break
    for row_dict in data:
        print(row_dict)

