rows = [n for n in open('d3in.txt').read().splitlines()]

trees = [[x == '#' for x in row] for row in rows]

x, y = 0, 0
count = 0
h, w = len(rows), len(trees[0])

while y < h:
    count += 1 if trees[y][x] else 0
    x = (x+3) % w
    y += 1

print(count)
