with open("aoc-4-input.txt") as f:
    final = 0
    for line in f:
        win_num = []
        actual_num = []
        _, data = line.split(":")
        winning, actual = data.split("|")
        
        for number in winning.split(" "):
            if number:
                win_num.append(int(number))
                
        for number in actual.split(" "):
            if number:
                actual_num.append(int(number))
        
        win_num = set(win_num)
        actual_num = set(actual_num)
        intersect = list(win_num.intersection(actual_num))
        if intersect:
            final += 2**(len(intersect)-1)
    print(final)