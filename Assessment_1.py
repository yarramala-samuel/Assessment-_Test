#question 1 

import os
print(os.getcwd())

#question 2 

import os

path = "your_path_here"

if os.path.isfile(path):
    print(f"{path} is a file")
elif os.path.isdir(path):
    print(f"{path} is a directory")
else:
    print(f"{path} does not exist")

#question 3
import os

folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")

#question 4 
import os

for file in os.listdir():
    if file.endswith(".txt"):
        print(file)

#question 5
import os
import shutil

reports_dir = "reports"


if not os.path.exists(reports_dir):
    os.mkdir(reports_dir)
    print(f"Directory '{reports_dir}' created.")
else:
    print(f"Directory '{reports_dir}' already exists.")

txt_files = [f for f in os.listdir() if f.endswith(".txt") and os.path.isfile(f)]

for txt_file in txt_files:
    print(f"Moving file: {txt_file}")
    shutil.move(txt_file, os.path.join(reports_dir, txt_file))