import string

input = open('input.txt', 'r')
inputLines = input.readlines()


def findStart():
    i = 0
    for line in inputLines:
        i += 1
        if "S" in line:
            print("start position is in line {} at position {}".format(i, line.index('S')) )
            startPositionY = i
            startPositionX = line.index('S')
            return [startPositionY, startPositionX];


startPosition = findStart()
Y, X = startPosition

    
findStart()
print("return result: {}, {}".format(X, Y))