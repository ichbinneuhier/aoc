with open("test.txt") as f:
    for line in f:
        if line.strip(): # if line not empty
            map_type, data = line.split(":")
            # todo
            # dict = {range(): function(source->dest)}