import string

def checkGame(input_string):
    b_min = 0
    g_min = 0
    r_min = 0

    game = input_string.split(':')
    rounds = game[1]
    game = game[0]

    for c in game:
        if not c.isdigit():
            game = game.replace(c, '')

    rounds = rounds.split(';')
    for round in rounds:
        values = round.split(',')
        for value in values: 
            if 'red' in value:
                for c in value:
                    if not c.isdigit():
                        value = value.replace(c, '')
                if int(value) > r_min:
                    r_min = int(value)
            elif 'blue' in value:
                for c in value:
                    if not c.isdigit():
                        value = value.replace(c, '')

                if int(value) > b_min:
                    b_min = int(value)
            else:
                for c in value:
                    if not c.isdigit():
                        value = value.replace(c, '')

                if int(value) > g_min:
                    g_min = int(value)
    print(g_min, b_min, r_min) 
    return g_min*b_min*r_min

if __name__ == "__main__":
    file = open('inputfile.txt', 'r')
    lines = file.readlines()

    sum = 0
    for line in lines:
        game = checkGame(line)

        if game != -1:
            sum += game

    print(sum)
    file.close()
