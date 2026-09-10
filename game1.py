##Game 1: High Card
import random
import time

class card:
    suits = ['Spades ♠️', 'Clubs ♣️', 'Hearts ♥️', 'Diamonds ♦️']
    ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    rank_name = {1: 'Ace of',
                2: 'Two of',
                3: 'Three of',
                4: 'Four of', 
                5: 'Five of',
                6: 'Six of',
                7: 'Seven of', 
                8: 'Eight of', 
                9: 'Nine of', 
                10: 'Ten of', 
                11: 'Jack of', 
                12: 'Queen of', 
                13: 'King of'}
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @classmethod
    def shuffle(cls):
        new_suit = random.choice(card.suits)
        new_rank = random.choice(card.ranks)
        return cls(new_suit, new_rank)

    def card_name (self):
        return '{} {}  (number {})'.format(self.rank_name[self.rank], self.suit, self.rank)

print("\nHigh Card — PC will draw a card, you'll have to guess if the one you'll draw will be higher or lower than PC's.")
PC_card = card.shuffle()
print("PC's card is the {}".format(PC_card.card_name()))

time.sleep(3)

while True:
    guess = input("Do you think your card will be:\n1. Higher\n2. Lower\n")
    if not guess in ['1','2','Higher','Lower']:
        time.sleep(0.5)
        print("Please pick one of the alternatives")
    else:
        break

if guess in ('1', 'Higher'):
    guess = 1
else:
    guess = 0

time.sleep(0.5)

user_card = card.shuffle()

print("Your card is the {}".format(user_card.card_name()))
## need to compare the result to win or lose
if user_card.rank == PC_card.rank:
    print("Tie!")
elif (user_card.rank > PC_card.rank) == guess:
    print("You Win!")
else:
    print("You Lose!")

    ##we can make games in a row, and use ascii to make it more interesting perhaps. And add points to make them craaaave the winnnnn