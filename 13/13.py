import sys

class Cart():

    def __init__(self, dir, x, y):
        self.dir = dir
        self.turn_pref = 0
        self.should_move = True
        self.x = x
        self.y = y

    def move(self):
        if self.should_move:
            self.x += self.dir[0]
            self.y += self.dir[1]

    def turn(self):
        if self.turn_pref == 2:
            self.turnRight()
        elif self.turn_pref == 0: 
            self.turnLeft()
        self.turn_pref = (self.turn_pref + 1) % 3
    
    def turnRight(self):
        self.dir = (-self.dir[1], self.dir[0])

    def turnLeft(self):
        self.dir = (self.dir[1], -self.dir[0])

    def __repr__(self):
        return 'Cart({}, {}, {})'.format(self.dir, self.x, self.y)


directions = { '^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0) }
print(directions)

grid = [ x.replace('\n', '') for x in sys.stdin.readlines() ] 
carts = []
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val in directions:
            carts.append(Cart(directions[val], x, y))

tick = 0 
crashed = False
while not crashed:
    tick += 1
    carts.sort(key=lambda x: (x.x, x.y))
    print(carts)
    for cart in carts:
        cart.move()
        if grid[cart.y][cart.x] == '+':
            cart.turn()
        elif (grid[cart.y][cart.x] == '/' and cart.dir[0] != 0) or (grid[cart.y][cart.x] == '\\' and cart.dir[1] != 0):
            cart.turnLeft()
        elif (grid[cart.y][cart.x] == '\\' and cart.dir[0] != 0) or (grid[cart.y][cart.x] == '/' and cart.dir[1] != 0):
            cart.turnRight()
        if len([ c for c in carts if cart.x == c.x and cart.y == c.y ]) > 1:
            crashed = True
            print('Crashed at ({}, {})!'.format(cart.x, cart.y))
            break