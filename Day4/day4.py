def checkNumbers(line):
    # Split on the card number and take the numbers
    numbers = line.split(': ')[1]
    numbers = numbers.split(' | ')
    winning_numbers = [x for x in numbers[0].split(' ') if x != '']
    card_numbers = [x for x in numbers[1].split(' ') if x != '']

    points = 0
    for number in card_numbers:
        if number in winning_numbers and points == 0:
            points = 1
        elif number in winning_numbers:
            points *= 2

    return points

if __name__ == "__main__":
    file = open('inputfile_1.txt', 'r')
    lines = file.read().splitlines()

    card_sum = 0
    for line in lines:
        card_sum += checkNumbers(line)

    print(card_sum)
    file.close()
