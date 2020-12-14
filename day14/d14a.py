import re

lines = [n.strip().split(' = ') for n in open('d14in.txt').read().splitlines()]

mask = ''
locations = {}

for [cmd, val] in lines:
    if cmd == 'mask':
        mask = val
    else:
        loc = int(re.match(r'mem\[([0-9]+)\]', cmd)[1])
        val = format(int(val), 'b').zfill(36)
        locations[loc] = int(''.join([m if m != 'X' else v for v, m in zip(val, mask)]), 2)

print(sum(locations.values()))

