# Team Merge Conflicts Algobowl Solution Algorithm

# name of file to read
inputFileName = "input_group463.txt"
inputFilePath = "allInputs\\" + inputFileName

# get file
inFile = open(inputFilePath)

# read first line to get size (of file) and num vars
firstLine = [int(x) for x in inFile.readline().split()]
size = firstLine[0]
numVars = firstLine[1]

# array of numbers for vars, all start at 0
arr = [0] * numVars
# if number read in is negative, subtract one at index=abs(num)
# if number read in is positive, add one at index=abs(num)
# if even number of positive and negative at the end, default to false

# first loop determines if each variable is more positive or negative
currLine = [int(x) for x in inFile.readline().split()]
while currLine:
    # get 2 vals in line
    num1 = currLine[0]
    num2 = currLine[1]

    if (num1 == 0) or (num2 == 0):
        print("Variable 0 detected")
        break

    # adds -1 if num is negative, 1 if positive
    arr[abs(num1) - 1] += (num1)/abs(num1)
    arr[abs(num2) - 1] += (num2)/abs(num2)

    currLine = [int(x) for x in inFile.readline().split()]

inFile.close()

# Read the file a second time, this time counting True clauses
inFile = open(inputFilePath)
inFile.readline() # Get rid of first line
currLine = [int(x) for x in inFile.readline().split()]
trueCount = 0
while currLine:
    num1 = currLine[0]
    num2 = currLine[1]
    num1Val = arr[abs(num1) - 1]
    num2Val = arr[abs(num2) - 1]

    # Check the following four possibilities for this to be true:
    # 1. num1Val is True and num1 is not negated
    # 2. num1Val is False and num1 is negated
    # 3. num2Val is True and num2 is not negated
    # 4. num2Val is False and num2 is negated
    if (num1Val > 0 and num1 > 0) or (num1Val <= 0 and num1 < 0) or (num2Val > 0 and num2 > 0) or (num2Val <= 0 and num2 < 0):
        trueCount += 1

    currLine = [int(x) for x in inFile.readline().split()]

inFile.close()

# write true count and array of solutions to output file
# if arr[index] > 0, write 1, if <= 0, write 0
# note that if there are an even amount of pos and neg, it defaults to false
outputFileName = "output" + inputFileName[11:14] + ".txt"
outputFilePath = "allOutputs\\" + outputFileName
fileOut = open(outputFilePath, "w")
fileOut.write(str(trueCount) + '\n')
for x in arr:
    if x <= 0:
        fileOut.write("0\n")
    else:
        fileOut.write("1\n")

