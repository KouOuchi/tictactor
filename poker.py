import random
import os
import sys

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def card_figure(suit, rank):

    suit_char = "♠"
    if suit == 1:
        suit_char = "♣"
    elif suit == 2:
        suit_char = "♥"
    elif suit == 3:
        suit_char = "♦"

    rank_char = ""
    if rank == 11:
        rank_char = "J"
    elif rank == 12:
        rank_char = "Q"
    elif rank == 13:
        rank_char = "K"
    else:
        rank_char = str(rank)

    lines = []
    lines.append("+--+")
    lines.append("|%2s|" % suit_char)
    lines.append("|%2s|" % rank_char)
    lines.append("+--+")

    return lines

def print_deck(deck):
    """

    """

    output_lines = ["", "", "", ""] 
    for card in deck:
        lines = card_figure(card[0], card[1])

        for i in range(4):
            output_lines[i] += lines[i]
            output_lines[i] += " "

    for i in range(4):
        print(output_lines[i])  

def print_hand(hand):

    print('')
    if hand == 'none':
        print('You lose...') 
    else:
        print('You win!!! : ' + hand) 

def draw_one_card():
    """
    draw 5 cards to deck
    """
    
    # get suit
    suit = random.randint(0, 3)

    # get rank
    rank = random.randint(1, 13)

    return suit, rank

def draw_deck():
    """
    """
    
    deck = []

    while len(deck) <= 4:
        suit, rank = draw_one_card()

        # check duplicate
        duplicate = False
        for deck_suit, deck_rank in deck:
            if deck_suit == suit and deck_rank == rank:
                duplicate = True
                break

        if not duplicate:
            deck.append( (suit, rank) )
            

    return deck

def check_hand(deck):
    """
    
    """

    hand_list = []

    for i in range(13):
        test_rank = i + 1
        match_count = 0
        for suit, rank in deck:
            if rank == test_rank:
                match_count += 1
            
        if match_count == 2:
            hand_list.append('one pair')
            
        if match_count == 3:
            hand_list.append('three card')

        if match_count == 4:
            hand_list.append('four card')

    hand = ''
    if len(hand_list) == 0:
        hand = 'none'
    elif len(hand_list) == 1:
        if hand_list.count('one pair') == 1:
            hand = 'none'
        else:
            hand = hand_list[0]
    elif len(hand_list) == 2:
        if hand_list.count('one pair') == 2:
            hand = 'two pair'
        elif ('one pair' in hand_list) and ('three card' in hand_list):
            hand = 'full house'

    if hand == '':
        print(hand_list)
        print(deck)
        raise(RuntimeError('unexpected hand'))

    return hand

def read_int():

    line = None
    while True:
        try:
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            return None
    
        if not line:
            continue

        try: 
            num = int(line) 

            if num > 0:
                return num

        except ValueError:
            pass
        
        sys.stdout.write('input positive number. Or Ctrl-C. : ')
        sys.stdout.flush()

def get_credit():

    sys.stdout.write('Credit of start : ')
    sys.stdout.flush()
    credit = read_int()
    if not credit:
        exit()

    return credit     

def get_bet(credit):

    while True:
        sys.stdout.write('How much do you bet ? : ')
        sys.stdout.flush()
        bet = read_int()
        if not bet:
            exit()
            
        if bet > credit:
            print('Your bet is exceeded.')
        else:
            return bet     

def calc(hand, bet, credit):

    print('')

    calcurated_creadit = credit - bet

    if hand == 'none':
        if calcurated_creadit <= 0:
            print('Collapsed.')
            quit()
    else:
        multiplier = 1
        if hand == 'two pair':
            multiplier = 2
        elif hand == 'three card':
            multiplier = 3
        elif hand == 'full house':
            multiplier = 4
        elif hand == 'four card':
            multiplier = 8

        calcurated_creadit += bet * multiplier

        print('You got %d X %d !!!' % bet % multiplier)

    print('Credit is %d.' % calcurated_creadit)

    return calcurated_creadit

def run_game():
    """ 
    run game
    """

    credit = get_credit()

    while True:

        bet = get_bet(credit)
    
        cls()

        deck = draw_deck()

        hand = check_hand(deck)
        
        print_deck(deck)

        print_hand(hand)

        credit = calc(hand, bet, credit)

"""

"""

run_game()
