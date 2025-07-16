import os, time, datetime, sys

from moduls.system import osCleanerHandler

# global variable
osType = os.name
folderData = "Datas"
fileData = "data.txt"
fullDataPath = os.path.join(folderData, fileData)

# main function
def addingSymbol():
    while True:
        osCleanerHandler()
        print("You enter symbol adder program")
        print("Choose symbol !")
        print('1. "Example data"')
        print("2. 'Example data'")
        print("3. [Example data]")
        print("4. {Example data}")
        print("5. Example data,")
        print("Enter any input except menu above For exit the program !")
        userChoose = input("Choose: ").strip()
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
            break

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

def summation():
    while True:
        osCleanerHandler()
        print("You enter Summation program !\n")
        print("Choose Summation !")
        print("1. Calculate Age")
        print("Enter any input except menu above For exit the program !")
        userInput = input("-> ").strip()
        if userInput == "1":
            calcAge()
        else:
            print("You exit the program !")
            break


def calcAge():
    osCleanerHandler()
    print("You enter Calculate Age program !\n")
    now = datetime.datetime.now()
    yearsNow = now.year
    yearsInput = int(input("Enter the year of birth: "))
    age = yearsNow - yearsInput
    ageStr = str(age)
    print(f"Current age: {ageStr}")
    print("\nEnter Y/y to exit program, or enter any input to back the program.")
    userInput = input("Input: ").lower()
    if userInput == "y":
        print("\nYou will be back to the Summation menu !")
        time.sleep(1.8)
        summation()
    else:
        print("\nInvalid input !")
        print("You will return to Calculate Age !")
        time.sleep(1.8)
        osCleanerHandler()
        calcAge()

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
    
# call main program
# if __name__=="__main__":
#     addingSymbol()


