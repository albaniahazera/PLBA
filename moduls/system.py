import time, os, sys, datetime


MIN_PYTHON_VERSION = (3, 12, 3)
osType = os.name

def checkPython():
    if sys.version_info < MIN_PYTHON_VERSION:
        print(f"Error: This program requires Python {MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]} or newer.")
        print(f"You are currently using Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        print("Please upgrade your Python version to run this program.")
        sys.exit(1)

def exitProgram():
    while True:
        osCleanerHandler()
        userInput = input("Are you sure to exit ? (Y/n)").lower().strip()
        if userInput == "y":
            print("Exit program !\n")
            time.sleep(1)
            sys.exit()
        elif userInput == "n":
            print("\nReturn to main program")
            break
        else:
            print("\nInvalid Input !")
            return exitProgram()

def osCleanerHandler():
    print("\nTerminal will be clear by program !")
    time.sleep(1)
    if osType == "nt":
        os.system("cls")
    elif osType == "posix":
        os.system("clear")
    else:
        print("Cannot execute terminal clear program, unknown OS type !")

def timeForUser():
    rawTime = datetime.datetime.now()
    hours = rawTime.strftime("Hours: %H:%M")
    print(hours)
    date = rawTime.strftime("Day: %D")
    print(date) 
    intHours = rawTime.hour
    if intHours >= 18:
        print("Good evening\n")
    elif intHours >= 12: 
        print("Good afternoon\n")
    else:
        print("Good morning\n")

# if __name__=="__main__":
#     osCleanerHandler()