from hashlib import new
import random

# J, Q, K = 10, A = 1 or 11
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

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
        self.deck = []

        # create a card object for each rank in each suit
        # and add to all cards list
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)
        
    def __str__(self):
        deck_output = ''
        for card in self.deck:
            deck_output += '\n' + card.__str__()

        return 'The deck has:' + deck_output

    # use random to shuffle all cards
    def shuffle(self):
        random.shuffle(self.deck)

    # deal a card - pop a card from the deck
    def deal(self):
        return self.deck.pop()
        
# class for a hand, storing the cards, value and number of aces
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    # add a card, and its value - if it is an ace, increment number of aces
    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1

    # check whether we want our ace to be 1 or 11, and decrement number of aces
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# class to keep track of number of chips a player has
class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    # if a player wins the bet, add the bet to the total number of chips
    def win_bet(self):
        self.total += self.bet
    
    # if a player loses the bet, remove the bet from the total number of chips
    def lose_bet(self):
        self.total -= self.bet

# function to take a bet from the user
def take_bet(chips):
    while True:
        try:
            bet = int(input('How much would you like to bet? '))
        except ValueError:
            print('Must be an integer!')
        else:    
            if chips.bet > chips.total:
                print('Insufficient funds!')
            else:
                break

# function to take a hit i.e call for another card
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# function to ask user whether they want to hit or stand
def hit_or_stand(deck, hand):
    global playing
    choice = ' '
    while True:
        choice = input('Would you like to hit or stand? \'Y\' or \'N\' ')
        if choice == 'Y':
            playing = True
            hit(deck, hand)
        elif choice == 'N':
            print('Player stands, the dealers turn') 
            playing = False
        else:
            print('Try again')
            continue
        break

# hide all but the first card of the dealers hand, show all players hand
def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
# show all cards in both hands
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

# functions to add/remove chips depending on who has won/gone bust
def player_busts(player, dealer, chips):
    print('Player has gone bust!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player has won!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Dealer has gone bust!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Dealer has won!')
    chips.lose_bet()

# push when the game is a tie
def push(player,dealer):
    print("Dealer and player tie! It's a push.")

while True:
    print('Welcome to blackjack!')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)
    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        # if players hand is > 21, they bust
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
        
    # if player hasn't busted, play dealers hand until they reach 17
    if dealer_hand.value  <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # reveal all cards
        show_all(player_hand, dealer_hand)
        
        # different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # tell player how many chips they have left
    print('You have {} chips remaining'.format(player_chips.total))
    new_game_choice = input('Would you like to play another hand? Enter \'Y\' or \'N\' ')
    
    # ask if the player would like to play again
    if new_game_choice =='Y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
