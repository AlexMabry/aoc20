numbers = [int(n) for n in open('d1in.txt').read().splitlines()]

numberSet = {n for n in numbers}
pairsSet = {(min(na, nb), max(na, nb)) for na in numbers for nb in numbers}

for na, nb in pairsSet:
    nc = 2020 - (na + nb)
    if nc in numberSet:
        print(na*nb*nc)
        break

