import random

# initialise suits, ranks and values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# class for a card - value is obtained by referencing to dictionary of values
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# class for a deck, made up of 52 cards
class Deck:

    def __init__(self):
        self.all_cards = []

        # create a card object for each rank in each suit
        # and add to all cards list
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    # use random to shuffle deck
    def shuffle(self):
        random.shuffle(self.all_cards)

    # deal a deck removing one card from the deck
    def deal_one(self):
        return self.all_cards.pop()

# class for a player
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # method to remove a card, removing the leftmost (top) card from the hand
    def remove_one(self):
        return self.all_cards.pop(0)

    # method to add a card, adding to the right (bottom) of the hand
    def add_cards(self, new_cards):
        # check if new_cards is of type list
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # check if new_cards is singular
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

# main method to play the game
def __main__():
    p1 = Player('p1')
    p2 = Player('p2')

    new_deck = Deck()
    new_deck.shuffle()

    # deal 26 cards to each player
    for i in range(26):
        p1.add_cards(new_deck.deal_one())
        p2.add_cards(new_deck.deal_one())

    # condition to check if game is still playing
    game_playing = True
    round_num = 0

    # while the game_playing condition is True, play the game
    while game_playing:
        round_num += 1
        print('currently on round {}'.format(round_num))

        # check if either player has lost the game - 0 cards in hand
        if len(p1.all_cards) == 0:
            print('Player 1 out of cards, player two wins!')
            game_playing = False
            break
        elif len(p1.all_cards) == 0:
            print('Player 1 out of cards, player two wins!')
            game_playing = False
            break

        # current cards in play
        p1_cards = []
        p1_cards.append(p1.remove_one())

        p2_cards = []
        p2_cards.append(p2.remove_one())

        # assume players are at war (when the two cards == each other)
        at_war = True
        # break out of war when the two cards aren't equal to each other
        while at_war:
            if p1_cards[-1].value > p2_cards[-1].value:
                p1.add_cards(p1_cards)
                p1.add_cards(p2_cards)
                at_war = False
            elif p1_cards[-1].value < p2_cards[-1].value:
                p2.add_cards(p1_cards)
                p2.add_cards(p2_cards)
                at_war = False
            else:
                print('WAR!')

                if len(p1.all_cards) < 5:
                    print('Player one unable to declar war')
                    print('Player two wins')
                    game_playing = False
                    break
                elif len(p2.all_cards) < 5:
                    print('Player two unable to declar war')
                    print('Player one wins')
                    game_playing = False
                    break
                else:
                    for num in range(5):
                        p1_cards.append(p1.remove_one())
                        p2_cards.append(p2.remove_one())

__main__()
