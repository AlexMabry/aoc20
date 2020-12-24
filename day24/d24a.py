import re

DIRECTIONS = {
    'e': lambda a, b: (a+1, b),
    'se': lambda a, b: (a+1 if b % 2 else a, b+1),
    'ne': lambda a, b: (a+1 if b % 2 else a, b-1),
    'w': lambda a, b: (a-1, b),
    'sw': lambda a, b: (a-1 if (b+1) % 2 else a, b+1),
    'nw': lambda a, b: (a-1 if (b+1) % 2 else a, b-1)
}

lines = [n.strip() for n in open('d24in.txt').read().splitlines()]
pattern = re.compile(r'(e|se|ne|w|sw|nw)')
tiles = [pattern.findall(line) for line in lines]

black_tiles = set()
for tile in tiles:
    x, y = (0, 0)
    for direction in tile:
        x, y = DIRECTIONS[direction](x, y)

    if (x, y) in black_tiles:
        black_tiles.remove((x, y))
    else:
        black_tiles.add((x, y))

print(len(black_tiles))
