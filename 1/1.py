import sys
# sorry
inp = [ int(y.replace('\n', '')) for y in sys.stdin.readlines()]
print(sum(inp))

seen = []
current = 0
i = 0
while not current in seen:
    seen.append(current)
    current = seen[i] + inp[i % len(inp)]
    i += 1
print(current)
