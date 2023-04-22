import os
import csv

# Open the CSV file and read its contents
with open('ethnicity_val.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Create a dictionary to hold the names of the folders we'll create
    folders = {}

    # Loop through each row in the CSV file
    for row in reader:
        # Extract the race value from the row
        race = row['race']

        # If we haven't already created a folder for this race, create one
        if race not in folders:
            folders[race] = os.makedirs(race)

        # Move the file into the appropriate folder
        filename = row['file']
        if not os.path.isfile(filename):
            print(f"Error: file '{filename}' does not exist.")
        else:
            try:
                os.rename(filename, os.path.join(race, os.path.basename(filename)))
            except Exception as e:
                print(f"Error moving file '{filename}': {str(e)}")
