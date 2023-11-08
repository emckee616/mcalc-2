import math
import time
import os

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

# display welcome message and init operationPick func =====================
operationsList = ["Add", "Subtract", "Multiply", "Divide", "Absolute-Value", "Exponents", "Roots", "Area", "Midpoint", "Distance", "Translation", "Rotation"]
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
        powPart2 = equationPart(input("\nEnter what exponent it has.\n"))
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
        nthPart2 = equationPart(input("\nWhat is the root you want?\n"))
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
            rectangleSide2 = equationPart(input("\nWhat is the first side length?\n"))
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
            trianglePart2 = equationPart(input("\nWhat is the height?\n"))
            trianglePartList.append(trianglePart)
            trianglePartList2.append(trianglePart2)
        for y in range(0,len(trianglePartList)):
            result = (trianglePartList[y] * trianglePartList2[y]) / 2
            resultFunc(result)
    # trapezoid =====================
    elif selectedShape == 4:
        shapeTotal = int(input("\nHow many trapezoids are there?\n"))
        trapezoidPartList = []
        trapezoidPartList2 = []
        trapezoidPartList3 = []
        for x in range(0,shapeTotal):
            trapezoidPart = equationPart(input("\nWhat is one base of the trapezoid?\n"))
            trapezoidPart2 = equationPart(input("\nWhat is the other base of the trapezoid?\n"))
            trapezoidPart3 = equationPart(input("\nWhat is the height of the trapezoid?\n"))
            trapezoidPartList.append(trapezoidPart)
            trapezoidPartList2.append(trapezoidPart2)
            trapezoidPartList3.append(trapezoidPart3)
        for y in range(0,len(trapezoidPartList)):
            result = ((trapezoidPartList[y] + trapezoidPartList2[y]) / 2) * trapezoidPartList3[y]
            resultFunc(result)

# midpoint =====================
elif selectedOperation == 8:
    midpointX1 = equationPart(input("\nWhat is the first x coordinate?\n"))
    midpointX2 = equationPart(input("\nWhat is the second x coordinate?\n"))
    midpointY1 = equationPart(input("\nWhat is the first y coordinate?\n"))
    midpointY2 = equationPart(input("\nWhat is the second y coordinate?\n"))
    result = ((midpointX1 + midpointX2) / 2), ((midpointY1 + midpointY2) / 2)
    resultFunc(result)

# distance =====================
elif selectedOperation == 9:
    distanceX1 = equationPart(input("\nWhat is the first x coordinate?\n"))
    distanceX2 = equationPart(input("\nWhat is the second x coordinate?\n"))
    distanceY1 = equationPart(input("\nWhat is the first y coordinate?\n"))
    distanceY2 = equationPart(input("\nWhat is the second y coordinate?\n"))
    result1 = ((distanceX2 + distanceX1) ** 2) + ((distanceY2 + distanceY1) ** 2)
    result2 = result1 ** 0.5
    resultFunc(result2)

# translation =====================
elif selectedOperation == 10:
    pointTotal = int(input("\nHow many points are there?\n"))
    pointList = []
    pointList2 = []
    transList = []
    transList2 = []
    for x in range(0,pointTotal):
        pointX = equationPart(input("\nWhat is the x coordinate of the point?\n"))
        pointY = equationPart(input("\nWhat is the y coordinate of the point?\n"))
        transX = equationPart(input("\nWhat is the x translation? (use negative number for moving left/down)\n"))
        transY = equationPart(input("\nWhat is the y translation? (use negative number for moving left/down)\n"))
        pointList.append(pointX)
        pointList2.append(pointY)
        transList.append(transX)
        transList2.append(transY)
    for y in range(0,len(pointList)):
        result = str(pointList[y] + transList[y]) + " " + str(pointList2[y] + transList2[y])
        resultFunc(result)

# rotation =====================
elif selectedOperation == 11:
    pointTotal = int(input("\nHow many points are there?\n"))
    pointList = []
    pointList2 = []
    directionsList = ["Clockwise", "Counter Clockwise"]
    degreeList = ["90", "180", "270", "360"]
    for x in range(0,pointTotal):
        pointX = equationPart(input("\nWhat is the x coordinate of the point?\n"))
        pointY = equationPart(input("\nWhat is the y coordinate of the point?\n"))
        pointList.append(pointX)
        pointList.append(pointY)
    for x in range(0,len(pointList)):
        for x in range(0,len(directionsList)):
            print("    " + directionsList[x] + "\n ==============================")
        selectedDirection = equationPart(input("\nWhat direction is the rotation?\n"))

        for y in range(0,len(degreeList)):
            print("    " + degreeList[y] + "\n ==============================")
        selectedDegree = equationPart(input("\nWhat is the degree of the rotation?\n"))

        if selectedDirection == directionsList[0].lower():
            if selectedDegree == degreeList[0]:
                result = str(pointList2[x]) + " " + str(pointList[x] * -1)
            elif selectedDegree == degreeList[1]:
                result = str(pointList[x] * -1) + " " + str(pointList2[x] * -1)
            else:
                result = str(pointList2[x] * -1) + " " + str(pointList[x])

        elif selectedDirection == directionsList[1].lower():
            print()