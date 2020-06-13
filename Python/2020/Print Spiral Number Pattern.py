# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:23:28 2020

@author: joshc
Spiral Printing, based on a meme of a HackerRank Problem

Given an odd perfect square N^2, and a direction (CW or CCW)
    print out a NxN array of numbers with 1 in the center, and the values
    spiraling outword in the chosen direction.
    
    Example: N^2 = 9, Dir = CW
    
    Output:
        7 8 9 
        6 1 2
        5 4 3
"""
"""
Ideas for spiral function
    Have to keep track of which spiral you're printing
    
    The below formulas break on n = 1, thus hardcoded a 1 into center 
        of array at creation, and we always start on spiral 2
    
    Spiral will range from input (2n-3)^2+1 up to (2n-1)^2 
        where n is your spiral value
    Spiral 1 = 1-1
    Spiral 2 = 2-9
    Spiral 3 = 10-25
    Spiral  4 = 26-49

    
    Array Size to Spiral Count:
        3, 2
        5, 3
        7, 4
        x = 2y-1
    Max Spirals: 
        x --> array size
        y --> max number of spirals
        y = (x+1)//2
    
    S2: down 1, over 1
    s3: down 3, over 1
    s4: down 5, over 1
    
    down = 2*spiral - 3
    
"""
"""
    Inputs: which spiral you are on
    In function:
        start number = (2n-3)^2+1
        end number = (2n-1)^2
    Starting Location:
        always 1 shifted horizontally based on loc of last spiral end
        can use dir to allow for right shift with cw, and left shift with ccw
            define dir as 1 for cw, -1 for ccw
    Example for n = 5, cw
        s1: 2,2
        s2: 2,3
        s3: 1,4
    n=5 ccw
        s1 = 2,2
        s2 = 2,1
        s3 = 1,0
        y = 2x-3
        size+3/2 = x
    Example start loc: for n = 7 sized array going cw
        S1: Starts at 3,3
        S2: Starts at 3,4
        S3: Starts at 2,5
        S4: Starts at 1,6
        
    Example start for ccw with n = 7
        S1: Starts at 3,3
        S2: Starts at 3,2
        S3: Starts at 2,1
        S4: Starts at 1,0
        
        start_column = size//2 + (spiral number - 1) * dir
        start_row = (size + 3)/2 - spiral
    Turning:
        Given a range of values, you print out however many based on your 
        spiral number, then make a turn inthe direction given in the prompt
"""
def makeStorageArray(size):
    #Given a size, output a square array for use in indexing
    array = [[0 for _ in range(size)] for _ in range(size)]
    center = (size//2)
    array [center][center] = 1
    return array

def printArray(array, size):
    for i in range(size):
        for j in range(size):
            print(str(array[i][j]) + "\t", end = "")
        print()
    print()
    
def addInDirection(array, direction, startVal, endVal, startPosX, startPosY, clockDirection):
    """
    Based on dir, you either go:
    CW (clockDirection = 1): down, left, up, right
    CCW (clockDirection = -1): down, right, up, left
    
    You always print out spiralNummber amount of nums, then turn
    ie if you're on spiral2, you print 2,3 then turn, print 4,5, then turn...
    When you execute a turn, you have to increment a location value by 1
        depending on turn direction, to get the start of the next block
    """
    xLoc = startPosX
    yLoc = startPosY
    if clockDirection: 
        nextVal = startVal
    else:
        nextVal = endVal
    while (nextVal <= endVal and nextVal >= startVal):
        if direction == "left":
            #Move across a row from right to left, increasing the number put in cell
            array[startPosY][xLoc] = nextVal
            xLoc -=  1
            nextVal += 1

        elif direction == "right":
            #Move across a row from left to right, increasing the number put in cell
            array[startPosY][xLoc] = nextVal
            xLoc +=  1
            nextVal += 1
            
        elif direction == "up":
            #Move across a row from down to up, increasing the number put in cell
            array[yLoc][startPosX] = nextVal
            yLoc -=  1
            nextVal += 1 
            
        else: #direction == "down"
            #Move across a row from up to down, increasing the number put in cell
            array[yLoc][startPosX] = nextVal
            yLoc +=  1
            nextVal += 1 
        # printArray(array, len(array))
    return array
        
    
def addNumbersToArray(array, spiralNumber, size, clockDirection):
    if spiralNumber == 1: return array
    start_column = int(size//2 + (spiralNumber - 1) * clockDirection)
    start_row = int((size + 3)/2 - spiralNumber)
    low = (2*spiralNumber-3)**2 + 1
    high = (2*spiralNumber-1)**2
    rangeForSpiral = high - low
    rangeChunk = rangeForSpiral//4
    
    #Hardcoded test input
    # array[start_row][start_column] = low
    #Turning Portion
    startVal = low
    endVal = low + rangeChunk
    for i in range(4):
        if i == 0:
            direction = "down"
        elif i == 1:
            if clockDirection == 1:
                direction = "left"
            else:
                direction = "right"
        elif i == 2:
            direction = "up"
        elif i == 3:
            if clockDirection == 1:
                direction = "right"
            else:
                direction = "left"
        # print(direction, spiralNumber, start_row,  start_column, startVal, endVal)
        array = addInDirection(array, direction, startVal, endVal, start_column, start_row, clockDirection)
        # printArray(array, size)
        if direction == "down":
            start_row += 2*spiralNumber - 3
            start_column -= clockDirection
        elif direction == "up":
            start_row -= 2*spiralNumber - 3
            start_column += clockDirection
        elif direction == "left":
            start_row -= clockDirection
            start_column -= (2*spiralNumber - 3)
        elif direction == "right":
            start_row += clockDirection
            start_column += (2*spiralNumber - 3)
        # print(direction, spiralNumber, start_row,  start_column)
        startVal += rangeChunk + 1
        endVal += rangeChunk + 1
            
    return array

for i in range(1,6,2):
    size = i
    array = makeStorageArray(size)
    spiralMaxNum = (size+1)//2
    
    #Print the Spiral going clockwise
    print("Size: " + str(i) + "  \nDirection: CW  Max Val: " + str(i**2))
    for spiralNum in range(2,(spiralMaxNum + 1)):
        array = addNumbersToArray(array, spiralNum, size, 1)
    printArray(array, size)

    #Print the spiral going counter clockwise
    print("Size: " + str(i) + "  \nDirection: CCW  Max Val: " + str(i**2))
    array = makeStorageArray(size)
    for spiralNum in range(2,(spiralMaxNum + 1)):
        array = addNumbersToArray(array, spiralNum, size, -1)
    printArray(array, size)
    
