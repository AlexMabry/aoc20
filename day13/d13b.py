lines = [n.strip() for n in open('d13in.txt').read().splitlines()]
bus_times = {ix: int(b) for ix, b in enumerate(lines[1].split(',')) if b != 'x'}
biggest = sorted(bus_times.items(), key=lambda bus: bus[1], reverse=True)

step, match = 1, -biggest[0][0]
for delay, num in biggest:
    while (match + delay) % num:
        match += step
    step *= num

print(match)
