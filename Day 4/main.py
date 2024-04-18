import copy

def main():
    with open('Day 4/input.txt') as f:
        lines = f.read().splitlines()

    total = 0

    repeat = {}

    totalCards = 0

    for lineNum, line in enumerate(lines):
        
        line = line.split(' | ')
        goodNums = line[0].split(": ")[1].split(" ")
        haveNums = line[1].split(" ")
        goodNums = [x.strip() for x in goodNums if x != '']
        haveNums = [x.strip() for x in haveNums if x != '']

        nums = [x for x in goodNums if x in haveNums]
        
        totalCards += 1
        cardNum = lineNum + 1
        if nums:
            for i in range(1,len(nums)+1):
                if cardNum + i in repeat:
                    repeat[cardNum+i] += 1
                else:
                    repeat[cardNum+i] = 1

        if cardNum in repeat:
            for i in range(repeat[cardNum]):
                totalCards += 1
                if nums:
                    for i in range(1,len(nums)+1):
                        if cardNum + i in repeat:
                            repeat[cardNum+i] += 1
                        else:
                            repeat[cardNum+i] = 1

        # print(totalCards)

        # part 1
        # if nums:
            # total += 2**(len(nums)-1)

    # print(total)
    print(totalCards)

if __name__ == '__main__':
    main()