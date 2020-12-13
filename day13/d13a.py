lines = [n.strip() for n in open('d13in.txt').read().splitlines()]
tod, buses = int(lines[0]), [int(b) for b in lines[1].split(',') if b != 'x']

arrivals = {b: -(-tod // b) * b for b in buses}
bus, arrival = min(arrivals.items(), key=lambda v: v[1])

print(bus*(arrival-tod))
