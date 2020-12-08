lines = [n.strip().split(' ') for n in open('d8in.txt').read().splitlines()]

past = set()
commands = [(cmd, int(num)) for [cmd, num] in lines]

acc = 0
ptr = 0
while ptr not in past:
    past.add(ptr)
    cmd, num = commands[ptr]

    if cmd == 'acc':
        acc += num

    if cmd == 'jmp':
        ptr += num
    else:
        ptr += 1

print(acc)
