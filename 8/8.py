import sys

data = [ int(x) for x in sys.stdin.read().split(' ') ]

class Node():

    def __init__(self, c_count: int, m_count: int):
        self.children = []
        self.metadata = []
        self.c_count = c_count
        self.m_count = m_count

# thanks Nic
def parse(rem_data: [int]) -> ([int], Node):
    cur = Node(*rem_data[:2])
    rem_data = rem_data[2:]

    for _ in range(cur.c_count):
        rem_data, node = parse(rem_data)
        cur.children.append(node)

    # now the end should be their metadata
    cur.metadata += rem_data[:cur.m_count]
    rem_data = rem_data[cur.m_count:]
    return (rem_data, cur)

def sum_meta(root: Node) -> int:
    s = sum(root.metadata)
    for c in root.children:
        s += sum_meta(c)
    return s

def sum_value(cur: Node) -> int:
    if cur.c_count == 0:
        return sum(cur.metadata)
    s = 0
    for m in cur.metadata:
        if m != 0 and m <= len(cur.children):
            s += sum_value(cur.children[m - 1])
    return s

data, root = parse(data)
total = sum_meta(root)
value = sum_value(root)
print(total)
print(value)