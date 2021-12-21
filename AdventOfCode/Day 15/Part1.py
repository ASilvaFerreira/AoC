import math
import time

def main():
    part2 = True
    input = TreatInput()
    if part2:
        print("treating input...")
        input = TreatInputPart2(input)
    startPos = (0, 0)
    endPos = (len(input[0]) - 1, len(input) - 1)

    
    origins = Dijkstra(input, startPos, endPos)
    path = BuildThePath(origins, endPos, startPos)
    CalculateRisk(input, path)

def TreatInputPart2(input):
    firstSize = len(input[0])
    for line in input:
        for number in line:
            if len(line) == firstSize * 5:
                break
            if number == 9:
                line.append(1)
            else:
                line.append(number + 1)
    
    for line in input:
        newLine = []
        
        if len(input) == firstSize * 5:
            break
        for number in line:
            if number == 9:
                newLine.append(1)
            else:
                newLine.append(number + 1)
        input.append(newLine.copy())

    return input

def TreatInput():
    input = []
    numbers = []
    rawInput = open("input")
    for line in rawInput:
        numbers = []
        for number in line.strip():
            numbers.append(int(number))
        input.append(numbers.copy())
    return input

def Dijkstra(input, startPos, endPos):
    start_time = time.time()
    print("Apllying Dijkstra...")
    finished = False

    distances = {}              #{(0,0) : 0}         pos: cost
    origins = {}                #{(0,1) : (0,0)}     endPos : starPos

    ExperienceDistancesList = []

    currentPos = startPos
    visited = []
    distancesStack = [0]

    #construnct a boolean list of visited points (all false at the beggining)
    for row in input:
        visitedCollums = []
        distancesCollums = []
        for collumn in row:
            visitedCollums.append(False)
            distancesCollums.append(math.inf)
        visited.append(visitedCollums.copy())
        ExperienceDistancesList.append(distancesCollums.copy())
    
    #initial spot is visited
    x, y = startPos
    ##visited[y][x] = True
    counter = 0
    while not finished:
        if counter == 10000:
            print("step: ", counter)
            print("--- %s seconds ---" % (time.time() - start_time))
        distances, origins, distancesStack, flag, nextPos = Explore(input, currentPos, ExperienceDistancesList, origins, distancesStack)
        currentPos, visited = Move(distances, distancesStack, currentPos, visited, flag, nextPos)

        if currentPos == endPos:
            finished = True
        counter += 1
    
    return origins

def Explore(input, currentPos, distances, origins, distancesStack):
    flag = False
    x, y = currentPos
    nextPos = (0, 0)
    if distances[y][x] != math.inf:
        cost = distances[y][x]
    else:
        cost = 0

    if x > 0:
        if distances[y][x-1] > input[y][x-1] + cost:
            costForNextStep = input[y][x-1] + cost
            distances[y][x-1] = input[y][x-1] + cost
            if costForNextStep < min(distancesStack):
                nextPos = (x-1, y)
                flag = True
            distancesStack.append(input[y][x-1] + cost)
            origins[(x-1,y)] = currentPos
            

    if x < len(input[0]) - 1:
        if distances[y][x+1] > input[y][x+1] + cost:
            costForNextStep = input[y][x-1] + cost
            distances[y][x+1] = input[y][x+1] + cost
            if costForNextStep < min(distancesStack):
                nextPos = (x+1, y)
                flag = True
            distancesStack.append(input[y][x+1] + cost)
            origins[(x+1,y)] = currentPos
    
    if y > 0:
        if distances[y-1][x] > input[y-1][x] + cost:
            costForNextStep = input[y][x-1] + cost
            distances[y-1][x] = input[y-1][x] + cost
            if costForNextStep < min(distancesStack):
                nextPos = (x, y-1)
                flag = True
            distancesStack.append(input[y-1][x] + cost)
            origins[(x,y-1)] = currentPos

    if y < len(input) - 1:
        if distances[y+1][x] > input[y+1][x] + cost:
            costForNextStep = input[y][x-1] + cost
            distances[y+1][x] = input[y+1][x] + cost
            if costForNextStep < min(distancesStack):
                nextPos = (x, y+1)
                flag = True
            distancesStack.append(input[y+1][x] + cost)
            origins[(x,y+1)] = currentPos
    
    distancesStack.sort()
    distancesStack = list(dict.fromkeys(distancesStack))
    return distances, origins, distancesStack, flag, nextPos


def Move(distances, distancesStack, currentPos, visited, flag, nextPos):

    if flag:
        x, y = nextPos
        visited[y][x] = True
        currentPos = (x, y)
        return currentPos, visited

    x = 0
    y = 0
    for i in range(len(distancesStack)):
        for y in range(len(distances)):
            for x in range(len(distances[y])):
                if visited[y][x] == False and distances[y][x] == distancesStack[i]:
                    visited[y][x] = True
                    currentPos = (x, y)
                    if i > 0:
                        for j in range(0,i):
                            distancesStack.pop(0)
                    return currentPos, visited

def BuildThePath(origins, endPos, startPos):
    afterPos = endPos
    originalPos = startPos
    path = []
    while True:
        if afterPos in origins:
            path.append(afterPos)
            afterPos = origins[afterPos]

        if afterPos == originalPos:
            return path
    
def CalculateRisk(input, path):
    risk = 0
    for x, y in path:
        risk += int(input[y][x])
    print(risk)


if __name__ == "__main__":
    main()