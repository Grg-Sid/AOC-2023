import re


def card_count(line) -> int:
    count = 0
    game = line.split(":")[1].split("|")
    winning_cards = game[0].split()
    my_cards = game[1].split()

    for card in my_cards:
        if card in winning_cards:
            count += 1

    return count


with open("./input.txt") as input_file:
    ans = 0
    data = input_file.read().splitlines()
    for id, line in zip(range(len(data)), data):
        x = card_count(line) - 1
        if x >= 0:
            print(x)
            ans += 2**x

    print(ans)
