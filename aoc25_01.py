import math

def GetTimesPassedZero(prev, rotation):

    times = 0
    new = prev + rotation
    untilZero = 0

    # going left
    if(rotation < 0 and new < 0):
        untilZero = prev
        rotationAfterPassing = abs(rotation) - untilZero
        times = math.floor((rotationAfterPassing)/100) + 1

    # going right
    elif(rotation > 0 and new > 99):
        untilZero = 100 - prev
        rotationAfterPassing = abs(rotation) - untilZero
        times = math.floor((rotationAfterPassing)/100) + 1

    if(untilZero == 0):
        times -= 1
    return times

def Unlock(input, val):
    counter = 0

    for line in input:
        prev = val
        rotation = -int(line[1:]) if line[0] == 'L' else int(line[1:])
        val = (prev + rotation) % 100
        timesPassedZero = GetTimesPassedZero(prev, rotation)

        # landed on zero
        if(val == 0):
            counter += 1
            timesPassedZero -= 1

        if(prev == 0 and timesPassedZero < 1):
            continue
        elif(timesPassedZero > 0):
            counter += timesPassedZero
        
    # Part 1: 1180
    # Part 2: 6892
    print("Total: " + str(counter)) 
    return counter


file = open("input_01.txt", "r")
input = file.read()
file.close()

input = input.splitlines()

# assert Unlock(["L100"], 50) == 1
# print("\n")
# assert Unlock(["L150"], 50) == 2
# print("\n")
# assert Unlock(["R150"], 50) == 2
# print("\n")
# assert  Unlock(["R200"], 0) == 2
# print("\n")
# assert  Unlock(["L200"], 0) == 2
# print("\n")
# assert Unlock(["R1000"], 50) == 10
# print("\n\n")
# assert Unlock(["L82"], 14) == 1
# print("\n\n")
# assert Unlock(["R50"], 0) == 0
# print("\n\n")
# assert Unlock(["L50"], 0) == 0
# print("\n\n")

# assert Unlock(input, 50) == 6
assert Unlock(input, 50) == 6892


print("SUCCESSS")