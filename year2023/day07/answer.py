import os, re
import pprint


class Hand_P1:
    cards: str
    card_rank: int
    bid: int

    def get_card_rank(self, cards: str) -> None:
        match len(set(cards)):
            case 1:
                return 7  # 5 cards
            case 2:
                for c in set(cards):
                    if cards.count(c) == 4:
                        return 6  # 4 cards
                return 5  # Full house
            case 3:
                for c in set(cards):
                    if cards.count(c) == 3:
                        return 4  # 3 cards
                return 3  # Two pair
            case 4:
                return 2  # one pair
            case 5:
                return 1  # High card

    def _get_card_level(self, card: str):
        if len(card) != 1:
            raise Exception(f"_get_card_level() accepts only one card")
        return "23456789TJQKA".index(card)

    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = int(bid)
        self.card_rank = self.get_card_rank(self.cards)

    def __lt__(self, other):
        if self.card_rank == other.card_rank:
            for i in range(0, 5):
                self_level = self._get_card_level(self.cards[i])
                other_level = self._get_card_level(other.cards[i])
                if self_level != other_level:
                    return self_level < other_level
        else:
            return self.card_rank < other.card_rank


class Hand_P2(Hand_P1):
    def _get_card_level(self, card: str):
        if len(card) != 1:
            raise Exception(f"_get_card_level() accepts only one card")
        return "J23456789TQKA".index(card)

    def get_card_rank(self, cards: str) -> None:
        if "J" not in cards:
            return super().get_card_rank(cards)

        max_rank = 0
        for x in "23456789TQKA":
            max_rank = max(max_rank, super().get_card_rank(cards.replace("J", x)))
        return max_rank

    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = int(bid)
        self.card_rank = self.get_card_rank(cards)


with open(f"{os.path.dirname(__file__)}/input.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    lines = [re.match(r"([\w\d]+) (\d+)", line).groups() for line in lines]

hands_p1 = [Hand_P1(x[0], x[1]) for x in lines]
hands_p1.sort()
pprint.pp([x.__dict__ for x in hands_p1])

hands_p2 = [Hand_P2(x[0], x[1]) for x in lines]
hands_p2.sort()
pprint.pp([x.__dict__ for x in hands_p2])

print(f"Puzzle 1: {sum([(i + 1) * x.bid for i, x in enumerate(hands_p1)])}")
print(f"Puzzle 2: {sum([(i + 1) * x.bid for i, x in enumerate(hands_p2)])}")
