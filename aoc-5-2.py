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
    maps = list(reversed([seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]))
    final = 0
    seeds = []
    finished = 0
    
    for line in f:
        if line.strip(): # if line not empty
            if ":" in line or in_loop:
                if line.startswith("seeds:"):
                    _, seed = line.split(":")
                    seeds_temp = list(map(int, seed.split()))
                    for idx in range(0,len(seeds_temp),2):
                        seeds.append(range(seeds_temp[idx],seeds_temp[idx+1]+seeds_temp[idx]))
                        
                else:
                    if not in_loop:
                        current_map = line.split()[0].replace("-", "_")
                        in_loop = True
                        continue
                    in_loop = True
                    nums = list(map(int, line.split()))
                    exec(f"{current_map}[range({nums[0]},{nums[0]+nums[2]})] = lambda x: x - {nums[0]} + {nums[1]}")
        else:
            in_loop = False
            
    while 1:
        if not finished:
            current_state = []
            current_state.append(final)
            for current_map in maps:
                found = 0
                for key in current_map.keys():
                    if current_state[-1] in key and not found:
                        found = 1
                        current_state.append(current_map[key](current_state[-1]))
                if not found:
                    current_state.append(current_state[-1])
            print(f"Try: {final}", end="\r")
            for possible in seeds:
                if current_state[-1] in possible:
                    print()
                    print(f"{final}")
                    finished = 1
            final += 1
        else:
            break