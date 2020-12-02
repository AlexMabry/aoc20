import re

lines = [n for n in open('d2in.txt').read().splitlines()]

template = re.compile(r'(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<char>.): (?P<password>.*)')

valid = 0
for line in lines:
    value = template.search(line).groupdict()
    low = value["password"][int(value["min"]) - 1]
    high = value["password"][int(value["max"]) - 1]

    if low != high and (low == value["char"] or high == value["char"]):
        valid += 1

print(valid)
