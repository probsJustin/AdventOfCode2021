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
    returnObject = [list()]
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
                        if (bingoCards[card][row][item][singleton][1] == bingoInput[itemToFind] and card not in returnObject[0]):
                            bingoCards[card][row][0][singleton] = 1
                            bingoCards[card][row][item][singleton][0] = 1
                            for y in range(0, len(bingoCards[card])):
                                if(checkColBingoCard(bingoCards[card]) and card not in returnObject[0]):
                                    returnObject[0].append(card)
                                    returnObject.append([card, bingoCards[card], bingoInput[itemToFind]])
                                if (bingoCards[card][y][0] == [1, 1, 1, 1, 1] and card not in returnObject[0]):
                                    returnObject[0].append(card)
                                    returnObject.append([card, bingoCards[card], bingoInput[itemToFind]])
    return returnObject

winningInfo = calculate()
sum_val = 0
for x in winningInfo[-1][1]:
    for y in x[1]:
        if(y[0] == 0):
            sum_val = sum_val + int(y[1])

print(f'Sum of the card: {sum_val}')
print(f'Number we stopped on: {winningInfo[-1][2]}')
print(f'Answer: {sum_val * int(winningInfo[-1][2])}')
print("CARD:")
for x in winningInfo[-1][1]:
    print(x[1])


# Sum of the card: 313
# Number we stopped on: 41
# Answer: 12833
# CARD:
# [[1, '52'], [1, '31'], [1, '24'], [1, '68'], [1, '41']]
# [[0, '48'], [1, '82'], [1, '19'], [0, '29'], [1, '65']]
# [[1, '51'], [0, '91'], [1, '97'], [1, '39'], [1, '80']]
# [[0, '3'], [1, '55'], [1, '43'], [1, '40'], [1, '38']]
# [[1, '20'], [0, '89'], [0, '53'], [1, '45'], [1, '75']]
