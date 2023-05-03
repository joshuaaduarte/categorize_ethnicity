import csv

# Open the CSV file and read its contents
with open('ethnicity_val.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Print the header row
    header = next(reader)
    print(header)
