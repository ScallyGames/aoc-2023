import re

input_file = open('input.txt', 'r')
lines = input_file.readlines()

available_balls = { 'red': 12, 'green': 13, 'blue': 14 }
game_pattern = re.compile("^Game (\d+): (.*)$")
draw_pattern = re.compile("(\d+) (red|green|blue)")

def isValidGame(game_string):
    for draw in game_string.split(';'):
        draw = draw.strip() # trim whitespace
        for draw_of_type in draw.split(','):
            draw_of_type = draw_of_type.strip()
            draw_parts = draw_pattern.match(draw_of_type)
            count = int(draw_parts.group(1))
            type = draw_parts.group(2)
            if count > available_balls[type]:
                return False
    return True

def getPower(game_string):
    min_count = { 'red': 0, 'green': 0, 'blue': 0 }
    for draw in game_string.split(';'):
        draw = draw.strip() # trim whitespace
        for draw_of_type in draw.split(','):
            draw_of_type = draw_of_type.strip()
            draw_parts = draw_pattern.match(draw_of_type)
            count = int(draw_parts.group(1))
            type = draw_parts.group(2)
            min_count[type] = max(min_count[type], count)
    power = 1
    for value in min_count.values():
        power *= value
    return power    
                


def part1():
    sum = 0

    for line in lines:
        game_pattern_match = game_pattern.match(line)
        game_id_string = game_pattern_match.group(1)
        game_id = int(game_id_string)
        game_string = game_pattern_match.group(2)
        
        if isValidGame(game_string):
            sum += game_id

    print('Part 1: ' + str(sum))

def part2():
    sum = 0

    for line in lines:
        game_pattern_match = game_pattern.match(line)
        game_id_string = game_pattern_match.group(1)
        game_string = game_pattern_match.group(2)
        
        power = getPower(game_string)
        sum += power

    print('Part 2: ' + str(sum))

part1()
part2()