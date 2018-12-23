inp = 1723

def power(x: int, y: int):
    i = x + 10
    return (((((i * y) + inp) * i) // 100) % 10) - 5

def power_square(x: int, y: int, s: int, cells):
    total = 0
    for i in range(s):
        for j in range(s):
            total += cells.get((x + i, y + j, s)) or 0
    return total

cells = { (i, j, s): power(i, j) for i in range(1, 298) for j in range(1, 298) for s in range(3, 30) }

best = -1
for s in range(3, 30):
    print('Trying size {}...'.format(s))
    for i in range(1, 298):
        for j in range(1, 298):
            if 300 < i + s or 300 < j + s:
                continue
            p = power_square(i, j, s, cells)
            if p > best:
                best = p
                print('New max power {} found at {}'.format(p, (i, j, s)))
