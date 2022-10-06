# Generates an input file for AlgoBowl

from random import randrange


def genInput(numVars, numClauses):
    file = open("input.txt", "w")

    # Writes meta information
    file.write(str(numVars) + " " + str(numClauses) + "\n")

    for i in range(numClauses):
        # Can be positive or negative
        var1 = randrange(-numVars, numVars + 1)
        while var1 == 0: # Cannot be 0
            var1 = randrange(-numVars, numVars + 1)
        
        var2 = var1
        # Can not have two of the same variable in one clause
        while var2 == var1 or var2 == -var1 or var2 == 0:
            var2 = randrange(-numVars, numVars + 1)
        
        file.write(str(var1) + " " + str(var2) + "\n")

    file.close()

genInput(numVars=500, numClauses=50000)