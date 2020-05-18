import random
from os import system
import threading
from multiprocessing import Process, current_process, Manager, Pool

# runtime variables
deals = 100


# indexes of cards for each line
l1 = [0,5,10,15]
l2 = [0,1,2,3]
l3 = [4,5,6,7]
l4 = [8,9,10,11]
l5 = [12,13,14,15]
l6 = [12,9,6,3]
l7 = [13,9,5,1]
l8 = [14,10,6,2]
l9 = [15,11,7,3]
l10 = [15,10,5,0]
l11 = [11,10,9,8]
l12 = [7,6,5,4]
l13 = [3,2,1,0]
l14 = [3,6,9,12]
l15 = [2,6,10,14]
l16 = [0,4,8,12]
l17 = [12,8,4,0]
l18 = [15,14,13,12]
l19 = [3,7,11,15]
l20 = [1,5,9,13]
lines = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20]

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
WILD = 'Wild'

stats = {
    '3xbar': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':10
    },
    '4xbar': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':30
    },
    '3xbar2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':25
    },
    '4xbar2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':75
    },
    '3xMelon': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':10
    },
    '4xMelon': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':30
    },
    '3xCoin': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':15
    },
    '4xCoin': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':45
    },
    '3xCrown': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':25
    },
    '4xCrown': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':75
    },
    '3xcherry': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':5
    },
    '4xcherry': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':15
    },
    '3xcherry2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':15
    },
    '4xcherry2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':75
    },
    '3xSeven': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':25
    },
    '4xSeven': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':75
    },
    '3xSeven3': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':50
    },
    '4xSeven3':{
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':250
    },
}

def get_triple_payout(card):
    return stats['3x' + card]['payout']

def get_quadruple_payout(card):
    return stats['4x' + card]['payout']

def deal_sixteen(remaining_cards):
    played= []
    for i in range(0,16):
        card = random.choice(remaining_cards)
        remaining_cards.remove(card)
        played.append(card)
    return played, remaining_cards


def deal_new_card(remaining_cards):
    card = random.choice(remaining_cards)
    remaining_cards.remove(card)
    return card, remaining_cards

def winning_lines(hand):
    winning_rows = []
    for line in lines:
        if hand[line[0]] == hand[line[1]] or hand[line[0]] == WILD or hand[line[1]] == WILD:
            if hand[line[2]] == hand[line[1]] or hand[line[2]] == hand[line[0]] or hand[line[2]] == WILD:
                if hand[line[3]] == hand[line[1]] or hand[line[3]] == hand[line[2]] or hand[line[3]] == hand[line[0]] or hand[line[3]] == WILD:
                    if hand[line[0]] != WILD:
                        winning_rows.append('4x' + hand[line[0]])
                        # print(hand[line[0]] + ' ' + hand[line[1]] + ' ' + hand[line[2]] + ' ' + hand[line[3]] + '==== 4')
                    else:
                        winning_rows.append('4x' + hand[line[1]])
                        # print(hand[line[0]] + ' ' + hand[line[1]] + ' ' + hand[line[2]] + ' ' + hand[line[3]] + '==== 4')
                else:
                    if hand[line[0]] != WILD:
                        winning_rows.append('3x' + hand[line[0]])
                        # print(hand[line[0]] + ' ' + hand[line[1]] + ' ' + hand[line[2]] + ' ' + hand[line[3]] + '==== 3')
                    else:
                        winning_rows.append('3x' + hand[line[1]])
                        # print(hand[line[0]] + ' ' + hand[line[1]] + ' ' + hand[line[2]] + ' ' + hand[line[3]] + '==== 3')
    return winning_rows            

