lines = [int(n.strip()) for n in open('d9in.txt').read().splitlines()]


sets = [{lines[y] for y in range(x, x+25)} for x in range(len(lines)-25)]


def combo(num, group):
    print(num, group)
    for g in group:
        if num-g in group:
            print(num, g, num-g)
            return False
    return True


for n in range(25, len(lines)):
    if combo(lines[n], sets[n-25]):
        print(lines[n])
        break



