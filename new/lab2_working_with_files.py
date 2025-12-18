# 1) Open a file for writing

import os


file = open("test.txt", "w")
file.write("This is a test file for cybersecurity lab.\n")
file.write("Python makes file handling easy.\n")
file.close()
print("test.txt written successfully.")

# 2) Open a file for reading

file = open("test.txt", "r")
content = file.read()
print("\n--- File content ---")
print(content)
file.close()

# 3) Display the current directory

current_directory = os.getcwd()
print("--- Current directory ---")
print(current_directory)
 
# 4) Create a new folder

folder_name = "lab_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created:", folder_name)
else:
    print("Folder already exists:", folder_name)

# 5) List all files and folders

print("\n--- Items in current directory ---")
items = os.listdir()
print(items)
 
# 6) Check object types

print("\n--- Type check ---")
for item in os.listdir():
    if os.path.isfile(item):
        print(item, "- File")
    elif os.path.isdir(item):
        print(item, "- Folder")

# 7) Delete a file if it exists

if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("\nFile deleted: test.txt")
else:
    print("\nFile does not exist: test.txt")