file = open("input_03.txt", "r")
input = file.read()
file.close()

input = input.splitlines()

def part_one(input):
    sum = 0
    for bank in input:
        joltage = 0
        for i, battery_1 in enumerate(bank):
            for battery_2 in range(i + 1, len(bank)):
                s = battery_1 + bank[battery_2]
                j = int(s)
                if joltage < j:
                    joltage = j
        # print(joltage)
        sum += joltage

    print(sum)

def part_two(input, depth):
    sum = 0
    for bank in input:
        bank_sum = search_bank(bank, depth)
        # print(f"{bank_sum}\n\n\n")
        sum += bank_sum


    print(sum)

def search_bank(bank, depth):
    joltage = ""
    search_val = 9
    start_index = 0
    while len(joltage) < depth:

        end_index = len(bank)-depth+len(joltage) + 1

        # print(f"{bank[start_index : end_index]}, {joltage}, searching for {search_val} in range {start_index}:{end_index}")

        for i in range(start_index, end_index):
            if(bank[i] == str(search_val)):
                joltage += bank[i]
                search_val = 10
                start_index = i + 1
                # print(f"found {bank[i]} at index {i}, {start_index}")
                break

        search_val -= 1
        if(search_val < 1):
            break

    return int(joltage)

# part 1 = 17087
part_one(input)
part_two(input, 2)

# part 2 = 169019504359949
# part_two(input, 12)