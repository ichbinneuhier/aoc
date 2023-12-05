with open("aoc-5-input.txt") as f:
    in_loop = False
    current_map = None
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}
    maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
    final = []
    
    for line in f:
        if line.strip(): # if line not empty
            if ":" in line or in_loop:
                if line.startswith("seeds:"):
                    _, seed = line.split(":")
                    seeds = list(map(int, seed.split()))
                else:
                    if not in_loop:
                        current_map = line.split()[0].replace("-", "_")
                        in_loop = True
                        continue
                    in_loop = True
                    nums = list(map(int, line.split()))
                    exec(f"{current_map}[range({nums[1]},{nums[1]+nums[2]})] = lambda x: x - {nums[1]-nums[0]}")
        else:
            in_loop = False
            
    for seed in seeds:
        curr_entry = []
        curr_entry.append(seed)
        for curr_map in maps:
            found = 0
            for key in curr_map.keys():
                if curr_entry[-1] in key and not found:
                    curr_entry.append(curr_map[key](curr_entry[-1]))
                    found = 1
            if found == 0:
                curr_entry.append(curr_entry[-1])
        final.append(curr_entry)
    print(sorted(final, key= lambda x: x[-1])[0][-1])