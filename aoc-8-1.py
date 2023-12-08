with open("aoc-8-input.txt") as f:
    graph = {}
    start = "AAA"
    finish = "ZZZ"
    pos = start
    steps = 0
    finished = False
    
    for line in f:
        if line.strip():
            if "=" not in line:
                route = line.strip()
            else:
                node, neighbours = line.split(" = ")
                neighbours = neighbours.replace("(", "(\"").replace(",", "\",").replace(" ", " \"").replace(")", "\")")
                exec(f"neighbours = {neighbours}")
                graph[node] = neighbours
        else:
            pass
    while not finished:
        for char in route:
            if char == "L":
                pos = graph[pos][0]
            elif char == "R":
                pos = graph[pos][1]
            else:
                print("Error")
            steps += 1
            if pos == finish:
                print(steps)
                finished = True
    