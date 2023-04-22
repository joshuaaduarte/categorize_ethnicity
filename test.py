import csv

# Open the CSV file and read its contents
with open('ethnicity.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    # Print the header row
    header = next(reader)
    print(header)
