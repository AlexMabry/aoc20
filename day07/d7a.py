from collections import defaultdict


def condense_line(line):
    necessary = line.replace(' bags', '').replace(' bag', '').replace('.', '')
    segmented = necessary.replace(' contain ', ':').replace(', ', ':').split(':')
    return segmented[0], segmented[1:]


def decode_bag_rules(rules):
    bags = defaultdict(set)

    for name, contents in rules:
        if contents[0] != 'no other':
            bags[name] = set(sub_bag[2:] for sub_bag in contents)

    return bags


def find_containers(children, rules):
    return [bname for bname, brules in rules.items() if any([x in brules for x in children])]


def holds_gold(rules):
    result = containers = set(find_containers(['shiny gold'], rules))
    while len(containers):
        containers = find_containers(containers, rules)
        result.update(containers)

    return result


if __name__ == '__main__':
    lines = [n.strip() for n in open('d7in.txt').read().splitlines()]
    rule_list = [condense_line(line) for line in lines]
    bag_rules = decode_bag_rules(rule_list)
    holds_gold = holds_gold(bag_rules)

    print(len(holds_gold))
