import math
import time

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
    return operation

def operationPick():
    for x in range(0, len(operationsList)):
        if operation == str(operationsList[x]).lower():
            selectedOperation = int(x)
            return selectedOperation
        else:
            print("Not a valid operation!")
            time.sleep(2)
            welcomeMessage()

def shapePick():
    for x in range(0,len(shapesList)):
        print("    " + shapesList[x] + "\n ==============================")
    shape = input("\nWhat shape do you want the area of?\n")
    if shape.islower() == False:
        shape = shape.lower()
    for x in range(0, len(shapesList)):
        if shape == str(shapesList[x]).lower():
            selectedShape = int(x)
            return selectedShape
        else:
            print("Not a valid shape!")
            time.sleep(2)
            shapePick()

def resultFunc(x):
    print("\n ==============================")
    print(x)

def equationPart(x):
    equationPart = float(x)
    return equationPart

def equationPart2(x):
    equationPart2 = float(x)
    return equationPart2

# display welcome message and init operationPick func =====================
operationsList = ["Add", "Subtract", "Multiply", "Divide", "Absolute-Value", "Exponents", "Roots", "Area"]
shapesList = ["Square", "Rectangle", "Circle", "Triangle", "Trapezoid"]
operation = welcomeMessage()
selectedOperation = operationPick()

# addition =====================
if selectedOperation == 0:
    summandTotal = int(input("\nHow many values are there in the problem?\n"))
    summandList = []
    result = 0
    for x in range(0,summandTotal):
        summand = equationPart(input("\nPlease input a number.\n"))
        summandList.append(summand)
    for y in summandList:
        result = result + y
    resultFunc(result)

# subtraction =====================
elif selectedOperation == 1:
    subPartTotal = int(input("\nHow many values are there in the problem?\n"))
    subPartList = []
    subPart = equationPart(input("\nPlease input the first number to be subtracted from.\n"))
    result = subPart
    for x in range(0,(subPartTotal - 1)):
        subPart = equationPart(input("\nPlease input the next number to be subtracted from the last / have the next subtract from it.\n"))
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
        multiPart = equationPart(input("\nPlease input a number.\n"))
        multiPartList.append(multiPart)
    for y in multiPartList:
        result = result * y
    resultFunc(result)


# division =====================
elif selectedOperation == 3:
    divPartTotal = int(input("\nHow many values are there in the problem?\n"))
    divPartList = []
    divPart = equationPart(input("\nPlease input the first number to be divided from.\n"))
    result = divPart
    for x in range(0,(divPartTotal - 1)):
        divPart = equationPart(input("\nPlease input the next number to divide from the last number.\n"))
        divPartList.append(divPart)
    for y in divPartList:
        result = result / y
    resultFunc(result)


# absolute value =====================
elif selectedOperation == 4:
    absPartTotal = int(input("\nHow many values are there?\n"))
    absPartList = []
    for x in range(0, absPartTotal):
        absPart = equationPart(input("\nEnter a value.\n"))
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
        powPart = equationPart(input("\nEnter a value.\n"))
        powPart2 = equationPart2(input("\nEnter what exponent it has.\n"))
        powPartList.append(powPart)
        powPartList2.append(powPart2)
    for y in range(0,len(powPartList)):
        result = powPartList[y] ** powPartList2[y]
        resultFunc(result)

# nth root =====================
elif selectedOperation == 6:
    nthPartTotal = int(input("\nHow many values are there?\n"))
    nthPartList = []
    nthPartList2 = []
    for x in range(0,nthPartTotal):
        nthPart = equationPart(input("\nWhat is the value that you want the nth root of?\n"))
        nthPart2 = equationPart2(input("\nWhat is the root you want?\n"))
        nthPartList.append(nthPart)
        nthPartList2.append(nthPart2)
    for y in range(0,len(nthPartList)):
        result = nthPartList[y] ** (1/nthPartList2[y])
        resultFunc(result)

# area =====================
elif selectedOperation == 7:
    selectedShape = shapePick()
    # square/rectangle =====================
    if selectedShape == 0 or selectedShape == 1:
        shapeTotal = int(input("\nHow many squares/rectangles are there?\n"))
        rectangleSideList = []
        rectangleSideList2 = []
        for x in range(0,shapeTotal):
            rectangleSide = equationPart(input("\nWhat is the first side length?\n"))
            rectangleSide2 = equationPart2(input("\nWhat is the first side length?\n"))
            rectangleSideList.append(rectangleSide)
            rectangleSideList2.append(rectangleSide2)
        for y in range(0,len(rectangleSideList)):
            result = rectangleSideList[y] * rectangleSideList2[y]
            resultFunc(result)
    # circle =====================
    elif selectedShape == 2:
        shapeTotal = int(input("\nHow many circles are there?\n"))
        circleRadiusList = []
        diameterOrRadius = input("\nDo you have the diameter or the radius?\n")
        if diameterOrRadius.islower() == False:
            diameterOrRadius = diameterOrRadius.lower()
        else:
            if diameterOrRadius == "radius":
                for x in range(0,shapeTotal):
                    radius = equationPart(input("\nWhat is the radius of the circle?\n"))
                    circleRadiusList.append(radius)
                for y in circleRadiusList:
                    result = (3.14 * y) ** 2
                    resultFunc(result)
            elif diameterOrRadius == "diameter":
                for x in range(0,shapeTotal):
                    diameter = equationPart(input("\nWhat is the diameter of the circle?\n"))
                    circleRadiusList.append((diameter/2))
                for y in circleRadiusList:
                    result = (3.14 * y) ** 2
                    resultFunc(result)
            else:
                print("Invalid input!")
    # triangle =====================
    elif selectedShape == 3:
        shapeTotal = int(input("\nHow many triangles are there?"))
        trianglePartList = []
        trianglePartList2 = []
        for x in range(0,shapeTotal):
            trianglePart = equationPart(input("\nWhat is the base length?\n"))
            trianglePart2 = equationPart2(input("\nWhat is the height?\n"))
            trianglePartList.append(trianglePart)
            trianglePartList2.append(trianglePart2)
        for y in range(0,len(trianglePartList)):
            result = (trianglePartList[y] * trianglePartList2[y]) / 2
            resultFunc(result)
