import re

lines = open('./day12/input.txt', 'r').readlines()

pattern_match = re.compile("([\.#\?]+) (.+)")

# recursively try to get the number of combinations possible
# it is assumed that there are no # characters immediately before records
# optimized in a principle of dynamic programming
def get_possible_combinations(records: str, checksum: list[int], memo, prefix = ''):

    dot_count = len(records) - len(records.lstrip('.'))
    prefix += records[:dot_count]
    records = records.lstrip('.')
    
    key = (records, tuple(checksum))
    if key in memo:
        return memo[key]

    # print("Trying " + records + "; " + str(checksum))

    # no more groups to find
    if len(checksum) == 0:
        # still intact springs that were not accounted by checksum => invalid
        if records.count('#') > 0:
            return 0
        # otherwise it's a valid result
        else:
            # print(prefix + records)
            return 1
    
    # still required springs in checksum but no more records => invalid
    if len(records) == 0:
        return 0
    
    if records[0:checksum[0]].count('#') == checksum[0]:
        # if checksum[0] >= len(records):
        #     # recursive call to make sure everything is done in a valid state
        #     return get_possible_combinations(records[(checksum[0] + 1):], checksum[1:], prefix + records[:checksum[0]])
        
        # too long sequence of # => invalid
        if records[checksum[0]:checksum[0]+1] == '#':
            return 0
        # recursive call skipping next character due to it having to be a . (even if it's ?)
        else:
            return get_possible_combinations(records[(checksum[0] + 1):], checksum[1:], memo, prefix + records[:checksum[0]] + '.')

    next_unknown = records[0:checksum[0]].find('?')

    # invalid state
    if next_unknown == -1:
        return 0
    
    option_operational = records[:next_unknown] + '#' + records[next_unknown + 1:]
    option_damaged = records[:next_unknown] + '.' + records[next_unknown + 1:]

    result = get_possible_combinations(option_damaged, checksum, memo, prefix) + get_possible_combinations(option_operational, checksum, memo, prefix)
    memo[key] = result
    return result

def is_valid(records: str, checksum: list[int]):
    while len(records) > 0 and len(checksum) > 0:
        records = records.lstrip('.')
        if records[:checksum[0]].count('#') < checksum[0]:
            return False
        if records[checksum[0]:checksum[0] + 1] == '#':
            return False
        records = records[checksum[0] + 1:]
        checksum = checksum[1:]
    records = records.lstrip('.')
    
    if len(records) == 0 and len(checksum) == 0:
        return True
    else:
        return False


def get_possible_combinations_bruteforce(records: str, checksum: list[int]):
    if records.count('?') == 0:
        return 1 if is_valid(records, checksum) else 0
    
    next_unknown = records.find('?')
    
    option_operational = records[:next_unknown] + '#' + records[next_unknown + 1:]
    option_damaged = records[:next_unknown] + '.' + records[next_unknown + 1:]

    return get_possible_combinations_bruteforce(option_operational, checksum) + get_possible_combinations_bruteforce(option_damaged, checksum)

def part1():
    sum = 0
    for line in lines:
        match_result = pattern_match.match(line)
        records = match_result.group(1)
        checksum = [int(x) for x in match_result.group(2).split(',')]
        # combinations_bruteforce = get_possible_combinations_bruteforce(records, checksum)
        combinations = get_possible_combinations(records, checksum, dict())
        sum += combinations
        
        # if(combinations_bruteforce != combinations):
        #     print(line.strip() + ' - ' + str(combinations) + ' should be ' + str(combinations_bruteforce))

    print("Part 1: " + str(sum))

def part2():
    sum = 0
    repeat_count = 5
    for line in lines:
        match_result = pattern_match.match(line)
        records = match_result.group(1)
        records = '?'.join([records] * repeat_count)
        checksum = [int(x) for x in match_result.group(2).split(',')]
        checksum = checksum * repeat_count
        combinations = get_possible_combinations(records, checksum, dict())
        # print(f'{line.strip()} - {combinations}')
        sum += combinations
    print("Part 2: " + str(sum))

part1()
part2()