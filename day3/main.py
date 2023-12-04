import re

input_file = open('input.txt', 'r')
lines = input_file.readlines()

lines = [line.rstrip() + '.' for line in lines]

def part1():
    sum = 0

    for line_number, line in enumerate(lines):
        number_start = None
        search_index = 0
        while search_index < len(line):
            # find digit sequences
            if line[search_index].isdigit():
                if number_start == None:
                    number_start = search_index
            # on end of digit sequence parse number
            elif number_start != None:
                number_string = line[number_start:search_index]
                is_valid_machine_label = False
                # check if the number string is next to any other special character
                for line_number_check_index in range(max(0, line_number - 1), min(len(lines), line_number + 2)):
                    for line_position_check_index in range(max(0, number_start - 1), min(len(line), search_index + 1)):
                        char_to_check = lines[line_number_check_index][line_position_check_index]
                        if not char_to_check.isdigit() and char_to_check != '.':
                            is_valid_machine_label = True
                            # could fast exit here
                if is_valid_machine_label:
                    number = int(number_string)
                    sum += number
                # reset number_start after we are done to find beginning of next number
                number_start = None

            # in any case increment to step to the next character in line
            search_index += 1

    print('Part 1: ' + str(sum))

def part2():
    gear_candidates = dict()

    for line_number, line in enumerate(lines):
        number_start = None
        search_index = 0
        while search_index < len(line):
            # find digit sequences
            if line[search_index].isdigit():
                if number_start == None:
                    number_start = search_index
            # on end of digit sequence parse number
            elif number_start != None:
                number_string = line[number_start:search_index]
                is_valid_machine_label = False
                # check if the number string is next to any other special character
                for line_number_check_index in range(max(0, line_number - 1), min(len(lines), line_number + 2)):
                    for line_position_check_index in range(max(0, number_start - 1), min(len(line), search_index + 1)):
                        char_to_check = lines[line_number_check_index][line_position_check_index]
                        if char_to_check == '*':
                            gear_candidate_position = (line_number_check_index, line_position_check_index)
                            if not gear_candidate_position in gear_candidates:
                                gear_candidates[gear_candidate_position] = []
                            gear_candidates[gear_candidate_position].append(int(number_string))
                            # don't fast exit now since a number could belong to to * characters
                
                # reset number_start after we are done to find beginning of next number
                number_start = None

            # in any case increment to step to the next character in line
            search_index += 1

    sum = 0
    for x in gear_candidates.values():
        if len(x) != 2:
            continue
        sum += x[0] * x[1]

    print('Part 2: ' + str(sum))

part1()
part2()