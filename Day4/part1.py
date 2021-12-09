def getPuzzle(fileLocation):
    with open(fileLocation, 'r') as fh:
        all_lines = fh.readlines()
    return all_lines

def rmvBlanks(listLines):
    returnObject = list()
    for x in list(filter(('').__ne__, listLines)):
        returnObject.append([0,x])
    return [[0,0,0,0,0],returnObject]

def checkColBingoCard(bingoCard):
    for x in range(0, 5):
        if([bingoCard[0][0][x] ,bingoCard[1][0][x], bingoCard[2][0][x], bingoCard[3][0][x], bingoCard[4][0][x]] == [1,1,1,1,1]):
            return True

def calculate():
    puzzle_lines = getPuzzle('./puzzle.txt')

    bingoInput = puzzle_lines[0].split(',')
    bingoCards = list()

    counter = 0
    cardThatWon = None
    while (counter < (len(puzzle_lines) - 5)):
        bingoCards.append([rmvBlanks(puzzle_lines[counter + 2][0:-1].split(' ')),
                           rmvBlanks(puzzle_lines[counter + 3][0:-1].split(' ')),
                           rmvBlanks(puzzle_lines[counter + 4][0:-1].split(' ')),
                           rmvBlanks(puzzle_lines[counter + 5][0:-1].split(' ')),
                           rmvBlanks(puzzle_lines[counter + 6][0:-1].split(' '))])
        counter = counter + 6
    for itemToFind in range(0, len(bingoInput)):
        for card in range(0, len(bingoCards)):
            for row in range(0, len(bingoCards[card])):
                for item in range(1, len(bingoCards[card][row])):
                    for singleton in range(0, len(bingoCards[card][row][item])):
                        if (bingoCards[card][row][item][singleton][1] == bingoInput[itemToFind]):
                            bingoCards[card][row][0][singleton] = 1
                            bingoCards[card][row][item][singleton][0] = 1
                            for y in range(0, len(bingoCards[card])):
                                if(checkColBingoCard(bingoCards[card])):
                                    return [bingoCards, "win", bingoInput[itemToFind], bingoCards[card]]
                                if (bingoCards[card][y][0] == [1, 1, 1, 1, 1]):
                                    return [bingoCards, "win", bingoInput[itemToFind], bingoCards[card]]


winningInfo = calculate()
sum_val = 0
for x in winningInfo[3]:
    for y in x[1]:
        if(y[0] == 0):
            sum_val = sum_val + int(y[1])


print(f'Sum of the card: {sum_val}')
print(f'Number we stopped on: {winningInfo[2]}')
print(f'Answer: {sum_val * int(winningInfo[2])}')
print("CARD:")
for x in winningInfo[3]:
    print(x[1])

# Sum of the card: 866
# Number we stopped on: 74
# Answer: 64084
# CARD:
# [[1, '7'], [1, '70'], [0, '5'], [0, '69'], [1, '4']]
# [[1, '34'], [0, '60'], [0, '40'], [0, '73'], [0, '6']]
# [[1, '74'], [0, '54'], [0, '67'], [0, '32'], [0, '38']]
# [[1, '93'], [0, '62'], [0, '17'], [0, '51'], [0, '86']]
# [[1, '57'], [0, '88'], [0, '99'], [0, '3'], [0, '16']]












