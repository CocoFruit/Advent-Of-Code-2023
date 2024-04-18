def main():
    with open("Day 9/input.txt", "r") as f: data = f.read().splitlines()
    # part 1
    total = 0
    allHistories = []
    for history in data:
        history = [int(h) for h in history.split(" ")]
        total += history[-1]-history[-2]
        allHistories.append([])
        allHistories[-1].append(history)
        while history != [0]*len(history):
            history = [r-l for l, r in zip(history, history[1:])]
            allHistories[-1].append(history)
            total += history[1]-history[0]
    # part 2
    total2 = 0
    for thing in allHistories:
        thing = thing[::-1]
        thing[0].insert(0,0)
        for i in range(1,len(thing)):
            thing[i].insert(0,thing[i][0]-thing[i-1][0])
        total2 += thing[-1][0]
    print(total,total2)
if __name__=='__main__':
    main()
