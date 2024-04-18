def main():
    with open("Day 6/input.txt") as f:
        lines = f.read().splitlines()

    times = lines[0].split(": ")[1].strip().split(" ")
    times = [int(time) for time in times  if time.isnumeric()]
    distances = lines[1].split(": ")[1].strip().split(" ")
    distances = [int(distance) for distance in distances if distance.isnumeric()]

    time = int("".join([str(t) for t in times]))    
    distance = int("".join(str(d) for d in distances))

    waysToWin = 0
    for heldTime in range(time):
        distanceGone = (time - heldTime) * heldTime
        if distanceGone > distance:
            waysToWin += 1
    print(waysToWin)
    input()
    allWaysToWin = 1
    for i in range(len(times)):
        waysToWin = 0

        timeLasted = times[i]
        distance = distances[i]

        for heldTime in range(timeLasted):
            distanceGone = (timeLasted - heldTime) * heldTime
            if distanceGone > distance:
                waysToWin += 1
        allWaysToWin *= waysToWin

    print(allWaysToWin)
    
if __name__ == "__main__":
    main()