# read https://adventofcode.com/2023/day/1 for information about this puzzle, if you would like to use the code to solve the puzzle, just empty input.txt 
#    and copy and paste your own input data into it.

input = open('input.txt', 'r')
inputLines = input.readlines()

def part1():
    def findStart():
        i = 0
        for line in inputLines:
            if "S" in line:
            # print("start position is in line {} at position {}".format(i, line.index('S')) )
                startPositionY = i
                startPositionX = line.index('S')
                return [startPositionY, startPositionX]
            else:
                i +=1

    def pipeTravel():
        line, position = findStartReturn
        X = position
        Y = line
        inputLines[Y][X]

        endPosition = ""
        lastPosition = ""
        steps = 0

        while endPosition != "S":
            #check up the position
            if inputLines[Y][X] in ('S'):
                if inputLines[Y - 1][X] in ("|", "7", "F"):
                #  print("there is an {} above starting postion, going up!".format(inputLines[Y += 1][X]))
                    Y -= 1
                    lastPosition = "up"
                    endPosition = inputLines[Y][X]
                    steps += 1

                elif inputLines[line][X - 1] in ("-" or "F" or "L") and lastPosition != "right":
                #  print("there is an {} left of the starting postion, going left!".format(inputLines[Y][X -= 1]))
                    X -= 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "left"
                    steps += 1

                #check to the right of position
                elif inputLines[line][X + 1] in ("-" or "7" or "J") and lastPosition != "left":
                #  print("there is an {} right of the starting postion, going left!".format(inputLines[Y][X += 1]))  
                    X += 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "right"
                    steps += 1
            
                #check down position
                elif inputLines[Y + 1][X] in ("|" or "L" or "J") and lastPosition != "up":
                #  print("there is an {} below the starting postion, going down!".format(inputLines[Y += 1][X]))
                    Y += 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "down"
                    steps += 1

            elif inputLines[Y][X] in ('F'):
                if lastPosition == "up":
                ##  print("its a {}, going right!".format(inputLines[Y][X]))
                    X += 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "right"
                    steps += 1

                elif lastPosition == "left":
                # print("it's a {}, going down!".format(inputLines[Y][X]))
                    Y += 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "down"
                    steps += 1

            elif inputLines[Y][X] in ('J'):
                if lastPosition == "right":
                    #print("it's a {}, going up!{}, {} and last position {}".format(inputLines[Y][X], [Y], [X], endPosition))
                    Y -= 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "up"
                    steps += 1

                elif lastPosition == "down":
                # print("it's a {}, going left!{}, {} and last position {}".format(inputLines[Y][X], [Y], [X], endPosition))
                    X -= 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "left"
                    steps += 1
            
            elif inputLines[Y][X] in ('L'):
                if lastPosition == "left":
                    #print("it's a {}, going up!{}, {} and last position {}".format(inputLines[Y][X], [Y], [X], endPosition))
                    Y -= 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "up"
                    steps += 1

                elif lastPosition == "down":
                    #print("it's a {}, going right! position {}, {} and last position {}".format(inputLines[Y][X], [Y], [X], endPosition))
                    X += 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "right"
                    steps += 1

            elif inputLines[Y][X] in ('|'):
                if lastPosition == "up":
                    #print("it's a {}, going up!{}, {} and last position {}".format(inputLines[Y][X], [Y], [X], endPosition))
                    Y -= 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "up"
                    steps += 1

                elif lastPosition == "down":
                    #print("it's a {}, going down!{}, {} and last position {}".format(inputLines[Y][X], [Y], [X], endPosition))
                    Y += 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "down"
                    steps += 1
                
            elif inputLines[Y][X] in ('-'):
                if lastPosition == "left":
                    #print("it's a {}, going left!{}, {} and last position {}".format(inputLines[Y][X], [Y], [X], endPosition))
                    X -= 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "left"
                    steps += 1

                elif lastPosition == "right":
                    #print("it's a {}, going right!{}, {} and last position {}".format(inputLines[Y][X], [Y], [X], endPosition))
                    X += 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "right"
                    steps += 1

            elif inputLines[Y][X] in ('7'):
                if lastPosition == "up":
                    #print("it's a {}, going left!{}, {} and last position {}".format(inputLines[Y][X], [Y], [X], endPosition))
                    X -= 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "left"
                    steps += 1

                elif lastPosition == "right":
                    #print("it's a {}, going down!{}, {} and last position {}".format(inputLines[Y][X], [Y], [X], endPosition))
                    Y += 1
                    endPosition = inputLines[Y][X]
                    lastPosition = "down"
                    steps += 1      
        result = steps /2
        print(int(result))
    
    findStartReturn = findStart()
    pipeTravel()
part1()
