import random
from os import system

# runtime variables
rerolls = 100
round = 0
rounds = 10000000

bitmasks = []

CHERRY = 'cherry'
BAR = 'bar'
SEVEN = 'seven'
COIN = 'coin'
SEVEN3 = 'seven3'
WILD = 'wild'

symbols = [CHERRY,BAR,SEVEN,COIN,SEVEN3]


# indexes of cards for each line
d1 = [SEVEN,SEVEN3,COIN,COIN,CHERRY,BAR]
d2 = [SEVEN,SEVEN3,COIN,BAR,BAR,CHERRY]
d3 = [SEVEN,SEVEN3,COIN,BAR,BAR,CHERRY]
d4 = [SEVEN,SEVEN3,COIN,BAR,CHERRY,CHERRY]
d5 = [SEVEN,SEVEN3,COIN,BAR,CHERRY,CHERRY]
d6 = [SEVEN,COIN,CHERRY,CHERRY,BAR,WILD]

die = [d1, d2, d3, d4, d5, d6]




dice_info = {
    'bar': {
        '4': {
            'hits':0,
            'payout':0
        },
        '5': {
            'hits':0,
            'payout':3
        },
        '6': {
            'hits':0,
            'payout':12
        }
    },
    'cherry': {
        '4': {
            'hits':0,
            'payout':0
        },
        '5': {
            'hits':0,
            'payout':2
        },
        '6': {
            'hits':0,
            'payout':8
        }
    },
    'coin': {
        '4': {
            'hits':0,
            'payout':1
        },
        '5': {
            'hits':0,
            'payout':4
        },
        '6': {
            'hits':0,
            'payout':20
        }
    },
    'seven': {
        '4': {
            'hits':0,
            'payout':2
        },
        '5': {
            'hits':0,
            'payout':6
        },
        '6': {
            'hits':0,
            'payout':40
        }
    },
    'seven3': {
        '4': {
            'hits':0,
            'payout':3
        },
        '5': {
            'hits':0,
            'payout':10
        },
        '6': {
            'hits':0,
            'payout':75
        }
    }
}

def roll_six(die):
    rolled = []
    for di in die:
        rolled_di = random.choice(di)
        rolled.append(rolled_di)
    return rolled

def reroll_di(di):
    rolled_di = random.choice(di)
    return rolled_di

def winning_rolls(die):
    winning_rolls = []
    contains_wild = WILD in die

    for symbol in symbols:
        if die.count(symbol) == 3 and contains_wild or die.count(symbol) == 4 and not contains_wild:
            winning_rolls.append('4x' + symbol)
        if die.count(symbol) == 4 and contains_wild or die.count(symbol) == 5 and not contains_wild:
            winning_rolls.append('5x' + symbol)
        if die.count(symbol) == 5 and contains_wild or die.count(symbol) == 6 and not contains_wild:
            winning_rolls.append('6x' + symbol)
    return winning_rolls            


def print_best_roll_stats():
    maxrtp = 0
    print("{:<15s}{:>15s}{:>15s}{:>15s}".format("Event","Hits","Probability","RTP"))
    for key, value in dice_info.items():
        for num,data in value.items():
            print("{:<15s}{:>15d}{:>15f}{:>15f}".format(num+'x'+key,data['hits'],data['hits']/(round * rerolls),data['hits']/(round * rerolls)*data['payout']))
            maxrtp = maxrtp + data['hits']/(round * rerolls)*data['payout']
    print("MAX RTP: {}".format(maxrtp))


def calculate_payout(array):
    total = 0
    for item in array:
        total = total + dice_info[item[2:]][item[0]]['payout']
    return total

def add_to_best_stats(array):
    for item in array:
        if item[0] == '4':
            dice_info[item[2:]]['4']['hits'] = dice_info[item[2:]]['4']['hits'] + 1
        if item[0] == '5':
            dice_info[item[2:]]['5']['hits'] = dice_info[item[2:]]['5']['hits'] + 1
        if item[0] == '6':
            dice_info[item[2:]]['6']['hits'] = dice_info[item[2:]]['6']['hits'] + 1


def run_analysis():
    di = die.copy()
    max_rtp = 0
    best_winning_di = []
    best_mask = 0
    # initial roll of 6 di
    initial_roll = roll_six(di)

    # Loop through 64 masks for the 6 initial di
    for mask in bitmasks:
        # copy original 6
        same_six = initial_roll.copy()
        rtp = 0
        reroll = 0
        best_strategy = []
        winning_arrays_per_roll = []
        
        # Loop through X amount of deals for each bitmask for the initial 6 rolled di
        while(reroll < rerolls):
            # make copy of remaining cards
            reroll = reroll + 1
            mask_total = 0
            for i in range(len(mask)):
                if mask[i] == str(1):
                    same_six[i] = reroll_di(di[i])
            winning_arrays_per_roll.append(winning_rolls(same_six))
        for array_winnings in winning_arrays_per_roll:
            rtp = rtp + calculate_payout(array_winnings)
        rtp = rtp / (rerolls)
        if rtp > max_rtp:
            max_rtp = rtp
            best_mask = mask
            best_winning_di = winning_arrays_per_roll
    for array in best_winning_di:
        add_to_best_stats(array)
    print("#######################################")
    print_best_roll_stats()
    print("Round: {}".format(round))
 

if __name__ == '__main__':
    for num in range(65):
        bitmasks.append(bin(num)[2:].zfill(6))

    while round < rounds:
        round = round + 1
        run_analysis()

