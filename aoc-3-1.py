def is_valid(entry, symbol_map): # (column, row(start), length, number)
    column, row, length, number = entry
    possible_pos = []
    """
    ..XXXXXX..  column -1 -> row -1 .. row+length +1
    ..XxxxxX..  row -1 & row+length +1
    ..XXXXXX..  column +1 -> row -1 .. row+length +1
    """
    possible_pos.append((column, row-1))
    possible_pos.append((column, row+length))
    for i in range(row-1, row+length+1):
        possible_pos.append((column-1, i))
        possible_pos.append((column+1, i))
        
    for pos_pos in possible_pos:
        if pos_pos in symbol_map:
            return True
    return False
with open("aoc-3-input.txt") as f:
    map_list = [] # (column, row(start), length, number)
    symbol_map = [] # (column, row)
    column_counter = 0
    final = 0
    for line in f:
        line = line.strip()
        row_counter = 0
        number = ""
        for char in line:
            if char == ".":
                if number != "":
                    map_list.append((column_counter, row_counter-len(number), len(number), int(number)))
                    number = ""
            else:
                try:
                    number += str(int(char))
                except ValueError:
                    symbol_map.append((column_counter, row_counter))
                    if number != "":
                        map_list.append((column_counter, row_counter-len(number), len(number), int(number)))
                        number = ""
            row_counter += 1 
        if number != "":
            map_list.append((column_counter, row_counter-len(number), len(number), int(number)))
        column_counter += 1
    for entry in map_list:
        if is_valid(entry, symbol_map):
            final += entry[-1]
    print(final)
            