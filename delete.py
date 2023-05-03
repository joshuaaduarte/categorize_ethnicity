
import os
import random

# Define the directory containing the folders to clean up
directory_path = "C:/Berkeley/spring2023/sdse/proj/train"

# Define the desired number of files to keep in each folder
desired_num_files = 1000

# Iterate over each folder in the directory
for folder_name in os.listdir(directory_path):
    # Determine the full path to the current folder
    folder_path = os.path.join(directory_path, folder_name)

    # If the current item in the directory is a folder, and not a file, continue with the cleanup
    if os.path.isdir(folder_path):
        # Get a list of all the files in the current folder
        file_list = os.listdir(folder_path)

        # Determine the number of files to delete from the folder
        num_files_to_delete = len(file_list) - desired_num_files

        # If there are more files than desired, randomly select and delete files
        if num_files_to_delete > 0:
            files_to_delete = random.sample(file_list, num_files_to_delete)
            for file_name in files_to_delete:
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)