import os
import sys
from functions import find, organizer

def main():
    folder = sys.argv[1]
    if not folder:
        folder = '/'
    
    #check if folder exists
    folder_path = find(folder)

    #organize the files in the folder
    organizer(folder_path)



if __name__ == "__main__":
    main()