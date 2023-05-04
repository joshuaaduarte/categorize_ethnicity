import os
import shutil
import random

# Set the source and destination folders
source_folder = "C:/Berkeley/spring2023/sdse/categorize_ethnicity/train_raw/White"
destination_folder = "C:/Berkeley/spring2023/sdse/categorize_ethnicity/val_raw/White"

# Set the number of files to transfer
num_files = 2430

# Get a list of all files in the source folder
files = os.listdir(source_folder)

# Shuffle the list of files to randomize which ones are selected
random.shuffle(files)

# Select the first num_files from the shuffled list
selected_files = files[:num_files]

# Move the selected files to the destination folder
for file in selected_files:
    source_path = os.path.join(source_folder, file)
    destination_path = os.path.join(destination_folder, file)
    shutil.move(source_path, destination_path)
