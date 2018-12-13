import sys
import heapq

# part one
steps = [ (x[5], x[36]) for x in sys.stdin.readlines() ]

def startEndSteps(xs: [(str, str)]) -> (str, str):
    # get the difference between the target and source sets
    targets = { x[1] for x in xs }
    sources = { x[0] for x in xs }
    starts = list(sources - targets)
    ends = list(targets - sources)
    return sorted(starts), sorted(ends)

starts, ends = startEndSteps(steps)
targets = { x[0]: [] for x in steps }
prerequisites = { x[1]: [] for x in steps }
for x in ends:
    targets[x] = []

for i in steps:
    targets[i[0]].append(i[1])
    prerequisites[i[1]].append(i[0])

for x in targets.values():
    x.sort()

heap = [ x for x in starts ]
order = ''
for i in range(len(targets)):
    s = heapq.heappop(heap)
    order += s
    for j in prerequisites.values():
        if s in j: j.remove(s)
    for x in targets[s]:
        if len(prerequisites[x]) == 0: heapq.heappush(heap, x)

print(order)