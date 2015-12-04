from card import Card
from random import shuffle


class Deck:
    """
    Simulates a deck of cards.
    """

    def __init__(self):
        self.cards = []
        for i in range(0, 4):
            for j in range(0, 13):
                self.cards.append(Card(i, j))

    def shuffle(self):
        """
        Shuffle the deck.
        """
        shuffle(self.cards)

    def peek(self):
        """
        Peek at the top card on the deck.
        :return: A card, the top card.
        """
        return self.cards[0]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.cards)


if __name__ == '__main__':
    print 'Running deck sim.'
    deck = Deck()
    trials = 0
    draws = 0
    for i in range(0, 1000000):
        deck.shuffle()
        card = deck.peek()
        if card.rank == Card.ranks[0]:
            draws += 1
        trials += 1
    print "Trials: ", trials, " Draws: ", draws, " Probability: ", (float(draws) / trials)
