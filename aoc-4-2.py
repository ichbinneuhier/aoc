with open("aoc-4-input.txt") as f:
    final = 0
    pile = {}
    max_game_num = 0
    for line in f:
        win_num = []
        actual_num = []
        game, data = line.split(":")
        game_num = int(game[5:])
        max_game_num = game_num
        pile[game_num] = pile.setdefault(game_num, 0)+1
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
            for i in range(1,len(intersect)+1):
                pile[game_num+i] = pile.setdefault(game_num+i, 0)+pile[game_num]
    for game_num, num in pile.items():
        if game_num <= max_game_num:
            final += num
    print(final)