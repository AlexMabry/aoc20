lines = [n.strip().split(": ") for n in open('rules.txt').read().splitlines()]
all_fields = {line[0]: [[int(num) for num in nums.split('-')] for nums in line[1].split(" or ")] for line in lines}

lines = [n.strip().split(",") for n in open('nearby_tickets.txt').read().splitlines()]
all_tickets = [[int(num) for num in line] for line in lines]

valid = lambda num: any([any([rule[0] <= num <= rule[1] for rule in field]) for field in all_fields.values()])
result = sum([num for ticket in all_tickets for num in ticket if not valid(num)])

print(result)
