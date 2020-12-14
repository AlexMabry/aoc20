import re


def replace(msk, num, dig):
    for c in format(int(num), 'b').zfill(dig):
        msk = msk.replace('X', c, 1)

    return int(msk, 2)


mask = ''
locations = {}

lines = [n.strip().split(' = ') for n in open('d14in.txt').read().splitlines()]
for [cmd, val] in lines:
    if cmd == 'mask':
        mask = val
    else:
        loc = format(int(re.match(r'mem\[([0-9]+)\]', cmd)[1]), 'b').zfill(36)
        result = ''.join([v if m == '0' else '1' if m == '1' else 'X' for v, m in zip(loc, mask)])
        unknowns = result.count('X')
        entries = [replace(result, x, unknowns) for x in range(2**unknowns)]
        for e in entries:
            locations[e] = int(val)

print(sum(locations.values()))
