def getPuzzle(fileLocation):
    with open(fileLocation, 'r') as fh:
        all_lines = fh.readlines()
    return all_lines

cordinates = dict()

def writeToCordinates(min_x_input, min_y_input, func_x_distance, func_y_distance):
    global cordinates
    if(func_x_distance == 0 or func_y_distance == 0):
        for x in range(min_x_input, min_x_input + func_x_distance + 1):
            for y in range(min_y_input, min_y_input + func_y_distance + 1):
                try:
                    cordinates[f'{x}:{y}'] = cordinates[f'{x}:{y}'] + 1
                except Exception as error:
                    cordinates[f'{x}:{y}'] = 0

def countCordinates():
    global cordinates
    counter = 0
    for x in cordinates:
        if(cordinates[x] >= 1):
            counter = counter + 1
    print(counter)

def createCordinates(points):
    p1 = [int(x) for x in points[0].split(',')]
    p2 = [int(x) for x in points[1].split(',')]
    writeToCordinates(min(p1[0], p2[0]), min(p1[1], p2[1]), abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))


puzzle_lines = getPuzzle("./puzzle.txt")

for x in range(0, len(puzzle_lines)):
    createCordinates(((puzzle_lines[x].strip('\n')).replace(" -> ", ' ')).split(' '))

countCordinates()
