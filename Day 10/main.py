import time

'''
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; th
'''

def getPossibleNeighbours(map, pos):
    x,y = pos
    neighbours = []
    if x<len(map[y])-1:
        right = map[y][x+1]
        if right in '-7J':
            if 
            neighbours.append((x+1, y))
    if x>0:
        left = map[y][x-1]
        if left in '-LF':
            neighbours.append((x-1, y))
    if y>0:
        up = map[y-1][x]
        if up in '|7F':
            neighbours.append((x, y-1))
    if y<len(map)-1:
        down = map[y+1][x]
        if down in '|LJ':
            neighbours.append((x, y+1))

    return neighbours

def move(map, prev_pos, pos):
    x,y = pos
    prev_x, prev_y = prev_pos
    if map[y][x] == '|':
        if prev_y > y: # moving south
            return (x, y+1)
        else: # moving north
            return (x, y-1)
    elif map[y][x] == '-':
        if prev_x > x: # moving west
            return (x-1, y)
        else: # moving east
            return (x+1, y)
    elif map[y][x] == 'L':
        if prev_y < y: # moving east
            return (x+1, y)
        else: # moving north
            return (x, y-1)
    elif map[y][x] == 'J':
        if prev_y < y: # moving west
            return (x-1, y)
        else: # moving north
            return (x, y-1)
    elif map[y][x] == '7':
        if prev_y < y: # moving south
            return (x, y+1)
        else: # moving west
            return (x-1, y)
    elif map[y][x] == 'F':
        if prev_y > y: # moving east
            return (x+1, y)
        else: # moving south
            return (x, y+1)
    else:
        return None
    

def main():
    with open("Day 10/input.txt") as f:
        lines = f.readlines()

    map = []
    for line in lines:
        map.append(list(line.strip()))
    
    # find S
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'S':
                start = (x, y)
                break
    
    # find the path
    prev_pos = None
    pos = start
    path = []
    while True:
        neighbours = getPossibleNeighbours(map, pos)
        for neighbour in neighbours:
            if neighbour != prev_pos:
                prev_pos = pos
                pos = neighbour
                path.append(pos)
                break
        else:
            break
            
    print(path)


if __name__ == '__main__':
    main()
