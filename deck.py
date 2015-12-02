from card import Card


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
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.cards)


if __name__ == '__main__':
    print 'Running deck sim.'
    deck = Deck()
    print deck
