file = open("input_04.txt", "r")
input = file.read()
file.close()

input = input.splitlines()

def coord_is_valid(x_length, y_length, new_x, new_y):
  if (new_x < 0 or new_x >= x_length or new_y < 0 or new_y >= y_length):
      return False
  return True

dx = [0, 1, 1,  1,  0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1,  0,  1]

def get_accessible(paper_input):
    accessible = []
    for y in range(0, len(paper_input)):
        for x in range(0, len(paper_input[y])):
            if(paper_input[y][x] != '@'):
                continue

            free_spaces = 0
            for i in range(0,8):
                x_val = x + dx[i]
                y_val = y + dy[i]

                if(coord_is_valid(len(paper_input[y]), len(paper_input), x_val, y_val)):
                    candidate = paper_input[y + dy[i]][x + dx[i]]
                    if(candidate == '.'):
                        free_spaces += 1
                else:
                    free_spaces += 1

            if(free_spaces > 4):
                accessible.append([y,x])
            
    return accessible

def remove_paper(paper_input: list[str]):
    output = paper_input

    accessible_rolls = get_accessible(paper_input)
    for roll in accessible_rolls:
        l = list(paper_input[roll[0]])
        l[roll[1]] = '.'
        output[roll[0]] = "".join(l)
            
    return paper_input

# part 1 = 1518

num_accessible = len(get_accessible(input))
print(num_accessible)

sum = 0
while(num_accessible > 0):
    num_accessible = len(get_accessible(input)) 
    sum += num_accessible
    input = remove_paper(input)

# for row in input:
#     print(f"{row}\n")

# part 2 = 8665
print(sum)