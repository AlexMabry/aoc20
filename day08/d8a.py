lines = [n.strip().split(' ') for n in open('d8in.txt').read().splitlines()]


def f_cmd(cmd, num):
    return lambda a, p: (a + (num if cmd == 'acc' else 0), p + (num if cmd == 'jmp' else 1))


past = set()
commands = [f_cmd(cmd, int(num)) for [cmd, num] in lines]

acc, ptr = 0, 0
while ptr not in past:
    past.add(ptr)
    acc, ptr = commands[ptr](acc, ptr)

print(acc)
