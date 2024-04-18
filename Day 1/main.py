with open("Day 1/input.txt") as f:
    lines = f.readlines()

def isNum(s,i,line):
    if s.isnumeric():
        return str(s)
    elif s == "o":
        if line[i:i+3] == "one":
            return "1"
    elif s == "t":
        if line[i:i+3] == "two":
            return "2"
        elif line[i:i+5] == "three":
            return "3"
    elif s == "f":
        if line[i:i+4] == "four":
            return "4"
        elif line[i:i+4] == "five":
            return "5"
    elif s == "s":
        if line[i:i+3] == "six":
            return "6"
        elif line[i:i+5] == "seven":
            return "7"
    elif s == "e":
        if line[i:i+5] == "eight":
            return "8"
    elif s == "n":
        if line[i:i+4] == "nine":
            return "9"
    return False

total = 0

for line in lines:
    n = ""
    for i,char in enumerate(line):
        a = isNum(char,i,line)
        if a:
            n += a
            break

    lastn = n
    for k,char in enumerate(line):
        a = isNum(char,k,line)
        if a:
            lastn = a

    n += lastn
    total += int(n)

print(total)