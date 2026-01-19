import os
import sys
from functions_organize import find_path, organizer

def main_org():
    

    folder = sys.argv[1]
    #check if folder exist
    folder_path = find_path(folder)

    if not folder_path:
        print(f"Error: '{folder}/{folder_path}' doesn't exists")
        sys.exit(1)

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' isn't a folder")
        sys.exit(1)


    try:
        #organize the files in the folder
        organizer(folder_path)
    except Exception as e:
        print(f"error organizer: {e}")
        sys.exit(1)

