from collections import defaultdict

SIZE = 12
LEFT, TOP, RIGHT, BOTTOM = 0, 1, 2, 3
MONSTER = [[18], [0, 5, 6, 11, 12, 17, 18, 19], [1, 4, 7, 10, 13, 16]]

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

def find_position(tile, left, top):
    return next(i for i, v in enumerate(matches[tile]) if v[TOP] == top and v[LEFT] == left)

def found_sea_monster(y_off, x_off):
    return all([picture[y_off + y][x_off + x] == '#' for y, points in enumerate(MONSTER) for x in points])

def mark_sea_monster(y_off, x_off):
    for y, points in enumerate(MONSTER):
        picture[y_off+y] = ''.join(['O' if (x-x_off in points) else c for x, c in enumerate(picture[y_off + y])])

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

start_tile = corners[0]
answer = []
positions = defaultdict(list)
for iy in range(SIZE):
    if iy == 0:
        first = start_tile
        turns = 2
        tiles[first] = rotate(tiles[first], turns)
        position = matches[first][turns]
    else:
        first = positions[answer[iy-1][0]][BOTTOM]
        turns = find_position(first, None, answer[iy - 1][0])
        tiles[first] = rotate(tiles[first], turns)
        position = matches[first][turns]

    positions[first] = position
    answer.append([first])
    prev = first

    for ix in range(1, SIZE):
        current = position[RIGHT]
        answer[iy].append(current)
        turns = find_position(current, prev, None if iy == 0 else answer[iy - 1][ix])
        tiles[current] = rotate(tiles[current], turns)
        position = matches[current][turns]
        positions[current] = position
        prev = current

picture = [''.join([''.join([tiles[answer[y][x]][w][v] for v in range(1, 9)]) for x in range(SIZE)]) for y in range(SIZE) for w in range(1, 9)]
picture = rotate(picture, 7)
for iy, row in enumerate(picture):
    for ix in range(len(row)):
        if iy < (len(picture) - 2) and ix < (len(row) - 19) and found_sea_monster(iy, ix):
            mark_sea_monster(iy, ix)

print(sum(tile_row.count('#') for tile_row in picture))
