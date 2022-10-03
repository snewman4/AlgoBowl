# Generates an input file for AlgoBowl

from random import randrange
import os


def genInput(numVars, numClauses):
    os.remove("input.txt")
    file = open("input.txt", "a")

    file.write(str(numVars) + " " + str(numClauses) + "\n")

    for i in range(numClauses):
        var1 = randrange(-numVars, numVars + 1)
        while var1 == 0:
            var1 = randrange(-numVars, numVars + 1)
        
        var2 = var1
        while var2 == var1 or var2 == -var1 or var2 == 0:
            var2 = randrange(-numVars, numVars + 1)
        
        file.write(str(var1) + " " + str(var2) + "\n")

    file.close()

genInput(numVars=2, numClauses=100)