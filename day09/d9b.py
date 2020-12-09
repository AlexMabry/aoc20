lines = [int(n.strip()) for n in open('d9in.txt').read().splitlines()]

parta = 373803594

for start, n in enumerate(lines):
    for end in range(start+2, len(lines)):
        subset = [lines[y] for y in range(start, end)]
        if sum(subset) > parta:
            break
        elif sum(subset) == parta:
            print(min(subset) + max(subset))
            break
