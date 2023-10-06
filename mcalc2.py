import math

# docs are in your favorite orange notebook :]
# dw i made sure to include readability linebreaks
# 
# Operations list is below functions
#
# TO-DO: 
# learn how to use github properly
# ~~make github page for this so i can access on laptop also~~
# make digital version of docs
# add more operations
# after all operations are added, add gui??? maybe???

def welcomeMessage():
    print("Hi, welcome to MCalc 2.0. A completely rewritten version of my first 'real' python project.")
    print("Current operations:")
    for x in range(0,len(operationsList)):
        print("    " + operationsList[x] + "\n ==============================")
    operation = input("Please input the operation of your choice, worded as is in the list. \n")
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
        
def resultFunc(x):
    print("\n ==============================")
    print(x)

def additionPart(x):
    summand = float(x)
    return summand

def subtractionPart(x):
    subPart = float(x)
    return subPart

def multiplicationPart(x):
    multiPart = float(x)
    return multiPart

def divisionPart(x):
    divPart = float(x)
    return divPart

def absoluteValuePart(x):
    absPart = float(x)
    return absPart

def powerPart(x):
    powPart = float(x)
    return powPart

def powerPart2(x):
    powPart2 = float(x)
    return powPart2

# display welcome message and init operationPick func =====================
operationsList = ["Add", "Subtract", "Multiply", "Divide", "Absolute-Value", "Exponents"]
operation = welcomeMessage()
operationPick()
selectedOperation = operationPick()

#addition =====================
if selectedOperation == 0:
    summandTotal = int(input("\nHow many values are there in the problem?\n"))
    summandList = []
    result = 0
    for x in range(0,summandTotal):
        summand = additionPart(input("\nPlease input a number.\n"))
        summandList.append(summand)
    for y in summandList:
        result = result + y
    resultFunc(result)

# subtraction =====================
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
    resultFunc(result)


# multiplication =====================
elif selectedOperation == 2:
    multiPartTotal = int(input("\nHow many values are there in the problem?\n"))
    multiPartList = []
    result = 1
    for x in range(0,multiPartTotal):
        multiPart = multiplicationPart(input("\nPlease input a number.\n"))
        multiPartList.append(multiPart)
    for y in multiPartList:
        result = result * y
    resultFunc(result)


# division =====================
elif selectedOperation == 3:
    divPartTotal = int(input("\nHow many values are there in the problem?\n"))
    divPartList = []
    divPart = divisionPart(input("\nPlease input the first number to be divided from.\n"))
    result = divPart
    for x in range(0,(divPartTotal - 1)):
        divPart = divisionPart(input("\nPlease input the next number to divide from the last number.\n"))
        divPartList.append(divPart)
    for y in divPartList:
        result = result / y
    resultFunc(result)


# absolute value =====================
elif selectedOperation == 4:
    absPartTotal = int(input("\nHow many values are there?\n"))
    absPartList = []
    for x in range(0, absPartTotal):
        absPart = absoluteValuePart(input("\nEnter a value.\n"))
        absPartList.append(absPart)
    for y in absPartList:
        result = abs(y)
        resultFunc(result)

# exponents =====================
elif selectedOperation == 5:
    powPartTotal = int(input("\nHow many values are there?\n"))
    powPartList = []
    powPartList2 = []
    for x in range(0, powPartTotal):
        powPart = powerPart(input("\nEnter a value.\n"))
        powPart2 = powerPart2(input("\nEnter what exponent it has.\n"))
        powPartList.append(powPart)
        powPartList2.append(powPart2)
    for y in range(0,len(powPartList)):
        result = powPartList[y] ** powPartList2[y]
        resultFunc(result)