from util import decode_list

lines = [n.strip() for n in open('d12in.txt').read().splitlines()]

template = r'(?P<cmd>.)(?P<num>[0-9]+)'
commands = decode_list(lines, template)

x, y = 0, 0
wx, wy = 10, 1

MOVE_WAY = {
    0: lambda _: (wx, wy),
    1: lambda _: (wy, -wx),
    2: lambda _: (-wx, -wy),
    3: lambda _: (-wy, wx),
    'R': lambda deg: MOVE_WAY[int(deg / 90)](deg),
    'L': lambda deg: MOVE_WAY[4 - int(deg / 90)](deg),
    'E': lambda off: (wx + off, wy),
    'S': lambda off: (wx, wy - off),
    'W': lambda off: (wx - off, wy),
    'N': lambda off: (wx, wy + off),
}

for c in commands:
    if c.cmd == 'F':
        x, y = x + int(c.num)*wx, y + int(c.num)*wy
        print(c.cmd, c.num, ":", x, y)
    else:
        wx, wy = MOVE_WAY[c.cmd](int(c.num))
        print(c.cmd, c.num, ":", wx, wy)

print(x, y)
print(abs(x) + abs(y))
