from collections import deque

p1_deck = deque([int(n.strip()) for n in open('player1.txt').read().splitlines()])
p2_deck = deque([int(n.strip()) for n in open('player2.txt').read().splitlines()])

while p1_deck and p2_deck:
    p1_card, p2_card = p1_deck.popleft(), p2_deck.popleft()

    if p1_card > p2_card:
        p1_deck.extend([p1_card, p2_card])
    else:
        p2_deck.extend([p2_card, p1_card])

both_decks = [*p1_deck, *p2_deck]
print(sum([card*(len(both_decks)-level) for level, card in enumerate(both_decks)]))


