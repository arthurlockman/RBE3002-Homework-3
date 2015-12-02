class Card:
    """
    This class simulates a card.
    """
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, rank):
        """
        Initialize the card.
        :param suit: Suit from 0-4
        :param rank: Rank from 0-13
        """
        self.suit = Card.suits[suit]
        self.rank = Card.ranks[rank]
        self.number = (suit + 1) * (rank + 1)

    def get_number(self):
        """
        Get the card number in the deck.
        :return:
        """
        return self.number

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.rank + ' of ' + self.suit)
