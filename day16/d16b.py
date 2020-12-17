from math import prod

lines = [n.strip().split(": ") for n in open('rules.txt').read().splitlines()]
all_fields = {line[0]: [[int(num) for num in nums.split('-')] for nums in line[1].split(" or ")] for line in lines}

lines = [n.strip().split(",") for n in open('nearby_tickets.txt').read().splitlines()]
all_tickets = [[int(num) for num in line] for line in lines]

lines = [n.strip().split(",") for n in open('your_ticket.txt').read().splitlines()]
my_ticket = [[int(num) for num in line] for line in lines][0]


def invalid_field(fields, num):
    return len([num for field in fields.values() for rule in field if rule[0] < num < rule[1]]) == 0


def invalid_ticket(fields, ticket):
    return len([num for num in ticket if invalid_field(fields, num)]) > 0


def could_be_field(rules, nums):
    return all([any([rule[0] <= num <= rule[1] for rule in rules]) for num in nums])


def get_valid_tickets(tickets, fields):
    return [ticket for ticket in tickets if not invalid_ticket(fields, ticket)]


valid_tickets = get_valid_tickets(all_tickets, all_fields)
columns = [set(ticket[ix] for ticket in valid_tickets) for ix, _ in enumerate(my_ticket)]
possibilities = {ix: [name for name, rules in all_fields.items() if could_be_field(rules, nums)] for ix, nums in enumerate(columns)}

answer = {}
while possibilities:
    only_one = {num: names[0] for num, names in possibilities.items() if len(names) == 1}

    for num, name in only_one.items():
        answer[name] = num

        for _, names in possibilities.items():
            if name in names:
                names.remove(name)

    possibilities = {k: v for k, v in possibilities.items() if v}

answer = prod([my_ticket[num] for name, num in answer.items() if 'departure' in name])

print(answer)
