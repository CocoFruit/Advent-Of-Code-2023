def main():
    with open('Day 2/input.txt') as f:
        lines = f.readlines()
    
    # bag = {"red":12,"green":13,"blue":14}

    # goodGames = 0
    powerSum = 0
    # game = 0
    for line in lines:
        line = line.strip()

        # game += 1

        line = line.replace(";", ",")

        minBag = {"red":0,"green":0,"blue":0}

        line = line.split(": ")[1].split(", ")
        # bad = True
        for thing in line:
            thing = thing.split(" ")
            num = int(thing[0])
            color = thing[1]

            if minBag[color] < num:
                minBag[color] = num

            # if bag[color] < num:
            #     bad = False
            #     break
        
        power = minBag["red"] * minBag["green"] * minBag["blue"]
        powerSum += power
        # if bad:
        #     goodGames += int(game)

    print(powerSum)
    
    # print(goodGames)

        
if __name__ == '__main__':
    main()