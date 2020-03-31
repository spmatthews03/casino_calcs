import random
from os import system
# indexes of cards for each line
l1 = [0,4,8]
l2 = [0,1,2]
l3 = [3,4,5]
l4 = [6,7,8]
l5 = [6,4,2]
l6 = [6,3,0]
l7 = [7,4,1]
l8 = [8,5,2]
l9 = [8,4,0]
l10 = [8,7,6]
l11 = [5,4,3]
l12 = [2,1,0]
l13 = [2,4,6]
l14 = [2,5,8]
l15 = [1,4,7]
l16 = [0,3,6]
lines = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16]

bitmasks = []

CHERRY = 'cherry'
CHERRY2 = 'cherry2'
BAR = 'bar'
BAR2 = 'bar2'
MELON = 'Melon'
CROWN = 'Crown'
SEVEN = 'Seven'
COIN = 'Coin'
SEVEN3 = 'Seven3'

stats = {
    '2xbar': 0,
    '3xbar': 0,
    '2xbar2': 0,
    '3xbar2': 0,
    '2xmelon': 0,
    '3xmelon': 0,
    '2xcoin': 0,
    '3xcoin': 0,
    '2xcrown': 0,
    '3xcrown': 0,
    '2xcherry': 0,
    '3xcherry': 0,
    '2xcherry2': 0,
    '3xcherry2': 0,
    '2xseven': 0,
    '3xseven': 0,
    '2xseven3': 0,
    '3xseven3': 0
}

times_hit = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0
}

def get_double_payout(card):
    if card in [BAR, MELON]:
        return 2
    elif card in [BAR2, CROWN, SEVEN]:
        return 6
    elif card in [COIN, CHERRY2]:
        return 4
    elif card is CHERRY:
        return 1
    elif card is SEVEN3:
        return 10

def get_triple_payout(card):
    if card in [BAR, MELON]:
        return 20
    elif card in [BAR2, CROWN, SEVEN]:
        return 60
    elif card in [COIN, CHERRY2]:
        return 40
    elif card is CHERRY:
        return 10
    elif card is SEVEN3:
        return 100

def deal_nine(remaining_cards):
    played= []
    for i in range(0,9):
        card = random.choice(remaining_cards)
        remaining_cards.remove(card)
        played.append(card)
    return played, remaining_cards


def deal_new_card(remaining_cards):
    card = random.choice(remaining_cards)
    remaining_cards.remove(card)
    return card, remaining_cards

def calculate_payout(hand):
    total = 0
    for line in lines:
        line_total = 0 
        if hand[line[0]] == hand[line[1]]:
            if hand[line[1]] == hand[line[2]]:
                line_total = line_total + get_triple_payout(hand[line[0]])
                # print("Triple Payout with: {}".format(hand[line[0]]))
            else:
                line_total = line_total + get_double_payout(hand[line[0]])
                # print("Double Payout with: {}".format(hand[line[0]]))
            total = line_total
    return total

def reset_cards():
    cards = ['cherry', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry',
            'cherry2', 'cherry2', 'cherry2', 'cherry2', 'cherry2', 'cherry2',
            'bar', 'bar', 'bar', 'bar', 'bar', 'bar', 'bar',
            'bar2', 'bar2', 'bar2', 'bar2',
            'Melon', 'Melon', 'Melon', 'Melon', 'Melon', 'Melon', 'Melon',
            'Crown', 'Crown', 'Crown', 'Crown',
            'Seven', 'Seven', 'Seven', 'Seven',
            'Coin', 'Coin', 'Coin', 'Coin', 'Coin', 'Coin',
            'Seven3', 'Seven3', 'Seven3']
    return cards



def run_analysis():
    deals = 100
    lines = 16
    average_payout = 0
    max_rtp = 0
    for mask in bitmasks:
        rtp = 0
        round_for_mask = 0
        while(round_for_mask < deals):
            round_for_mask = round_for_mask + 1
            cards = reset_cards()
            player_hand, cards = deal_nine(cards)
            mask_total = 0
            for i in range(len(mask)):
                if mask[i] == str(1):
                    new_card, cards = deal_new_card(cards)
                    player_hand[i] = new_card
            rtp = rtp +  calculate_payout(player_hand)
        rtp = rtp / (lines * deals)
        print(rtp)
        if rtp > max_rtp:
            max_rtp = rtp
            print("Best Total for bitmask: {}".format(max_rtp))
        system('clear')
        print("#######################################")
        print("Bitmask: {}".format(mask))
        print("Max RTP: {}".format(max_rtp))
        print("########################################")

# def print_stats():
    # print("Round: {}, Average Payout: {}, percent: {} %"
        #       .format(round,num_bonus_rounds,str(float(num_bonus_rounds)/float(round) * 100)))


if __name__ == '__main__':
    round = 0

    for num in range(513):
        bitmasks.append(bin(num)[2:].zfill(9))

    while round < 2:
        round = round + 1
        run_analysis()
        # print_stats()
        # print("Round: {}, Average Payout: {}, percent: {} %"
        #       .format(round,num_bonus_rounds,str(float(num_bonus_rounds)/float(round) * 100)))
