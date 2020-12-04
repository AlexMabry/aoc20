import re

from day04.d4a import get_passports, REQUIRED

RULES = {
    'byr': lambda byr: byr.isnumeric() and 1920 <= int(byr) <= 2002,
    'iyr': lambda iyr: iyr.isnumeric() and 2010 <= int(iyr) <= 2020,
    'eyr': lambda eyr: eyr.isnumeric() and 2020 <= int(eyr) <= 2030,
    'hgt': lambda hgt: 150 <= int(hgt[:-2]) <= 193 if 'cm' in hgt else 59 <= int(
        hgt[:-2]) <= 76 if 'in' in hgt else False,
    'hcl': lambda hcl: re.match(r'#[0-9a-f]{6}', hcl),
    'ecl': lambda ecl: ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda pid: re.match(r'[0-9]{9}$', pid),
}


def is_valid(passport):
    return all([key in passport and RULES[key](passport[key]) for key in REQUIRED])


if __name__ == '__main__':
    passports = get_passports('d4in.txt')
    valid = sum([is_valid(p) for p in passports])
    print(valid)
