spots = [[c for c in n.strip()] for n in open('d11in.txt').read().splitlines()]
height = len(spots)
width = len(spots[0])


def neighbors_occupied(x, y):
    neighbors = [(ix, iy) for ix in range(x-1, x+2) for iy in range(y-1, y+2) if 0 <= ix < width and 0 <= iy < height and not (ix == x and iy == y)]
    return sum([1 if spots[iy][ix] == '#' else 0 for ix, iy in neighbors])


def what_now(x, y):
    now = spots[y][x]
    neighbors = neighbors_occupied(x, y)

    if now == 'L' and neighbors == 0:
        return '#'
    elif now == '#' and neighbors >= 4:
        return 'L'
    else:
        return now


taken = 0
new_taken = -1
while taken != new_taken:
    taken = new_taken
    spots = [[what_now(ix, iy) for ix in range(width)] for iy in range(height)]
    new_taken = sum([1 if spots[iy][ix] == '#' else 0 for ix in range(width) for iy in range(height)])

print(new_taken)
