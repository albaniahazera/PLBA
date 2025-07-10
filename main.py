import os, time, datetime, sys

# global variable
osType = os.name
folderData = "Datas"
fileData = "data.txt"
fullDataPath = os.path.join(folderData, fileData)

PROGRAM_VERSION = "1.0.0"
MIN_PYTHON_VERSION = (3, 13, 1)

# check python version function
def checkPython():
    if sys.version_info < MIN_PYTHON_VERSION:
        print(f"Error: This program requires Python {MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]} or newer.")
        print(f"You are currently using Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        print("Please upgrade your Python version to run this program.")
        sys.exit(1)

# main function
def addingSymbol():
    osCleanerHandler()
    timeForUser()
    print(f"Symbol Adder Program - Version: {PROGRAM_VERSION}\n")
    print("Choose symbol !")
    print('1. "Example data"')
    print("2. 'Example data'")
    print("3. [Example data]")
    print("4. {Example data}")
    print("5. Example data,")
    print("Enter any input except menu above For exit the program !")
    userChoose = input("Choose: ")
    if userChoose == "1":
        emptyDoubleQuotes()
    elif userChoose == "2":
        emptySingleQuotes()
    elif userChoose == "3":
        squareBrackets()
    elif userChoose == "4":
        curlyBrackets()
    elif userChoose == "5":
        coma()
    else:
        print("You exit the program !")
        exit

# adding double quotes function 
def emptyDoubleQuotes():
    print('You choose: ""')
    print("Enter data !")
    stringInput = input("Data: ")
    finalInput = (f'"{stringInput}"')
    print(f"Result: {finalInput}")
    print(f"Wanna save result to {fileData} y/n ?")
    userSave = input("Input: ").lower()
    if userSave == "y":
        saveData(finalInput)
        emptyDoubleQuotes()
    else:
        print("\nEnter Y/y to exit program, or enter any input to back the program.")
        userInput = input("Input: ").lower()
        if userInput == "y":
            print("\nYou will be back to the first program !")
            time.sleep(1.8)
            addingSymbol()
        else:
            print("\nInvalid input !")
            print("You will return to enter data set to double quotes")
            time.sleep(1.8)
            osCleanerHandler()
            emptyDoubleQuotes()

# adding single quotes function 
def emptySingleQuotes():
    print("You choose: ''")
    print("Enter data !")
    stringInput = input("Data: ")
    finalInput = (f"'{stringInput}'")
    print(f"Result: {finalInput}")
    print(f"Wanna save result to {fileData} y/n ?")
    userSave = input("Input: ").lower()
    if userSave == "y":
        saveData(finalInput)
        emptySingleQuotes()
    else:
        print("\nEnter Y/y to exit program, or enter any input to back the program.")
        userInput = input("Input: ").lower()
        if userInput == "y":
            print("\nYou will be back to the first program !")
            time.sleep(1.8)
            addingSymbol()
        else:
            print("\nInvalid input !")
            print("You will return to enter data set to single quotes")
            time.sleep(1.8)
            osCleanerHandler()
            emptySingleQuotes()
    
# adding curly brackets function 
def curlyBrackets():
    print("You choose: {}")
    print("Enter data !")
    stringInput = input("Data: ")
    finalInput = (f"{{{stringInput}}}")
    print(f"Result: {finalInput}")
    print(f"Wanna save result to {fileData} y/n ?")
    userSave = input("Input: ").lower()
    if userSave == "y":
        saveData(finalInput)
        curlyBrackets()
    else:
        print("\nEnter Y/y to exit program, or enter any input to back the program.")
        userInput = input("Input: ").lower()
        if userInput == "y":
            print("\nYou will be back to the first program !")
            time.sleep(1.8)
            addingSymbol()
        else:
            print("\nInvalid input !")
            print("You will return to enter data set to curly brackets")
            time.sleep(1.8)
            osCleanerHandler()
            curlyBrackets()

# adding square brackets function 
def squareBrackets():
    print("You choose: []")
    print("Enter data !")
    stringInput = input("Data: ")
    finalInput = (f"[{stringInput}]")
    print(f"Result: {finalInput}")
    print(f"Wanna save result to {fileData} y/n ?")
    userSave = input("Input: ").lower()
    if userSave == "y":
        saveData(finalInput)
        squareBrackets()
    else:
        print("\nEnter Y/y to exit program, or enter any input to back the program.")
        userInput = input("Input: ").lower()
        if userInput == "y":
            print("\nYou will be back to the first program !")
            time.sleep(1.8)
            addingSymbol()
        else:
            print("\nInvalid input !")
            print("You will return to enter data set to square brackets")
            time.sleep(1.8)
            osCleanerHandler()
            squareBrackets()
    
# adding coma function 
def coma():
    print("You choose: ,")
    print("Enter data !")
    stringInput = input("Data: ")
    finalInput = (f"{stringInput},")
    print(f"Result: {finalInput}")
    print(f"Wanna save result to {fileData} y/n ?")
    userSave = input("Input: ").lower()
    if userSave == "y":
        saveData(finalInput)
        coma()
    else:
        print("\nEnter Y/y to exit program, or enter any input to back the program.")
        userInput = input("Input: ").lower()
        if userInput == "y":
            print("\nYou will be back to the first program !")
            time.sleep(1.8)
            addingSymbol()
        else:
            print("\nInvalid input !")
            print("You will return to enter data set to coma")
            time.sleep(1.8)
            osCleanerHandler()
            coma()

# save data to file.txt
def saveData(dataToSave):
    try:
        os.makedirs(folderData, exist_ok="True")
        print(f"Checking folder {folderData}...")
        time.sleep(1.8)
        with open(fullDataPath, 'a') as file:
            file.write(dataToSave + '\n')
        print(f"\nResult succesfully save at {fullDataPath}")
    except IOError:
        print(f"\nError: data failed when save to {fullDataPath}")
    except Exception as e:
        print(f"\nError message: {e}")
    time.sleep(1.8)
    
# say time function
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

# terminal cleaner for windows and linux distro 
def osCleanerHandler():
    print("\nTerminal will be clear by system !")
    time.sleep(1.8)
    if osType == "nt":
        os.system("cls")
    elif osType == "posix":
        os.system("clear")
    else:
        print("Cannot execute terminal clear program, unknown OS type !")

# call main program
if __name__=="__main__":
    checkPython()
    addingSymbol()


