import sys

def parse(x: [str]) -> (str, [str]):
    init = x[0][x[0].find(':') + 2:].strip()
    will_live = [ y[:5] for y in x if '=> #' in y ]
    return (init, will_live)

def calc_score(state: str, offset: int) -> int:
    score = 0
    for i, v in enumerate(state):
        if v == '#': 
            score += (i - offset)
    return score

state, will_live = parse(sys.stdin.readlines())
state = '.....' + state + '....'

prev_score = None
cur_score = None
offset = 5
for i in range(150):
    new_state = ''
    for x in range(len(state)):
        if state[x-2:x+3] in will_live:
            new_state += '#'
        else: new_state += '.'
    if new_state[:3] == '..#':
        offset += 2
        new_state = '..' + new_state
    if new_state[-3:] == '#..':
        new_state = new_state + '..'
    state = new_state
    prev_score = cur_score
    cur_score = calc_score(state, offset)
    if prev_score and cur_score:
        print('Generation #{}: Score {}, Diff {}'.format(i + 1, cur_score, cur_score - prev_score))

print(state)