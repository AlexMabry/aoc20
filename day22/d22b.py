from collections import deque
from itertools import islice

p1_deck = deque([int(n.strip()) for n in open('player1.txt').read().splitlines()])
p2_deck = deque([int(n.strip()) for n in open('player2.txt').read().splitlines()])
game_hands = {}

def play_game(p1, p2):
    beginning_hands = (tuple(p1), tuple(p2))

    if beginning_hands not in game_hands:
        round_hands = set()
        while p1 and p2:
            if (tuple(p1), tuple(p2)) in round_hands:
                return "p1"
            else:
                round_hands.add((tuple(p1), tuple(p2)))

            p1_card, p2_card = p1.popleft(), p2.popleft()

            if len(p1) >= p1_card and len(p2) >= p2_card:
                p1_sub_deck = deque([c for c in islice(p1, 0, p1_card)])
                p2_sub_deck = deque([c for c in islice(p2, 0, p2_card)])
                winner = play_game(p1_sub_deck, p2_sub_deck)
            else:
                winner = "p1" if p1_card > p2_card else "p2"

            if winner == "p1":
                p1.extend([p1_card, p2_card])
            else:
                p2.extend([p2_card, p1_card])

        game_hands[beginning_hands] = "p1" if p1 else "p2"

    return game_hands[beginning_hands]


big_winner = play_game(p1_deck, p2_deck)
both_decks = [*p1_deck, *p2_deck]
print(sum([card*(len(both_decks)-level) for level, card in enumerate(both_decks)]))

