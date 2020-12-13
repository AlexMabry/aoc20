from collections import defaultdict

lines = [int(n.strip()) for n in open('d10in.txt').read().splitlines()]

last = 0
count = defaultdict(int)



for n in sorted(lines):
    print(n)
    count[n-last] += 1
    last = n

print(count)

print(count[1] * (count[3]+1))
