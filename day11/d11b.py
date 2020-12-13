spots = [[c for c in n.strip()] for n in open('d11in.txt').read().splitlines()]
height = len(spots)
width = len(spots[0])


DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def move(point, offset):
    return point[0] + offset[0], point[1] + offset[1]


def value(point):
    return spots[point[1]][point[0]]


def neighbors_occupied(x, y):
    neighbors = 0
    for d in DIRECTIONS:
        cur = (x + d[0], y + d[1])
        while 0 <= cur[0] < width and 0 <= cur[1] < height:
            if value(cur) == '#':
                neighbors += 1
                break
            elif value(cur) == 'L':
                break

            cur = move(cur, d)

    return neighbors


def what_now(x, y):
    now = value((x, y))
    neighbors = neighbors_occupied(x, y)

    if now == 'L' and neighbors == 0:
        return '#'
    elif now == '#' and neighbors >= 5:
        return 'L'
    else:
        return now

taken = 0
new_taken = -1
while taken != new_taken:
    taken = new_taken
    spots = [[what_now(ix, iy) for ix in range(width)] for iy in range(height)]
    new_taken = sum([1 if value((ix, iy)) == '#' else 0 for ix in range(width) for iy in range(height)])

print(new_taken)
