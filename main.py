# manage system
from moduls.system import osCleanerHandler
from moduls.system import checkPython
from moduls.system import timeForUser
from moduls.system import exitProgram

# manage program
from moduls.program import addingSymbol
from moduls.program import summation

PROGRAM_VERSION = "1.0.0"

def mainMenu():
    while True:
        osCleanerHandler()
        timeForUser()
        print(f"PLBA - Version: {PROGRAM_VERSION}\n")
        print("What do you want ?")
        print("1. Symbol Adder")
        print("2. Summation")
        print("0. Exit")
        userInput = input("-> ").strip()
        if userInput == "1":
            addingSymbol()
        elif userInput == "2":
            summation()
        elif userInput == "0":
            exitProgram()
        else:
            print("Invalid input !")

if __name__=="__main__":
    checkPython()
    mainMenu()