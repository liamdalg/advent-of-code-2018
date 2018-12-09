import sys
# part one
items = [ x[:-1] for x in sys.stdin.readlines() ]
count = [0, 0]

for i in items:
    occurences = { i.count(x) for x in i if i.count(x) == 2 or i.count(x) == 3 }
    for o in occurences:
        count[o - 2] += 1

prod = count[0] * count[1]
print(prod)

#part two
def dist(a: str, b: str) -> int:
    d = 0
    for x in zip(a,b):
        if x[0] != x[1]:
            d += 1
    return d

for x in items:
    for y in items:
        if dist(x, y) == 1:
            print('Found {}, {}!'.format(x, y))
            print('Diff: ' + ''.join([ x[0] for x in zip(x, y) if x[0] == x[1] ]))
            exit()