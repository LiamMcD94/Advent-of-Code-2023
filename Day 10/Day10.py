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
        Y = position
        X = line
        inputLines[X][Y]

        endPosition = ""
        lastPosition = ""
        steps = 0

        while endPosition != "S":
            #check up the position
            if inputLines[X][Y] in ('S'):
                if inputLines[X - 1][Y] in ("|", "7", "F"):
                #  print("there is an {} above starting postion, going up!".format(inputLines[up][Y]))
                    X -= 1
                    lastPosition = "up"
                    endPosition = inputLines[X][Y]
                    steps += 1

                elif inputLines[line][Y - 1] in ("-" or "F" or "L") and lastPosition != "right":
                #  print("there is an {} left of the starting postion, going left!".format(inputLines[X][left]))
                    Y -= 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "left"
                    steps += 1

                #check to the right of position
                elif inputLines[line][Y + 1] in ("-" or "7" or "J") and lastPosition != "left":
                #  print("there is an {} right of the starting postion, going left!".format(inputLines[X][right]))  
                    Y += 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "right"
                    steps += 1
            
                #check down position
                elif inputLines[X + 1][position] in ("|" or "L" or "J") and lastPosition != "up":
                #  print("there is an {} below the starting postion, going down!".format(inputLines[down][Y]))
                    X += 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "down"
                    steps += 1

            elif inputLines[X][Y] in ('F'):
                if lastPosition == "up":
                ##  print("its a {}, going right!".format(inputLines[X][Y]))
                    Y += 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "right"
                    steps += 1

                elif lastPosition == "left":
                # print("it's a {}, going down!".format(inputLines[X][Y]))
                    X += 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "down"
                    steps += 1

            elif inputLines[X][Y] in ('J'):
                if lastPosition == "right":
                    #print("it's a {}, going up!{}, {} and last position {}".format(inputLines[X][Y], [X], [Y], endPosition))
                    X -= 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "up"
                    steps += 1

                elif lastPosition == "down":
                # print("it's a {}, going left!{}, {} and last position {}".format(inputLines[X][Y], [X], [Y], endPosition))
                    Y -= 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "left"
                    steps += 1
            
            elif inputLines[X][Y] in ('L'):
                if lastPosition == "left":
                    #print("it's a {}, going up!{}, {} and last position {}".format(inputLines[X][Y], [X], [Y], endPosition))
                    X -= 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "up"
                    steps += 1

                elif lastPosition == "down":
                    #print("it's a {}, going right! position {}, {} and last position {}".format(inputLines[X][Y], [X], [Y], endPosition))
                    Y += 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "right"
                    steps += 1

            elif inputLines[X][Y] in ('|'):
                if lastPosition == "up":
                    #print("it's a {}, going up!{}, {} and last position {}".format(inputLines[X][Y], [X], [Y], endPosition))
                    X -= 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "up"
                    steps += 1

                elif lastPosition == "down":
                    #print("it's a {}, going down!{}, {} and last position {}".format(inputLines[X][Y], [X], [Y], endPosition))
                    X += 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "down"
                    steps += 1
                
            elif inputLines[X][Y] in ('-'):
                if lastPosition == "left":
                    #print("it's a {}, going left!{}, {} and last position {}".format(inputLines[X][Y], [X], [Y], endPosition))
                    Y -= 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "left"
                    steps += 1

                elif lastPosition == "right":
                    #print("it's a {}, going right!{}, {} and last position {}".format(inputLines[X][Y], [X], [Y], endPosition))
                    Y += 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "right"
                    steps += 1

            elif inputLines[X][Y] in ('7'):
                if lastPosition == "up":
                    #print("it's a {}, going left!{}, {} and last position {}".format(inputLines[X][Y], [X], [Y], endPosition))
                    Y -= 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "left"
                    steps += 1

                elif lastPosition == "right":
                    #print("it's a {}, going down!{}, {} and last position {}".format(inputLines[X][Y], [X], [Y], endPosition))
                    X += 1
                    endPosition = inputLines[X][Y]
                    lastPosition = "down"
                    steps += 1      
        result = steps /2
        print(int(result))
    
    findStartReturn = findStart()
    pipeTravel()
part1()
