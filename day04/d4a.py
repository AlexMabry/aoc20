def get_passports(filename):
    result = []
    rows = [n.strip() for n in open('d4in.txt').read().splitlines()]

    cur = 0
    for row in rows:
        if row == "":
            cur += 1
        else:
            fields = dict([field.split(':') for field in row.split(' ')])

            if len(result) == cur:
                result.append(fields)
            else:
                result[cur].update(fields)

    return result

passports = get_passports('d4in.txt')
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid = 0
for p in passports:
    if all([key in p for key in required]):
        valid += 1

print(valid)

