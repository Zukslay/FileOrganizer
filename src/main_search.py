import os
import sys
from functions_search import search_text

def main_sea():
    if len(sys.argv) < 3:
        print("Error: need one argument and flag")
        print("python main.sh <text> <flag>")
        print("                ^^^^   ^^^^")
        sys.exit(1)
    
    text = sys.argv[1]
    flag = sys.argv[2]

    if not flag.startswith("--"):
        print("Error: flag required")
        print("python main.sh <text> <flag>(all flags starts with '--')")
        print("                       ^^^^")
        sys.exit(1)

    elif type(text) != str:
        print("Error: first argument type is not str")
        print("python main.sh <text> <flag>")
        print("                ^^^^")
        sys.exit(1)
    try:
        list_of_files = search_text(text)
        for file in list_of_files:
            print(file)
        return list_of_files
    except Exception as e:
        print(f"error search: {e}")
        sys.exit(1)

