import sys

inp = sys.stdin.read().split(' ')
players, max_marble = int(inp[0]), int(inp[6])

state = [0]
cur_marble, cur_player = 1, 0
scores = [0] * players
for i in range(1, max_marble + 1):
    if i % 23 == 0:
        seven = (cur_marble - 7) % len(state)
        cur_marble = seven
        other = state[seven]
        scores[cur_player] += (i + other)
        state.remove(other)
    else:
        cur_marble = (cur_marble + 2) % len(state)
        state.insert(cur_marble, i)
    if cur_marble == 0: cur_marble = len(state)
    cur_player = (cur_player + 1) % players

print(max(scores))