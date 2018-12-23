import sys

def parse(x: [str]) -> (str, [str]):
    init = x[0][x[0].find(':') + 2:].strip()
    will_live = [ y[:5] for y in x if '=> #' in y ]
    return (init, will_live)

state, will_live = parse(sys.stdin.readlines())
# I'm lazy so let's just pad for now
state = state.ljust(200, '.').rjust(300, '.')

for i in range(20):
    new_state = ''
    for x in range(len(state)):
        if state[x-2:x+3] in will_live:
            new_state += '#'
        else: new_state += '.'
    state = new_state

score = 0
for i, v in enumerate(state):
    if v == '#': 
        score += (i - 100)

print(state)
print(score)