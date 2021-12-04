import re

def main():
    minRound = 100
    minCardList = []
    soma = 0
    draw = TakeDraw()
    i = 0
    while i < 100:
        cardToAnalize, cardList = BuildCard(i)
        round, cardList = CheckForWin(draw, cardToAnalize, cardList)
        if round < minRound:
            minRound = round
            minCardList = cardList.copy()
        i += 1
    for number in minCardList:
        soma += int(number)
    print(soma * int(draw[minRound]))
    

#TODO: FOR EACH CARD CHECK THE ROUND WHERE THE WIN CONDITION IS MET AND STORE A LIST OF NOT MARKED NUMBERS. COMPARED WIN ROUNDS EVERYTIME WE CHECK A CARD AND STORE ONLY THE LIST
#AND ROUND OF THE ONE THAT HAS THE SMALEST ROUND

def TakeDraw():
    with open("input") as f:
        firstLine = f.readline()
    drawList = firstLine.split(",")
    return drawList

def BuildCard(cardNumber):
    input = open("input")
    card = []
    numberCardList = []
    i = 2
    counter = 0
    lineToStart = i + (6 * cardNumber)
    lines = input.readlines()
    while counter < 5:
        row = re.split(r"\s+", lines[lineToStart + counter].strip())
        card.append(row)
        for number in row:
            numberCardList.append(number)
        counter += 1
    return card, numberCardList

def CheckForWin(draw, cardToAnalize, cardList):
    round = 0
    column = 0
    row = 0
    marksDictionary = {}
    for round in range(len(draw)):
        row = 0
        while row < 5:
            column = 0
            while column < 5:
                numerodraw= draw[round]
                #print(cardToAnalize[row][column])
                if draw[round] == cardToAnalize[row][column]:
                    cardList.remove(draw[round])
                    marksDictionary[column, row] = "1"
                column += 1
            row += 1
        if CheckIfBingo(marksDictionary):
            return round, cardList

def CheckIfBingo(marksDictionary):
    row = 0
    collumn = 0
    countForBingoH = 0
    countForBingoV = 0
    while row < 5:
        if (row, collumn) in marksDictionary:
            countForBingoH += 1
            collumn += 1
            if countForBingoH == 5:
                return True
        else:
            row += 1
            collumn = 0
            countForBingoH = 0
    while collumn < 5:
        if (row, collumn) in marksDictionary:
            countForBingoV += 1
            row += 1
            if countForBingoV == 5:
                return True
        else:
            collumn += 1
            row = 0
            countForBingoV = 0
    return False

if __name__ == "__main__":
    main()