def reset_cards():
    cards = ['cherry', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry',
            'cherry2', 'cherry2', 'cherry2', 'cherry2', 'cherry2', 'cherry2',
            'bar', 'bar', 'bar', 'bar', 'bar', 'bar', 'bar',
            'bar2', 'bar2', 'bar2', 'bar2',
            'Melon', 'Melon', 'Melon', 'Melon', 'Melon', 'Melon', 'Melon',
            'Crown', 'Crown', 'Crown', 'Crown',
            'Seven', 'Seven', 'Seven', 'Seven',
            'Coin', 'Coin', 'Coin', 'Coin', 'Coin', 'Coin',
            'Seven3', 'Seven3', 'Seven3',
            'Wild']
    return cards

def print_best_hand_stats(end_stats, round):
    maxrtp = 0
    print("{:<15s}{:>15s}{:>15s}{:>15s}".format("Card","Hits","Probability","RTP"))
    for key, value in end_stats.items():
        maxrtp = maxrtp + value['bestPlayHits']/(round * deals)*value['payout']/20
        print("{:<15s}{:>15d}{:>15f}{:>15f}".format(key,value['bestPlayHits'],value['bestPlayHits']/(round * deals),value['bestPlayHits']/(round * deals)*value['payout']/20))
    print("MAX RTP: {}".format(maxrtp))


def calculate_payout_deal(array):
    total = 0
    for item in array:
        if item[0] == '3':
            total = total + get_triple_payout(str(item[2:]))
        if item[0] == '4':
            total = total + get_quadruple_payout(str(item[2:]))
    return total

def add_to_best_stats(array, process_stats):
    for item in array:
        if item[0] == '3':
            process_stats[item]['bestPlayHits'] = process_stats[item]['bestPlayHits'] + 1
        if item[0] == '4':
            process_stats[item]['bestPlayHits'] = process_stats[item]['bestPlayHits'] + 1

def run_analysis(process_stats):
    cards = reset_cards()
    lines = 20
    max_rtp = 0
    best_winning_array_of_deals = []
    best_mask = 0
    # initial deal of 9 cards
    initial_deal, cards = deal_sixteen(cards)

    # Loop through 512 masks for the 9 initial cards
    for mask in bitmasks:
        # print("MASK: {}, Process: {}".format(mask, current_process()))
        # copy original 9
        same_sixteen = initial_deal.copy()
        rtp = 0
        deal = 0
        best_strategy = []
        winning_arrays_per_deal = []
        
        # Loop through X amount of deals for each bitmask for the initial 9 cards
        while(deal < deals):
            # make copy of remaining cards
            remaining_cards = cards.copy()
            deal = deal + 1
            mask_total = 0
            for i in range(len(mask)):
                if mask[i] == str(1):
                    new_card, remaining_cards = deal_new_card(remaining_cards)
                    same_sixteen[i] = new_card
            winning_arrays_per_deal.append(winning_lines(same_sixteen))
        # print(winning_arrays_per_deal)
        for array_winnings in winning_arrays_per_deal:
            rtp = rtp + calculate_payout_deal(array_winnings)
        rtp = rtp / (lines * deals)
        if rtp > max_rtp:
            max_rtp = rtp
            best_mask = mask
            best_winning_array_of_deals = winning_arrays_per_deal
    for array in best_winning_array_of_deals:
        # print(len(best_winning_array_of_deals))
        add_to_best_stats(array, process_stats)
        # print_best_hand_stats(stats, 10*16)
 

def run_multi_thread(stats):
    round = 0
    rounds = 1000
        # for num in range(65537):
#
    for num in range(6553):
        bitmasks.append(bin(num)[2:].zfill(16))

    while round < rounds:
        round = round + 1
        print("Round: {}, Process: {}".format(round, current_process()))
        run_analysis(stats)
        print("#######################################")
        print_best_hand_stats(stats, round)
        print("Round: {}, Current Thread: {}".format(round, threading.current_thread().name))

if __name__ == '__main__':

    manager = Manager()
    shared_stats = manager.dict()

    
    for i in range(9):
        Process(target=run_multi_thread, name='Thread '+str(i), args=[stats]).start()

    # print(stats)

    # print_best_hand_stats(stats, 10*16)