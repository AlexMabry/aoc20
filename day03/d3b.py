rows = [n for n in open('d3in.txt').read().splitlines()]

trees = [[x == '#' for x in row] for row in rows]

h, w = len(rows), len(trees[0])
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1

for dx, dy in slopes:

    count = 0
    x, y = 0, 0
    while y < h:
        count += 1 if trees[y][x] else 0
        x = (x+dx) % w
        y += dy

    product *= count

print(product)
