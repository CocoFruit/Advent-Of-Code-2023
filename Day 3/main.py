def getNeighbors(x, y, arr):
    neighbors = []
    if x > 0:
        neighbors.append(arr[y][x-1])
        neighbors.append((y,x-1))
    if x < len(arr[y])-1:
        neighbors.append(arr[y][x+1])
        neighbors.append((y,x+1))
    if y > 0:
        neighbors.append(arr[y-1][x])
        neighbors.append((y-1,x))
    if y < len(arr)-1:
        neighbors.append(arr[y+1][x])
        neighbors.append((y+1,x))
    if x > 0 and y > 0:
        neighbors.append(arr[y-1][x-1])
        neighbors.append((y-1,x-1))
    if x > 0 and y < len(arr)-1:
        neighbors.append(arr[y+1][x-1])
        neighbors.append((y+1,x-1))
    if x < len(arr[y])-1 and y > 0:
        neighbors.append(arr[y-1][x+1])
        neighbors.append((y-1,x+1))
    if x < len(arr[y])-1 and y < len(arr)-1:
        neighbors.append(arr[y+1][x+1])
        neighbors.append((y+1,x+1))

    return neighbors

seenCoords = []

def getNum(x,y,arr):
    num = []
    x1 = x
    # go left
    if x1 > 0 and (y,x1): 
        while arr[x1].isnumeric() and (y,x1) not in seenCoords:
            num.insert(0,arr[x1])
            seenCoords.append((y,x1))
            x1 -= 1
        
    # go right
    x1 = x+1
    if x1 < len(arr)-1 and (y,x1):
        try:
            while arr[x1].isnumeric() and (y,x1) not in seenCoords:
                num.append(arr[x1])
                seenCoords.append((y,x1))
                x1 += 1
        except:
            pass

    num = "".join(num)
    return num

def main():
    with open("Day 3/input.txt", "r") as f:
        lines = f.readlines()

    lineArr = []
    for line in lines:
        lineArr.append(line.strip())
    
    total = 0

    for y,line in enumerate(lineArr):
        for x,char in enumerate(line):
            if char != "." and not char.isnumeric(): # is symbol
                numbers = []
                neighbors = getNeighbors(x,y,lineArr)
                for n,neighbor in enumerate(neighbors):
                    if type(neighbor) != tuple and neighbor.isnumeric():
                        neighborY, neighborX = neighbors[n+1]
                        num = getNum(neighborX, neighborY, lineArr[neighborY])
                        if num:
                            numbers.append(int(num))
                if len(numbers) == 2:
                    total += numbers[0] * numbers[1]
    print(total)

if __name__ == "__main__":
    main()