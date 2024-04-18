def checkCurrs(currs):
    for curr in currs:
        if curr[-1] != "Z":
            return False
    return True

def main():
    with open("Day 8/input.txt") as f:
        data = f.read().splitlines()

    dictThing = {}
    instructions = list(data[0])
    for line in data[2:]:
        line = line.split(" = ")
        otherThing = line[1].split(", ")
        dictThing[line[0]] = (otherThing[0][1:], otherThing[1][:-1])


    # part 1
    # curr = "AAA"
    # i = 0
    # steps = 0
    # while curr != "ZZZ":
    #     if i >= len(instructions):
    #         i = 0
    #     if instructions[i] == "L":
    #         curr = dictThing[curr][0]
    #     elif instructions[i] == "R":
    #         curr = dictThing[curr][1]
    #     i += 1
    #     steps += 1
    # print(steps)

    # part 2
    currs = []

    for key in dictThing.keys():
        if key[-1] == "A":
            currs.append(key)

    i = 0
    steps = 0
    numInsturctions = len(instructions)
    numCurrs = len(currs)
    
    while not checkCurrs(currs):
        print(steps)
        if instructions[i] == "L":
            for j in range(numCurrs):
                currs[j] = dictThing[currs[j]][0]
        elif instructions[i] == "R":
            for j in range(numCurrs):
                currs[j] = dictThing[currs[j]][1]
        i = (i + 1) % numInsturctions
        steps += 1

    print(steps)


if __name__ == "__main__":
    main()