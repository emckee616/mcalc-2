import math

# docs are in your favorite orange notebook :]
# dw i made sure to include readability linebreaks
# 
# TO-DO: 
# learn how to use github properly
# make github page for this so i can access on laptop also
# make digital version of docs
# add more operations
# after all operations are added, add gui??? maybe???

def welcomeMessage():
    print("Hi, welcome to MCalc 2.0. A completely rewritten version of my first 'real' python project.")
    print("Current operations:")
    for x in range(0,len(operationsList)):
        print("    " + operationsList[x] + "\n ===============")
    operation = input("Please input the operation of your choice, worded as is in the list, with no space before/afterwards \n")
    if operation.islower() == False:
        operation = operation.lower()
    elif operation.isalpha() == False:
        print("Hey! That's not a valid input!")
    return operation

def operationPick():
    for x in range(0, len(operationsList)):
        if operation == str(operationsList[x]).lower():
            selectedOperation = int(x)
            return selectedOperation

def additionPart(x):
    summand = float(x)
    return summand

def subtractionPart(x):
    subPart = float(x)
    return subPart

def multiplicationPart(x):
    multiPart = float(x)
    return multiPart

# display welcome message and init operationPick func
operationsList = ["Add", "Subtract", "Multiply", "Divide"]
operation = welcomeMessage()
operationPick()
selectedOperation = operationPick()

#addition
if selectedOperation == 0:
    summandTotal = int(input("\nHow many values are there in the problem?\n"))
    summandList = []
    result = 0
    for x in range(0,summandTotal):
        summand = additionPart(input("\nPlease input a number.\n"))
        summandList.append(summand)
    for y in summandList:
        result = result + y
    print("\n")
    print(result)

# subtraction
elif selectedOperation == 1:
    subPartTotal = int(input("\nHow many values are there in the problem?\n"))
    subPartList = []
    subPart = subtractionPart(input("\nPlease input the first number to be subtracted from.\n"))
    result = subPart
    for x in range(0,(subPartTotal - 1)):
        subPart = subtractionPart(input("\nPlease input the next number to be subtracted from the last / have the next subtract from it.\n"))
        subPartList.append(subPart)
    for y in subPartList:
        result = result - y
    print("\n")
    print(result)

# multiplication
elif selectedOperation == 2:
    multiPartTotal = int(input("\nHow many values are there in the problem?\n"))
    multiPartList = []
    result = 1
    for x in range(0,multiPartTotal):
        multiPart = multiplicationPart(input("\nPlease input a number.\n"))
        multiPartList.append(multiPart)
    for y in multiPartList:
        result = result * y
    print("\n")
    print(result)

# division