##Game 1: High Card
import random

class card:
    suits = ['Spades ♠️', 'Clubs ♣️', 'Hearts ♥️', 'Diamonds ♦️']
    ranks = ['Two of', 'Three of', 'Four of', 'Five of', 'Six of', 'Seven of', 'Eight of', 'Nine of', 'Ten of', 'Jack of', 'Queen of', 'King of', 'Ace of']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @classmethod
    def shuffle(cls):
        new_suit = random.choice(card.suits)
        new_rank = random.choice(card.ranks)
        return cls(new_suit, new_rank)

    def card_name (self):
        ##no = self.rank(ranks[no])
        ##return '{} {} is no. {}'.format(self.rank, self.suit, no)

user_card = card.shuffle()
print(user_card.card_name())

##i wanna know what rank it isssss