with open("aoc-1-input.txt") as f:
    final = 0
    number_char = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
    }
    
    for line in f:
        pos = []
        for entry in number_char.keys():
            entry_count = line.count(entry)
            start_pos = 0
            while entry_count != 0:
                try:
                    pos.append((line.index(entry, start_pos), number_char[entry]))
                    start_pos = pos[-1][0]+len(entry)
                except ValueError:
                    pass
                entry_count -= 1
        pos.sort(key=lambda x: x[0])
        print(pos)
        final += int(f"{pos[0][-1]}{pos[-1][-1]}")
    print(final)