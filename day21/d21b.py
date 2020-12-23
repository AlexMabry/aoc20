from collections import defaultdict
from util import decode_list

lines = [n.strip() for n in open('d21in.txt').read().splitlines()]
template = r'(?P<ingredients>[a-z ]*) \(contains (?P<allergens>[a-z, ]*)\)'
foods = decode_list(lines, template)

all_ingredients = set([ingredient for food in foods for ingredient in food.ingredients.split(' ')])
not_present = defaultdict(set)

for food in foods:
    ingredients = set(food.ingredients.split(' '))
    absent = all_ingredients - ingredients

    for allergen in food.allergens.split(', '):
        not_present[allergen] |= absent

not_possible = set.intersection(*not_present.values())

possible = {allergen: all_ingredients - no_chance for allergen, no_chance in not_present.items()}
answers = defaultdict(str)

while len(possible):
    obvious = {k: v for k, v in possible.items() if len(v) == 1}

    for k, v in obvious.items():
        for allergen in possible:
            possible[allergen] = possible[allergen] - v

        answers[k] = v.pop()

    possible = {k: v for k, v in possible.items() if v}

print(','.join([v for k, v in sorted(answers.items())]))
