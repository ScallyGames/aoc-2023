import re
import math

input_file = open('input.txt', 'r')
lines = input_file.readlines()

card_match_pattern = re.compile("^Card\s*(\d+): ([^|]*)\|(.*)$")

def part1():
    sum = 0

    for line in lines:
        match_result = card_match_pattern.match(line)
        winning_numbers_sequence = match_result.group(2).strip()
        own_numbers_sequence = match_result.group(3).strip()
        winning_numbers = set([int(x) for x in winning_numbers_sequence.split(' ') if x != ''])
        own_numbers = set([int(x.strip()) for x in own_numbers_sequence.split(' ') if x != ''])
        winning_matches = own_numbers.intersection(winning_numbers)
        score = math.floor(pow(2, len(winning_matches) - 1))
        sum += score

    print('Part 1: ' + str(sum))


def part2():
    card_counts = dict()
    win_counts = dict()

    for line in lines:
        match_result = card_match_pattern.match(line)
        card_number = int(match_result.group(1))
        winning_numbers_sequence = match_result.group(2).strip()
        own_numbers_sequence = match_result.group(3).strip()
        winning_numbers = set([int(x) for x in winning_numbers_sequence.split(' ') if x != ''])
        own_numbers = set([int(x.strip()) for x in own_numbers_sequence.split(' ') if x != ''])
        winning_matches = own_numbers.intersection(winning_numbers)
        card_counts[card_number] = 1
        win_counts[card_number] = len(winning_matches)
        
    for i in range(1, len(lines) + 1):
        # print(f'Got {win_counts[i]} wins with {card_counts[i]} copies of card {i}')
        for x in range(win_counts[i]):
            # print(f'Increasing copies of card {i + x + 1}')
            card_counts[i + x + 1] += card_counts[i]

    total_card_count = sum(card_counts.values())

    print('Part 2: ' + str(total_card_count))

part1()
part2()