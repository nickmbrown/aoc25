def part_one(input):
    invalids_sum = 0
    for id_range in input:
        split = id_range.split('-')
        start = int(split[0])
        end = int(split[1])
        for id in range(start, end + 1):
            id_string = str(id)
            id_length = len(id_string) 
            if(id_length % 2 != 0):
                continue
            front = id_string[0:id_length//2]
            back = id_string[id_length//2:]

            if(front == back):
                invalids_sum += id


    print(invalids_sum)

def part_two(input):
    invalid_sums = 0
    for id_range in input:
        split = id_range.split('-')
        start = int(split[0])
        end = int(split[1])
        for id in range(start, end + 1):
            s = str(id)
            # clever slicing technique from https://www.geeksforgeeks.org/python/python-check-if-string-repeats-itself/
            if(s in (s + s)[1:-1]):
                invalid_sums += id
            continue
    print(invalid_sums)

file = open("input_02.txt", "r")
input = file.read()
file.close()

input = input.split(',')

# part 1 = 52316131093
part_one(input)

# part 2 = 69564213293
part_two(input)
