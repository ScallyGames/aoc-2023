import re

input_file = open('input.txt', 'r')
lines = input_file.readlines()


def part1():
    sum = 0
    for line in lines:
        first_digit = None
        last_digit = None
        for char in line:
            if(char.isdigit()):
                if first_digit is None:
                    first_digit = char
                last_digit = char
        if(first_digit is not None and last_digit is not None):
            digit_string = first_digit + last_digit
            sum += int(digit_string)
    print('Part 1: ' + str(sum))

def part2():
    sum = 0

    digit_strings = {
        ('zero', '0'),
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9'),
    }
    for line in lines:
        first_digit = None
        last_digit = None
        for i in range(len(line)):
            if first_digit is None:
                if(line[i].isdigit()):
                        first_digit = line[i]
                for pattern, digit in digit_strings:
                    if line[i:i+len(pattern)] == pattern:
                        first_digit = digit
        for i in reversed(range(len(line))):
            if last_digit is None:
                if(line[i].isdigit()):
                    last_digit = line[i]
                for pattern, digit in digit_strings:
                    if line[i:i+len(pattern)] == pattern:
                        last_digit = digit

        
        if(first_digit is not None and last_digit is not None):
            digit_string = first_digit + last_digit
            sum += int(digit_string)
    print('Part 2: ' + str(sum))

part1()
part2()