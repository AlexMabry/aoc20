REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def get_passports(filename):
    result = []
    rows = [n.strip() for n in open(filename).read().splitlines()]

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


def is_valid(passport):
    return all([key in passport for key in REQUIRED])


if __name__ == '__main__':
    passports = get_passports('d4in.txt')
    valid = sum([is_valid(p) for p in passports])
    print(valid)
