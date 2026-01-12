import os
import sys
from functions import find_path, organizer

def main():
    if len(sys.argv) < 2:
        print("Error: need at least one argument")
        print("python main.sh <folder_name>")
        print("                  ^^^^^^^^^^^")
        sys.exit(1)

    folder = sys.argv[1]
    #check if folder exist
    folder_path = find_path(folder)
    print(folder_path)

    
    if not folder_path:
        print(f"Error: '{folder}' doesn't exists")
        sys.exit(1)

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' isn't a folder")
        sys.exit(1)


    try:
        #organize the files in the folder
        #organizer(folder_path)
        pass
    except Exception as e:
        print(f"error organizer: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()