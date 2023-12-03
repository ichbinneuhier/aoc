def get_power(game_stat):
    return game_stat["red"]*game_stat["green"]*game_stat["blue"]

with open("aoc-2-input.txt") as f:
    final = 0
    colors = ["red", "green", "blue"]
    for line in f:
        game_stat = {
        "id": None,
        "red": 0,
        "green": 0,
        "blue": 0
        }
        first, second = line.split(":")
        game_stat["id"] = int(first[5:])
        
        reveals = second.split(";")
        for reveal in reveals:
            information = reveal.split(",")
            for info in information:
                for color in colors:
                    if color in info:
                        amount = int(info.replace(color, ""))
                        if amount > game_stat[color]:
                            game_stat[color] = amount
        
        final += get_power(game_stat)
    print(final)