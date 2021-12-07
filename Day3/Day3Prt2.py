def processList(listLines, action):
    sizeInt = len(listLines[0])
    for y in range(0, sizeInt - 1):
        bitCounter = 0
        bitToRemove = 2
        for x in listLines:
            if(x[y] != '\n'):
                bitCounter += int(x[y])
        if(bitCounter > (len(listLines) - bitCounter)):
            bitToRemove = 1
        else:
            if(bitCounter == (len(listLines) - bitCounter)):
                bitToRemove = 1
            else:
                bitToRemove = 0
        for x in range(0, len(listLines)):
            if(listLines[x][y] != '\n'):
                if(action == "oxy"):
                    if((int(listLines[x][y]) == bitToRemove) and (len(listLines) > 1)):
                        print(len(listLines))
                        listLines[x] = ""
                else:
                    if((int(listLines[x][y]) != bitToRemove) and (len(listLines) > 1)):
                        print(len(listLines))
                        listLines[x] = ""
        listLines = list(filter(("").__ne__, listLines))
    return int(listLines[0], 2)


with open('./puzzle.txt', 'r') as fh:
    all_lines = fh.readlines()
    cpy_all_lines = all_lines.copy()

    oxy = processList(all_lines, "oxy")
    co2 = processList(cpy_all_lines, "co2")

    print(f'{co2 * oxy}')