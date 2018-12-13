import sys
from string import ascii_letters

# part one AND part two
coords = [ (int(x.split(',')[0]), int(x.split(',')[1])) for x in sys.stdin.readlines() ]

def dist(a: (int, int), b: (int, int)) -> int:
    return dist_x(a, b) + dist_y(a, b)

def dist_x(a: (int, int), b: (int, int)) -> int:
    return abs(b[0] - a[0])

def dist_y(a: (int, int), b: (int, int)) -> int:
    return abs(b[1] - a[1])

def isFinite(x: (int, int), ys: [(int, int)]) -> bool:
    left  = [ x[0] > y[0] and dist_y(y, x) <= dist_x(y, x) for y in ys if x != y ]
    right = [ x[0] < y[0] and dist_y(y, x) <= dist_x(y, x) for y in ys if x != y ]
    down  = [ x[1] < y[1] and dist_y(y, x) >= dist_x(y, x) for y in ys if x != y ]
    up    = [ x[1] > y[1] and dist_y(y, x) >= dist_x(y, x) for y in ys if x != y ]
    return any(left) and any(right) and any(down) and any(up)

max_x, max_y = max(coords, key=lambda x: x[0])[0], max(coords, key=lambda x: x[1])[1]

width = max_x
height = max_y

grid = [ '' ] * height
areas = { c: 0 for c in coords}
chars = { coords[i]: ascii_letters[i] for i in range(len(coords)) }

safe = 0
for i in range(height):
    for j in range(width):
        distances = { x: dist((j, i), x) for x in coords }
        total_dist = sum(distances.values())
        safe += 1 if total_dist < 10000 else 0
        closest = min(distances, key=distances.get)
        closest_dist = distances[closest]
        # if owned by one
        if sum(v == closest_dist for v in distances.values()) == 1:
            grid[i] += chars[closest]
            areas[closest] += 1
        else: grid[i] += '.'

finites = { k: v for (k, v) in areas.items() if isFinite(k, coords) }
max_area = max(finites, key=finites.get)
print('{}: {}'.format(max_area, areas[max_area]))
print('Safe size: {}'.format(safe))

with open('out.txt', 'w+') as f:
    for l in grid:
        f.write(''.join(l) + '\n')
