import sys
# strip down into x y w h 
stripped = [ x[x.index('@') + 1:].replace(':', '').replace(',', ' ').replace('x', ' ').strip().split(' ') for x in sys.stdin.readlines() ]
# now parse into (x,y) and (x', y') (wtf)
claims = [ ((int(x[0]), int(x[0]) + int(x[2])), ((int(x[1]), int(x[1]) + int(x[3])))) for x in stripped ]

claimed = {}
for c in claims:
    for x in range(c[0][0], c[0][1]):
        for y in range(c[1][0], c[1][1]):
            if (x, y) in claimed:
                claimed[(x, y)] = 1
            else: claimed[(x, y)] = 0

print(sum(claimed.values()))

#part two (ok this is very inefficient)
for c in claims:
    intact = True
    for x in range(c[0][0], c[0][1]):
        for y in range(c[1][0], c[1][1]):
            if claimed[(x,y)] == 1:
                intact = False
    if intact: 
        print(c)
        break