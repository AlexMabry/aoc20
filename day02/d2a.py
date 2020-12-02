import re

lines = [n for n in open('d2in.txt').read().splitlines()]

template = re.compile(r'(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<char>.): (?P<password>.*)')

valid = 0
for line in lines:
    value = template.search(line).groupdict()
    times = value["password"].count(value["char"])

    if int(value["min"]) <= times <= int(value["max"]):
        valid += 1

print(valid)
