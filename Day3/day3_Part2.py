# Parse grid and return list of symbol tuples
def parseGrid(grid):
    symbols = {}
    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(row)):
            if row[x] == '*':
                symbols[(y, x)] = []
    
    return symbols

def checkNumber(x_start, x_end, y, symbols, row):
    # y+2 because range end is non-inclusive
    for y in range(y-1, y+2, 1):
        for x in range(x_start-1, x_end+1, 1):
            if (y, x) in symbols:
                symbols[(y, x)].append(int(row[x_start:x_end]))

def findNumbers(grid, symbols):
    numbers = []
    for y in range(len(grid)):
        row = grid[y]
        x_start = -1
        x_end = -1
        digit_flag = False
        print(f'Row {y}')
        for x in range(len(row)):
            if row[x].isdigit() and not digit_flag:
                x_start = x
                digit_flag = True
            # Include the second conditional for the case the number ends at the end of the line 
            elif (not row[x].isdigit() and digit_flag) or (x == len(row) - 1 and digit_flag):
                x_end = x

                # Add one if end of line
                if (row[x].isdigit() and x == len(row) - 1):
                    x_end += 1

                digit_flag = False
                checkNumber(x_start, x_end, y, symbols, row)
                    
    return numbers
    
if __name__ == "__main__":
    file = open('inputfile_1.txt', 'r')
    lines = file.read().splitlines()

    grid = []
    sum = 0
    for line in lines:
        grid.append(line)

    # Precompute in the indexes of all the symbols
    symbols = parseGrid(grid)
    # Check the areas around each number to see if they match the symbols
    findNumbers(grid, symbols)

    for key in symbols:
        if len(symbols[key]) == 2:
            sum += symbols[key][0] * symbols[key][1]

    print(sum)
    file.close()
