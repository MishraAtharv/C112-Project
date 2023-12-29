import os
import shutil

# Define source and destination directories
from_dir = "C:/Users/infos/OneDrive/Documents/Documents"
to_dir = "C:/Users/infos/Downloads"

# Modify path separators for compatibility with Visual Studio Code
from_dir = from_dir.replace("\\", "/")
to_dir = to_dir.replace("\\", "/")

# Get a list of files in the source directory
list_of_files = os.listdir(from_dir)

# Print the list of files
print("List of files in the source directory:")
for file_name in list_of_files:
    print(file_name)

# Iterate through the list of files
for file_name in list_of_files:
    # Use os.path.splitext() to capture the name and extension of each file
    name, extension = os.path.splitext(file_name)

    # Check if the extension is blank, continue to the next file
    if not extension:
        continue

    # Check if the extension is in the list of allowed extensions
    allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']
    if extension in allowed_extensions:
        # Create directory paths
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + extension[1:].upper()  # Create a folder with uppercase extension
        path3 = to_dir + '/' + extension[1:].upper() + '/' + file_name

        # Check if the folder/directory path exists before moving
        if os.path.exists(path2):
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)
        else:
            # Make a new folder/directory
            os.makedirs(path2)
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)

print("Files moved successfully!")
