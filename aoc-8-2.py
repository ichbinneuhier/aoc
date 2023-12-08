import math

with open("aoc-8-input.txt") as f:
    graph = {}
    starts = []
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
    
    for key in graph.keys():
        if key[-1] == "A":
            starts.append(key)
          
    step_map = [None for i in starts]
    
    while not all(step_map):
        for char in route:
            steps += 1
            for idx, elem in enumerate(starts):
                if char == "L":
                    starts[idx] = graph[elem][0]
                else:
                    starts[idx] = graph[elem][1]
            for elem in starts:
                if elem[-1] == "Z":
                    step_map[starts.index(elem)] = steps
                    
    def lcm(a, b):
        return abs(a*b) // math.gcd(a, b)
    
    lcm_val = 1
    for i in step_map:
        lcm_val = lcm(lcm_val,i)
    print(lcm_val)