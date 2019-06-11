import random
from copy import deepcopy

suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
suit_dict = {0:1, 1:4, 2:9, 3:16}
rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9',
                  '10', 'Jack', 'Queen', 'King']

class Card:
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return ('{} of {}'.format(rank_names[self.rank],
                                  suit_names[self.suit]))


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = [str(card) for card in self.cards]
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label


print('===   The small card game STOP   ===')
print()
print('Shuffling a deck of cards')
print()
print('Dealing 2 cards for each players')
print()
k = input('5 players for this game. \n   Which player will you bet (1~5) : ')
while True:
    if k == '1' or k == '2' or k == '3' or k == '4' or k == '5':
        break;
    else:
        k = input('  Which player will you bet (1 ~ 5 ) : ')
print()

hand1 = Hand('Player 1')
hand2 = Hand('Player 2')
hand3 = Hand('Player 3')
hand4 = Hand('Player 4')
hand5 = Hand('Player 5')

deck = Deck()
deck.shuffle()

deck.move_cards(hand1, 2)
deck.move_cards(hand2, 2)
deck.move_cards(hand3, 2)
deck.move_cards(hand4, 2)
deck.move_cards(hand5, 2)

print('::::: Player 1:')
print(hand1)
print('::::: Player 2:')
print(hand2)
print('::::: Player 3:')
print(hand3)
print('::::: Player 4:')
print(hand4)
print('::::: Player 5:')
print(hand5)

def compare(h1, h2):
    '''

    :param h1:
    :param h2:
    :return:
    '''
    rank1 = (h1.cards[0].rank + h1.cards[1].rank) % 10
    rank2 = (h2.cards[0].rank + h2.cards[1].rank) % 10

    suit1_sum = suit_dict[h1.cards[0].suit] + suit_dict[h1.cards[1].suit]
    suit2_sum = suit_dict[h2.cards[0].suit] + suit_dict[h2.cards[1].suit]

    max_rank1 = max(h1.cards[0].rank, h1.cards[1].rank)
    max_rank2 = max(h2.cards[0].rank, h2.cards[1].rank)

    if (h1.cards[0].rank == h1.cards[1].rank) and (h2.cards[0].rank != h2.cards[1].rank):
        return True
    if (h1.cards[0].rank != h1.cards[1].rank) and (h2.cards[0].rank == h2.cards[1].rank):
        return False
    if rank1 > rank2:
        return True
    elif rank1 < rank2:
        return False
    else:
        if suit1_sum > suit2_sum:
            return True
        elif suit1_sum < suit2_sum:
            return False
        else:
            if max_rank1 > max_rank2:
                return True
            elif max_rank1 < max_rank2:
                return False
            else:
                if h1.cards[0].rank > h1.cards[1].rank:
                    h1_winCard = 0
                elif h1.cards[0].rank < h1.cards[1].rank:
                    h1_winCard = 1
                else:
                    raise AssertionError

                if h2.cards[0].rank > h2.cards[1].rank:
                    h2_winCard = 0
                elif h2.cards[0].rank < h2.cards[1].rank:
                    h2_winCard = 1
                else:
                    raise AssertionError

                if suit_dict[h1.cards[h1_winCard].suit] > suit_dict[h2.cards[h2_winCard].suit]:
                    return True
                elif suit_dict[h1.cards[h1_winCard].suit] < suit_dict[h2.cards[h2_winCard].suit]:
                    return False
                else:
                    raise AssertionError

array = [hand1, hand2, hand3, hand4, hand5]

k = int(k)
for i in range(len(array)):
    winner = True
    for j in range(len(array)):
        if i == j:
            pass
        elif compare(array[i], array[j]):
            winner = winner and True
        else:
            winner = winner and False
    if winner:
        if k == i + 1:
            print('Win')
        else:
            print('Lose')
        break