import re
from sys import maxsize

DIRECTIONS = {
    'e': lambda a, b: (a+1, b),
    'se': lambda a, b: (a+1 if b % 2 else a, b+1),
    'ne': lambda a, b: (a+1 if b % 2 else a, b-1),
    'w': lambda a, b: (a-1, b),
    'sw': lambda a, b: (a-1 if (b+1) % 2 else a, b+1),
    'nw': lambda a, b: (a-1 if (b+1) % 2 else a, b-1)
}
NEIGHBORS = lambda a, b: [DIRECTIONS[d](a, b) for d in DIRECTIONS]


def get_bounds(pairs):
    low = (maxsize, maxsize)
    high = (-maxsize, -maxsize)
    for a, b in pairs:
        low = (min(low[0], a), min(low[1], b))
        high = (max(high[0], a), max(high[1], b))
    return [low, high]


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

for turn in range(100):
    new_black_tiles = set()
    [(min_x, min_y), (max_x, max_y)] = get_bounds(black_tiles)

    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            black_neighbors = len([n for n in NEIGHBORS(x, y) if n in black_tiles])
            if (x, y) in black_tiles:
                if 0 < black_neighbors < 3:
                    new_black_tiles.add((x, y))
            else:
                if black_neighbors == 2:
                    new_black_tiles.add((x, y))

    black_tiles = new_black_tiles
    print(len(black_tiles))
