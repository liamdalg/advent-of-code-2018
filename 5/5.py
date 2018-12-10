import sys
from string import ascii_lowercase

# part one 
inp = sys.stdin.read()

def remove(x: str) -> str:
    changed = True
    new = ''
    while changed:
        new = x
        for i in ascii_lowercase:
            x = x.replace(i + i.upper(), '').replace(i.upper() + i, '')
        changed = new != x
    return new

new = remove(inp)

print(new)
print(len(new))

# part two
minimum = len(new)
for i in ascii_lowercase:
    minimum = min(minimum, len(remove(new.replace(i, '').replace(i.upper(), ''))))

print(minimum)