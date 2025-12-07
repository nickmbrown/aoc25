file = open("input_05.txt", "r")
input = file.read()
file.close()

def get_ranges(ranges: list[str]):
    new_ranges = []
    for fresh_range in ranges:
        range_start = int(fresh_range.split('-')[0])
        range_end = int(fresh_range.split('-')[1])
        new_ranges.append([range_start, range_end])
    return new_ranges

fresh_ranges = input.split('\n\n')[0].split('\n')
available_ingredients = input.split('\n\n')[1].split('\n')
fresh_ranges = get_ranges(fresh_ranges)

def get_num_available_fresh():
    num_fresh = 0
    for ingredient in available_ingredients:
        for range in fresh_ranges:
            id = int(ingredient)

            if id <= range[1] + 1 and id >= range[0]:
                num_fresh += 1
                break
    return num_fresh

def has_overlap(ranges: list):
    for val in ranges:
        for other_val in ranges:
            start_in_range = other_val[0] <= val[0]  <= other_val[1]
            end_in_range = other_val[0] <= val[1] <= other_val[1]
            if(val == other_val):
                continue
            # print(f"{val[0]} - {start_in_range}, {val[1]} - {end_in_range}, {other_val}, {val}")
            if ((start_in_range or end_in_range)):
                # print(f"overlap {ranges}")
                return True
            
    # print(f"no overlap {ranges}")
    return False

def cull_identicals(ranges):
    new_ranges = []
    for val in ranges:
        if val not in new_ranges:
            new_ranges.append(val)
    
    return new_ranges

def get_ranges_without_overlap(id_ranges: list):
    new_ranges = []
    new_ranges.append(id_ranges[0])
    for other_id_range in id_ranges:
        updated = False
        for id_range in id_ranges:
            start_in_range = other_id_range[0] <= id_range[0]  <= other_id_range[1]
            end_in_range = other_id_range[0] <= id_range[1] <= other_id_range[1]

            # print(f"{fresh_range[0]} - {start_in_range}, {fresh_range[1]} - {end_in_range}, {new_range}")
            if(id_range == other_id_range):
                continue

            if start_in_range:
                id_range[0] = min(id_range[0], other_id_range[0])
                updated = True
            if end_in_range:
                id_range[1] = max(id_range[1], other_id_range[1])
                updated = True
            if(updated):
                new_ranges.append(id_range)
                break
        if(not updated):
            new_ranges.append(id_range)

    # print(f"new: {new_ranges}")
    return new_ranges

def get_num_possible_fresh():
    num_fresh = 0
    ranges_no_overlap = cull_identicals(fresh_ranges)

    # print(f"ranges_no_overlap {ranges_no_overlap}")    

    while(has_overlap(ranges_no_overlap)):
        ranges_no_overlap = get_ranges_without_overlap(ranges_no_overlap)

    print(f"ranges_no_overlap {cull_identicals(ranges_no_overlap)}")

    for fresh_range in cull_identicals(ranges_no_overlap):
        num_fresh += fresh_range[1] - fresh_range[0] + 1
    return num_fresh


# part 1 = 674
# print(get_num_available_fresh())



# part 2 = 
print(get_num_possible_fresh())
# 381752921180592, too high
# 355648227273757, too high
# 19538543375891, too low