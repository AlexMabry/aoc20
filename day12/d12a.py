from util import decode_list

lines = [n.strip() for n in open('d12in.txt').read().splitlines()]

template = r'(?P<cmd>.)(?P<num>[0-9]+)'
commands = decode_list(lines, template)

DIRECTIONS = ['E', 'S', 'W', 'N']
DISTANCE = {'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'N': (0, 1)}

x, y = 0, 0
pointed = 0

ROTATE = {
    'R': lambda deg: (pointed + int(deg / 90)) % 4,
    'L': lambda deg: (pointed - int(deg / 90)) % 4
}

MOVE = {
    'E': lambda off: (x + off, y),
    'S': lambda off: (x, y + off),
    'W': lambda off: (x - off, y),
    'N': lambda off: (x, y - off),
    'F': lambda off: MOVE[DIRECTIONS[pointed]](off)
}


for c in commands:
    if c.cmd in ['L', 'R']:
        pointed = ROTATE[c.cmd](int(c.num))
    else:
        x, y = MOVE[c.cmd](int(c.num))

print(x, y)
print(abs(x) + abs(y))
