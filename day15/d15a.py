recent = {
    9: (1, 1),
    3: (2, 2),
    1: (3, 3),
    0: (4, 4),
    8: (5, 5),
    4: (6, 6)
}

last = 4
for turn in range(len(recent.keys()) + 1, 2_021):
    last = recent[last][1] - recent[last][0]
    recent[last] = (recent[last][1] if last in recent else turn, turn)

print(last)
