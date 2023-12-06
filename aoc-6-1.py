def get_bounds(race_stat):
    time, distance = race_stat
    possible = 0
    for held_down in range(time+1):
        total_distance = (time-held_down) * held_down
        if total_distance > distance:
            possible += 1
    return possible
    
with open("aoc-6-input.txt") as f:
    time = []
    distance = []
    final = 1
    
    for line in f:
        if line.startswith("Time"):
            _, data = line.split(":")
            for i in data.split():
                time.append(int(i))
        if line.startswith("Distance"):
            _, data = line.split(":")
            for i in data.split():
                distance.append(int(i))
                
    race_stats = list(zip(time,distance))
    
    for race_stat in race_stats:
        final *= get_bounds(race_stat)
    
    print(final)
    