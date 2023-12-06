def get_bounds(race_stat):
    time, distance = race_stat
    possible = 0
    for held_down in range(time+1):
        total_distance = (time-held_down) * held_down
        if total_distance > distance:
            possible += 1
    return possible
    
with open("aoc-6-input.txt") as f:
    time = None
    distance = None
    final = 1
    
    for line in f:
        if line.startswith("Time"):
            _, data = line.split(":")
            data = data.replace(" ", "").replace("\t", "").replace("\n", "")
            time = int(data)
        if line.startswith("Distance"):
            _, data = line.split(":")
            data = data.replace(" ", "").replace("\t", "").replace("\n", "")
            distance = int(data)
            
    final *= get_bounds((time,distance))
    
    print(final)
    