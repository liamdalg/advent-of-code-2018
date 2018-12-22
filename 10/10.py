import sys

class Point():

    def __init__(self, x, y, dx, dy):
        self.pos = (int(x), int(y))
        self.vel = (int(dx), int(dy))

    def __repr__(self):
        return 'Point({}, {}, {}, {})'.format(*self.pos, *self.vel)

def parse(x: str) -> Point:
    voff = x.find('vel')
    px = x[x.find('<') + 1:x.find(',')]
    py = x[x.find(',') + 1:x.find('>')]
    vx = x[x.find('<', voff) + 1:x.find(',', voff)]
    vy = x[x.find(',', voff) + 1:x.find('>', voff)]
    return Point(px, py, vx, vy)

def bounds(points: [Point]) -> ((int, int), (int, int)):
    tl = min(points, key=lambda x: x.pos[0]).pos[0], min(points, key=lambda x: x.pos[1]).pos[1]
    br = max(points, key=lambda x: x.pos[0]).pos[0], max(points, key=lambda x: x.pos[1]).pos[1]
    return (tl, br)

def smallest_area(points: [Point]) -> int:
    top_left, bot_right = bounds(points)
    return (bot_right[0] - top_left[0] + 1) * (bot_right[1] - top_left[1] + 1)

def print_sky(points: [Point]):
    top_left, bot_right = bounds(points)
    w, h = (bot_right[0] - top_left[0] + 1), (bot_right[1] - top_left[1] + 1)
    sky = ''
    for y in range(h):
        for x in range(w): 
            if any([ p.pos == (x + top_left[0], y + top_left[1]) for p in points ]):
                sky += '#'
            else: sky += '.'
        sky += '\n'
    print(sky)

def advance(points: [Point]):
    for x in points:
        x.pos = ((x.pos[0] + x.vel[0]), x.pos[1] + x.vel[1])

with open('input.txt') as f:
    points = [ parse(x) for x in f.readlines() ]

found = False
press = False
time = 1
while not found:
    advance(points)
    closeness = smallest_area(points)
    if closeness < 1000:
        press = True
        print('Possible word found, time: {}, closeness: {}\nPress p to print'.format(time, closeness))
    else: press = False
    if press:
        ans = input()
        if ans == 'p':
            print_sky(points)
        found = ans == 'q'
    time += 1