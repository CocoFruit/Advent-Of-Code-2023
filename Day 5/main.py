import time
import plotter

def main():
    startTime = time.time()
    with open('Day 5/input.txt') as f:
        lines = f.read().splitlines()
    
    seeds = lines[0].split(": ")[1].split(" ")

    mappings = [[]] 

    
    for line in lines[3:]:
        if line == "":
            continue
        if ":" in line:
            # new mapping
            mappings.append([])
            continue
            
        line = [int(x) for x in line.split(" ")]
        # source range
        sourceMin = line[1]
        sourceMax = line[1]+line[2]
        
        # dest range
        destMin = line[0]
        destMax = line[0]+line[2]   

        mappings[-1].append((sourceMin, sourceMax, destMin, destMax))
    
    destinations = []

    actualSeeds = [range(int(seeds[i]), int(seeds[i])+int(seeds[i+1])) for i in range(0,len(seeds),2)]
    # fullLength = sum([len(r) for r in actualSeeds])

    change = 50000

    # i = 0
    lastDest = 0

    for r in actualSeeds:
        for s in range(0,len(r),change):
            seed = r[s]
            seed = int(seed)
            ogSeed = seed

            for mapping in mappings:
                for sourceMin, sourceMax, destMin, destMax in mapping:
                    if seed >= sourceMin and seed <= sourceMax:
                        seed = destMin + (seed - sourceMin)
                        break
            # seed is now a destination
            destinations.append((ogSeed,seed))
    
    print("Done with first part")

    minDest = min(destinations, key=lambda x:x[1])
    # (2686125464, 23738616)
    destinations = []
    all_y_values = []
    i = 0
    for seed in range(minDest[0]-change, minDest[0]+change,1):
        ogSeed = seed
        y_values = []
        i += 1
        for mapping in mappings:
            for sourceMin, sourceMax, destMin, destMax in mapping:
                if seed >= sourceMin and seed <= sourceMax:
                    seed = destMin + (seed - sourceMin)
                    break
            if i % 100 == 0:
                y_values.append(seed)
         
        if y_values: all_y_values.append(y_values)
        # seed is now a destination
        destinations.append((ogSeed,seed))


    plotter.showThings(all_y_values)
    print(min(destinations, key=lambda x:x[1]))
    print(f"Found in {time.time()-startTime} seconds")
    

if __name__ == '__main__':
    main()
