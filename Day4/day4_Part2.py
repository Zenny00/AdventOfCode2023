def checkNumbers(line):
    card_number = int(line.split(': ')[0][5:])
    # Split on the card number and take the numbers
    numbers = line.split(': ')[1]
    numbers = numbers.split(' | ')
    winning_numbers = [x for x in numbers[0].split(' ') if x != '']
    card_numbers = [x for x in numbers[1].split(' ') if x != '']

    matching_numbers = 0
    for number in card_numbers:
        if number in winning_numbers:
            matching_numbers += 1

    return matching_numbers, card_number

if __name__ == "__main__":
    file = open('inputfile_1.txt', 'r')
    lines = file.read().splitlines()

    card_sum = 0

    cards = []

    for line in lines:
        cards.append(line)

    for card in cards:
        num, card_num = checkNumbers(card)
        for i in range(card_num, card_num+num):
            cards.append(cards[i])

    print(len(cards))
    file.close()
