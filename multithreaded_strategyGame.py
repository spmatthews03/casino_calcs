import random
from os import system
from multiprocessing import Process, current_process

# runtime variables
deals = 100
# round = 0
# rounds = 10000000

avgRTP=0


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
    '2xbar': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':2
    },
    '3xbar': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':12
    },
    '2xbar2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':5
    },
    '3xbar2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':30
    },
    '2xMelon': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':2
    },
    '3xMelon': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':12
    },
    '2xCoin': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':3
    },
    '3xCoin': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':15
    },
    '2xCrown': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':5
    },
    '3xCrown': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':30
    },
    '2xcherry': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':1
    },
    '3xcherry': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':8
    },
    '2xcherry2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':3
    },
    '3xcherry2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':15
    },
    '2xSeven': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':5
    },
    '3xSeven': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':30
    },
    '2xSeven3': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':7
    },
    '3xSeven3':{
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':100
    },
}

def get_double_payout(card):
    return stats['2x' + card]['payout']

def get_triple_payout(card):
    return stats['3x' + card]['payout']

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

def winning_lines(hand):
    winning_rows = []
    for line in lines:
        if hand[line[0]] == hand[line[1]]:
            if hand[line[1]] == hand[line[2]]:
                winning_rows.append('3x' + hand[line[0]])
            else:
                winning_rows.append('2x' + hand[line[0]])
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
            'Seven3', 'Seven3', 'Seven3']
    return cards

def print_best_hand_stats(round):
    maxrtp = 0
    print("{:<15s}{:>15s}{:>15s}{:>15s}".format("Card","Hits","Probability","RTP"))
    global stats
    for key, value in stats.items():
        maxrtp = maxrtp + value['bestPlayHits']/(round * deals)*value['payout']/16
        print("{:<15s}{:>15d}{:>15f}{:>15f}".format(key,value['bestPlayHits'],value['bestPlayHits']/(round * deals),value['bestPlayHits']/(round * deals)*value['payout']/16))
    print("MAX RTP: {}".format(maxrtp))


def calculate_payout_deal(array):
    total = 0
    for item in array:
        if item[0] == '2':
            total = total + get_double_payout(str(item[2:]))
        if item[0] == '3':
            total = total + get_triple_payout(str(item[2:]))
    return total

def add_to_best_stats(array):
    for item in array:
        if item[0] == '2':
            stats[item]['bestPlayHits'] = stats[item]['bestPlayHits'] + 1
        if item[0] == '3':
            stats[item]['bestPlayHits'] = stats[item]['bestPlayHits'] + 1

def run_analysis():
    cards = reset_cards()
    lines = 16
    max_rtp = 0
    best_winning_array_of_deals = []
    best_mask = 0
    # initial deal of 9 cards
    initial_deal, cards = deal_nine(cards)

    # Loop through 512 masks for the 9 initial cards
    for mask in bitmasks:
        # copy original 9
        same_nine = initial_deal.copy()
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
                    same_nine[i] = new_card
            winning_arrays_per_deal.append(winning_lines(same_nine))
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
        add_to_best_stats(array)
    

 

def run_multi_thread():
    round = 0
    rounds = 100
    for num in range(513):
        bitmasks.append(bin(num)[2:].zfill(9))

    while round < rounds:
        round = round + 1
        print("#######################################")
        print("Round: {}, Process: {}".format(round, current_process()))
        run_analysis()
        print_best_hand_stats(round)

if __name__ == '__main__':

    p1 = Process(target=run_multi_thread, name='Thread 1')
    p2 = Process(target=run_multi_thread, name='Thread 2')
    p3 = Process(target=run_multi_thread, name='Thread 3')
    p4 = Process(target=run_multi_thread, name='Thread 4')
    p5 = Process(target=run_multi_thread, name='Thread 5')
    p6 = Process(target=run_multi_thread, name='Thread 6')
    p7 = Process(target=run_multi_thread, name='Thread 7')
    p8 = Process(target=run_multi_thread, name='Thread 8')
    p9 = Process(target=run_multi_thread, name='Thread 9')
    p10 = Process(target=run_multi_thread, name='Thread 10')
    p11 = Process(target=run_multi_thread, name='Thread 11')
    p12 = Process(target=run_multi_thread, name='Thread 12')
    p13 = Process(target=run_multi_thread, name='Thread 13')
    p14 = Process(target=run_multi_thread, name='Thread 14')
    p15 = Process(target=run_multi_thread, name='Thread 15')
    p16 = Process(target=run_multi_thread, name='Thread 16')

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p13.start()
    p14.start()
    p15.start()
    p16.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    p11.join()
    p12.join()
    p13.join()
    p14.join()
    p15.join()
    p16.join()

