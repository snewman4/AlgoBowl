# Team Merge Conflicts Algobowl Solution Algorithm

# name of file to read
fileName = ''

# get file
inFile = open(fileName)

# read first line to get size (of file) and num vars
firstLine = [int(x) for x in inFile.readline().split()]
size = firstLine[0]
numVars = firstLine[1]

# array of numbers for vars, all start at 0
arr = [0] * numVars
# if number read in is negative, subtract one at index=num
# if number read in is positive, add one at index=num

# loop, if number in array is negative, make it false, if positive, make it true
currLine = [int(x) for x in inFile.readline().split()]
counter = 1
trueCount = 0
while currLine
    # get 2 vals in line
    num1 = currLine[0]
    num2 = currLine[1]

    # adds -1 if num is negative, 1 if positive
    arr[abs(num1)] += (num1)/(num1)
    arr[abs(num2)] += (num2)/(num2)

    if (num1 > 0 and num2 > 0) or (num1 > 0) or (num2 > 0) :
        trueCount +=1

    currLine = [int(x) for x in inFile.readline().split()]

fileIn.close()   

# write true count and array of solutions to output file
# if arr[index] > 0, write 1, if <0, write 0

fileOut = open("output.txt", "x")
fileOut.write(trueCount+'\n')
for x in arr:
    if x <= 0:
        fileOut.write("0\n")
    else:
        fileOut.write("1\n")

