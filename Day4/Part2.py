import time
import re
# ADVENT OF CODE DAY 4 - PART1


def getbingonumbers(input):
    numbers = input.readline().strip().split(",")
    return numbers


def getbingoboards(input):
    BoardDict = {}
    BoardList = []
    boardCounter = 0
    input.readline()
    for i in input:
        if " " in i:
            line = "".join(i.strip())
            BoardList.append(re.split(r"\s+",line))
            # print(BoardList)
        else:
            BoardDict[boardCounter] = BoardList
            BoardList = []
            boardCounter += 1
    BoardDict[boardCounter] = BoardList
    return BoardDict


def findbingo(boards, numbers):
    BingoDict = {}
    winOrder = []
    for i in range(len(boards)):
        BingoDict[i] = [0]*10
    L = range(5)
    for number in numbers:
        # print(number)
        for i in boards:
            for row in L:
                for col in L:
                    if boards[i][row][col] == number:
                        # print(row, col+5)
                        boards[i][row][col] = 0
                        BingoDict[i][row] += 1
                        BingoDict[i][col+5] += 1
                    if 5 in BingoDict[i] and i not in winOrder:
                        winOrder.append(i)
                        # print(winOrder)
                    elif len(winOrder) == 100:
                        return boards[winOrder[-1]], int(number)

    # return winOrder[-1]


def main(file):
    input = open(file)
    NumberList = getbingonumbers(input)
    BingoBoards = getbingoboards(input)
    LastWinBoard, WinningNumber = findbingo(BingoBoards, NumberList)
    LastWinBoard = sum([sum(list(map(int,i))) for i in LastWinBoard])

    print("answer is: ", LastWinBoard * WinningNumber)


start_time = time.time()

main("input.txt")

print("--- %s seconds ---" % (time.time() - start_time))
