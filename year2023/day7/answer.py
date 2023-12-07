import os, re
import pprint


class Hand:
    cards: str
    card_rank: int
    bid: int

    def _set_card_rank(self) -> None:
        match len(set(self.cards)):
            case 1:
                self.card_rank = 7  # 5 cards
            case 2:
                self.card_rank = 5  # Full house
                for c in set(self.cards):
                    if self.cards.count(c) == 4:
                        self.card_rank = 6  # 4 cards
            case 3:
                self.card_rank = 3  # Two pair
                for c in set(self.cards):
                    if self.cards.count(c) == 3:
                        self.card_rank = 4  # 3 cards
            case 4:
                self.card_rank = 2  # one pair
            case 5:
                self.card_rank = 1  # High card

    def _get_card_level(self, card: str):
        if len(card) != 1:
            raise Exception(f"_get_card_level() accepts only one card")
        return "23456789TJQKA".index(card)

    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = int(bid)
        self._set_card_rank()

    def __lt__(self, other):
        if self.card_rank == other.card_rank:
            for i in range(0, 5):
                self_level = self._get_card_level(self.cards[i])
                other_level = self._get_card_level(other.cards[i])
                if self_level != other_level:
                    return self_level < other_level
        else:
            return self.card_rank < other.card_rank


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    lines = [re.match(r"([\w\d]+) (\d+)", line).groups() for line in lines]

hands = [Hand(x[0], x[1]) for x in lines]
hands.sort()
pprint.pp([x.__dict__ for x in hands])

print(f"Puzzle 1: {sum([(i + 1) * x.bid for i, x in enumerate(hands)])}")
