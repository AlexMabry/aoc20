lines = [n.strip().split(' ') for n in open('d8in.txt').read().splitlines()]

commands = [(cmd, int(num)) for [cmd, num] in lines]
jmp_nop = iter([ix for ix, [cmd, num] in enumerate(commands) if cmd in ['nop', 'jmp']])

acc = 0
ptr = 0

while not ptr >= len(commands):
    ptr = 0
    acc = 0
    past = {len(commands)}
    change = next(jmp_nop)

    while ptr not in past:
        past.add(ptr)
        cmd, num = commands[ptr]

        if cmd == 'acc':
            acc += num

        if ptr == change:
            cmd = 'jmp' if cmd == 'nop' else 'nop'

        if cmd == "jmp":
            ptr += num
        else:
            ptr += 1

print(acc)
