import sys
import os
from main_organize import main_org
from main_search import main_sea

def main():
    if len(sys.argv) < 2:
        print("Error: need at least one argument")
        print("python main.sh <arg>")
        print("                ^^^")
        sys.exit(1)

    elif len(sys.argv) > 3:
        print("Error: more than 2 arguments not supported")
        sys.exit(1)

    argument = sys.argv[1]
    try:
        flag = sys.argv[2]
    except:
        pass

    if flag:
        if flag == "--search":
            main_sea()
            sys.exit(0)
        else:
            print(f"Error: invalid flag {flag}. try with --search")
            sys.exit(1)
    
    try:
        main_org()
        sys.exit(0)
    except Exception as e:
        print(f"Error at main_org: {e}")

if __name__ == "__main__":
    main()