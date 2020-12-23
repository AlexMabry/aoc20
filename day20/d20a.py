from collections import defaultdict
from math import prod

def rotate(tile, times=1):
    size = len(tile)
    result = tile if times < 4 else [tile[size-x-1] for x in range(size)]
    for t in range(times % 4):
        result = [''.join([result[iy][size-ix-1] for iy in range(size)]) for ix in range(size)]
    return result

def get_sides(square):
    return [[row[0] for row in square], square[0], [row[-1] for row in square], square[-1]]

def find_match(parent, cube_side):
    for number, edge_versions in boarders.items():
        for version in edge_versions:
            if number != parent and cube_side in version:
                return number
    return None

lines = [n.strip() for n in open('d20in.txt').read().splitlines()]

next_tile = None
tiles = defaultdict(list)
for line in lines:
    if not line:
        next_tile = None
    elif not next_tile:
        next_tile = int(line[5:].replace(':', ''))
    else:
        tiles[next_tile].append(line)

versions = {num: [rotate(tile, turn) for turn in range(8)] for num, tile in tiles.items()}
boarders = {num: [[''.join(edge) for edge in get_sides(square)] for square in squares] for num, squares in versions.items()}
matches = {num: [[find_match(num, side) for side in version] for version in modes] for num, modes in boarders.items()}
corners = [num for num, modes in matches.items() if len({edge for tile in modes for edge in tile if edge}) == 2]
print(prod(corners))
