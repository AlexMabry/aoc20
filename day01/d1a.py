numbers = [int(n) for n in open('d1in.txt').read().splitlines()]

numberSet = {n for n in numbers}

for n in numberSet:
    if (2020-n) in numberSet:
        print((2020-n)*n)
        break
