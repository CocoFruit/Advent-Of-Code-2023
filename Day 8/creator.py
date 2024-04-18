with open("Day 8/input.txt") as f:
    data = f.read().splitlines()

with open("Day 8/thing.txt","w") as f:
    for char in data[0]:
        if char == "L":
            f.write("for j in range(numCurrs):\n\tcurrs[j] = dictThing[currs[j]][0]\n")
        elif char == "R":
            f.write("for j in range(numCurrs):\n\tcurrs[j] = dictThing[currs[j]][1]\n")

