lines = [n.strip() for n in open('d6in.txt').read().splitlines()]

groups = []
new_group = True

for line in lines:
    if new_group:
        groups.append(set([c for c in line]))
        new_group = False
    elif line == '':
        new_group = True
    else:
        groups[-1] &= set([c for c in line])

counts = [len(group) for group in groups]

print(sum(counts))
