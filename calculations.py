import random


stats = {
    'cherry': 0,
    # 'cherry2': 0,
    'bar': 0,
    # 'bar2': 0,
    'Melon': 0,
    'Crown': 0,
    'zero': 0,
    # 'Seven': 0,
    # 'Coin': 0,
    # 'Seven3': 0
}

bb_perc = .0261248186
num_bonus_rounds = 0
times_hit = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0
}


# def deal_nine(remaining_cards):
#     played= []
#     for i in range(0,9):
#         card = random.choice(remaining_cards)
#         remaining_cards.remove(card)
#         played.append(card)
#     return played, remaining_cards
#
#
# def deal_seven(remaining_cards):
#     played= []
#     for i in range(0,7):
#         card = random.choice(remaining_cards)
#         remaining_cards.remove(card)
#         played.append(card)
#     return played, remaining_cards

def deal_4(remaining_cards):
    played= []
    for i in range(0,4):
        card = random.choice(remaining_cards)
        remaining_cards.remove(card)
        played.append(card)
    return played, remaining_cards


def deal_4(remaining_cards):
    played= []
    for i in range(0,4):
        card = random.choice(remaining_cards)
        remaining_cards.remove(card)
        played.append(card)
    return played, remaining_cards

def run_analysis():
    # cards = ['cherry', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry',
    #          'cherry2', 'cherry2', 'cherry2', 'cherry2', 'cherry2', 'cherry2',
    #          'bar', 'bar', 'bar', 'bar', 'bar', 'bar', 'bar',
    #          'bar2', 'bar2', 'bar2', 'bar2',
    #          'Melon', 'Melon', 'Melon', 'Melon', 'Melon', 'Melon', 'Melon',
    #          'Crown', 'Crown', 'Crown', 'Crown',
    #          'Seven', 'Seven', 'Seven', 'Seven',
    #          'Coin', 'Coin', 'Coin', 'Coin', 'Coin', 'Coin',
    #          'Seven3', 'Seven3', 'Seven3',
    #          'Wild',
    #          'Jackpot',
    #          'Bonus','Bonus']

    cards = ['cherry', 'cherry','cherry','cherry',
             'bar', 'bar', 'bar', 'bar', 'bar','bar','bar', 'bar', 'bar', 'bar', 'bar','bar',
             'Melon', 'Melon',
             'Crown', 'Crown', 'Crown', 'Crown', 'Crown', 'Crown']

    # first_nine, cards = deal_nine(cards)
    # count = 0
    # for card in first_nine:
    #     if card is 'Bonus':
    #         count = count + 1
    #
    # if count == 2:
    #     global num_bonus_rounds
    #     num_bonus_rounds = num_bonus_rounds + 1
    #     second_seven, cards = deal_seven(cards)
    #     first_seven =[]
    #     first_seven[:] = [x for x in first_nine if x != 'Bonus']
    #
    #     for card1, card2 in zip(first_nine,second_seven):
    #         if card1 == card2:
    #             stats[card1] = stats[card1] + 1
    #         if card1 is 'Wild' and card2 not in ['Jackpot','Bonus']:
    #             stats[card2] = stats[card2] + 1
    #         if card2 is 'Wild' and card1 not in ['Jackpot','Bonus']:
    #             stats[card1] = stats[card1] + 1
    #
    #
    # list = {}
    # print(stats)
    # for item in stats:
    #     list[item] = float(stats[item]/round)
    # print(list)

    first_4, cards = deal_4(cards)


    second_4, cards = deal_4(cards)
    print(first_4)
    print(second_4)
    num_hits = 0

    for card1, card2 in zip(first_4,second_4):
        if card1 == card2:
            stats[card1] = stats[card1] + 1
            num_hits = num_hits + 1

    if num_hits > 0:
        times_hit[str(num_hits)] = times_hit[str(num_hits)] + 1
    else:
        stats['zero'] = stats[card1] + 1
        times_hit[str(num_hits)] = times_hit[str(num_hits)] + 1



    list = {}
    print(times_hit)
    print(stats)
    for item in stats:
        list[item] = float(stats[item]/round)
    print(list)


if __name__ == '__main__':
    round = 0
    while round < 100000:
        round = round + 1
        run_analysis()
        print("Round: {}"
              .format(round))

# if __name__ == '__main__':
#     round = 0
#     while True:
#         round = round + 1
#         run_analysis()
#         print("Round: {}, Bonus Rounds: {}, percent: {} %"
#               .format(round,num_bonus_rounds,str(float(num_bonus_rounds/round * 100))))
