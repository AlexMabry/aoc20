lines = [int(n.strip()) for n in open('d10in.txt').read().splitlines()]

nums = set(lines)
combos = {n: [x for x in range(n+1, n+4) if x in nums] for n in sorted(lines)}
multiple = {num: combo for num, combo in combos.items() if len(combo) > 1}

arr = {}
for num in reversed(multiple.keys()):
    res = 0
    for x in multiple[num]:
        next_keys = [key for key in arr.keys() if key > x]
        res += arr.get(x) or (arr[min(next_keys)] if next_keys else 1)

    arr[num] = res

print(arr[0])
