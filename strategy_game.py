import random
from os import system

# runtime variables
deals = 100
round = 0



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
        'payout':20
    },
    '2xbar2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':6
    },
    '3xbar2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':60
    },
    '2xMelon': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':2
    },
    '3xMelon': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':20
    },
    '2xCoin': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':4
    },
    '3xCoin': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':40
    },
    '2xCrown': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':6
    },
    '3xCrown': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':60
    },
    '2xcherry': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':1
    },
    '3xcherry': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':10
    },
    '2xcherry2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':4
    },
    '3xcherry2': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':40
    },
    '2xSeven': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':6
    },
    '3xSeven': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':60
    },
    '2xSeven3': {
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':10
    },
    '3xSeven3':{
        'bestPlayHits': 0,
        'overallHits':0,
        'payout':100
    },
}

times_hit = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0
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
                winning_rows.append('3x' + hand[line[2]])
            else:
                winning_rows.append('2x' + hand[line[2]])
    return winning_rows            


def calculate_payout(hand):
    total = 0
    for line in lines:
        line_total = 0 
        if hand[line[0]] == hand[line[1]]:
            if hand[line[1]] == hand[line[2]]:
                line_total = line_total + get_triple_payout(hand[line[0]])
            else:
                line_total = line_total + get_double_payout(hand[line[0]])
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

def print_overall_stats():
    maxrtp = 0
    for key, value in stats.items():
        maxrtp = maxrtp + value['overallHits']/(512 * round * deals)*value['payout']
        print("{}: {} hits, Probability: {}, RTP: {}".format(key, value['overallHits'], value['overallHits']/(512 * round * deals), value['overallHits']/(512 * round * deals)*value['payout']))
    print("MAX RTP OVERALL: {}".format(maxrtp))

def print_best_hand_stats():
    maxrtp = 0
    for key, value in stats.items():
        maxrtp = maxrtp + value['bestPlayHits']/(512 * round * deals)*value['payout']
        print("{}: {} hits, Probability: {}, RTP: {}".format(key, value['bestPlayHits'], value['bestPlayHits']/(round * deals), value['bestPlayHits']/(round * deals)*value['payout']))
    print("MAX RTP BEST HAND: {}".format(maxrtp))


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

def add_to_overall_stats(array):
    for item in array:
        if item[0] == '2':
            stats[item]['overallHits'] = stats[item]['overallHits'] + 1
        if item[0] == '3':
            stats[item]['overallHits'] = stats[item]['overallHits'] + 1

def run_analysis():
    lines = 16
    average_payout = 0
    max_rtp = 0
    
    for mask in bitmasks:
        system('clear')
        best_strategy = []
        rtp = 0
        winning_arrays_per_deal = []
        
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
            winning_arrays_per_deal.append(winning_lines(player_hand))
        for array_winnings in winning_arrays_per_deal:
            rtp = calculate_payout_deal(array_winnings)
            add_to_overall_stats(array_winnings)
            rtp = rtp / (lines * deals)
            if rtp > max_rtp:
                max_rtp = rtp
                best_strategy = array_winnings
        add_to_best_stats(best_strategy)
        print("#######################################")
        print("Bitmask: {}".format(mask))
        # print("Max RTP: {}".format(max_rtp))
        print("########################################")
        print("#######################################")
        print("OVERALL STATS (EVERY DISCARD ON EVERY HAND)")
        print_overall_stats()
        print("#######################################")
        print("BEST HAND STATS (BEST OUTCOME FOR EACH DEAL FOR EACH BITMASK")
        print_best_hand_stats()
 

# def print_stats():
    # print("Round: {}, Average Payout: {}, percent: {} %"
        #       .format(round,num_bonus_rounds,str(float(num_bonus_rounds)/float(round) * 100)))


if __name__ == '__main__':
    for num in range(513):
        bitmasks.append(bin(num)[2:].zfill(9))

    while round < 1000:
        round = round + 1
        run_analysis()
        # print_stats()
        # print("Round: {}, Average Payout: {}, percent: {} %"
        #       .format(round,num_bonus_rounds,str(float(num_bonus_rounds)/float(round) * 100)))
