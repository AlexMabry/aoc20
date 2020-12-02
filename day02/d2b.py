from util import decode_list

lines = [n for n in open('d2in.txt').read().splitlines()]

template = r'(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<char>.): (?P<password>.*)'
decoded = decode_list(lines, template)

valid = 0
for line in decoded:
    low = line.password[int(line.min) - 1]
    high = line.password[int(line.max) - 1]

    if low != high and (low == line.char or high == line.char):
        valid += 1

print(valid)
