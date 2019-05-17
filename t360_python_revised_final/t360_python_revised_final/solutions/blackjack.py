import random
from functools import reduce


class Card:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    def __str__(self):
        return self.color + str(self.shape)

    def value(self):
        if type(self.shape) == int:
            return self.shape
        elif self.shape == "A":
            return 1
        else:
            return 10

    def order(self):
        return Deck.shapes.index(self.shape)


class Deck:
    shapes = [2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K", "A"]

    def __init__(self):
        self.cards = []
        for color in ["♠", "♥", "♦", "♣"]:
            for shape in Deck.shapes:
                self.cards.append(Card(color, shape))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def take(self, card):
        self.cards.append(card)

    def __str__(self):
        card_strings = map(lambda c: str(c), self.cards)
        cards = reduce(lambda c1, c2: c1 + " " + c2, card_strings)
        return "{} ({})".format(cards, self.value())

    def value(self):
        card_values = map(lambda c: c.value(), self.cards)
        total = reduce(lambda c1, c2: c1 + c2, card_values)

        if total <= 11:
            for card in self.cards:
                if card.shape == "A":
                    total += 10
                    break

        return total

    def __lt__(self, other):
        if self.value() > 21 >= other.value():
            return True
        elif other.value() > 21 >= self.value():
            return False
        elif self.value() > other.value():
            return False
        elif other.value() > self.value():
            return True
        elif len(self.cards) < len(other.cards):
            return False
        elif len(other.cards) < len(self.cards):
            return True
        else:
            self_cards = sorted(self.cards, key=lambda c: c.order(), reverse=True)
            other_cards = sorted(other.cards, key=lambda c: c.order(), reverse=True)

            for i in range(len(self_cards)):
                if self_cards[i].order() < other_cards[i].order():
                    return True


def main():
    # 1: initial deal
    deck = Deck()
    dealer = Hand()
    player = Hand()

    player.take(deck.draw())
    player.take(deck.draw())

    dealer.take(deck.draw())
    dealer.take(deck.draw())

    print("Dealer's hand: ", dealer)
    print("Your hand: ", player)

    # 2: player acts

    while player.value() < 21:
        action = input("hit or stand?")
        if action == "stand":
            break
        player.take(deck.draw())
        print("Your hand: ", player)

    # 3: dealer acts

    while dealer < player and dealer.value() <= 21:
        dealer.take(deck.draw())

    # 4: print result

    print("Dealer's hand: ", dealer)
    print("Your hand: ", player)

    if dealer < player:
        print("You won! Congratulations!")
    else:
        print("You suck, loser!")

main()