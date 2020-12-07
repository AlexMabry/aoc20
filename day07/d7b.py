from collections import defaultdict


def condense_line(line):
    necessary = line.replace(' bags', '').replace(' bag', '').replace('.', '')
    segmented = necessary.replace(' contain ', ':').replace(', ', ':').split(':')
    return segmented[0], segmented[1:]


def decode_bag_rules(rules):
    bags = defaultdict(dict)

    for name, contents in rules:
        if contents[0] != 'no other':
            bags[name] = {sub_bag[2:]: int(sub_bag[0]) for sub_bag in contents}

    return bags


def children_require(bag, rules):
    return sum([num * bag_requires(bag_rules[name], rules) for name, num in bag.items()]) if bag else 0


def bag_requires(bag, rules):
    return children_require(bag, rules) + 1


if __name__ == '__main__':
    lines = [n.strip() for n in open('d7in.txt').read().splitlines()]
    rule_list = [condense_line(line) for line in lines]
    bag_rules = decode_bag_rules(rule_list)

    gold_requires = children_require(bag_rules['shiny gold'], bag_rules)
    print(gold_requires)
