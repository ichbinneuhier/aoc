with open("aoc-1-input.txt") as f:
    final = 0
    for line in f:
        numbers = []
        for char in line:
            try:
                numbers.append(int(char))
            except ValueError:
                pass
        final += int(f"{numbers[0]}{numbers[-1]}")
    print(final)