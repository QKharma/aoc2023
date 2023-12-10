file = []
with open('day_7_input.txt') as f:
    file = [' '.join(line.strip().split()) for line in f.readlines() if line.strip() != '']

values = [
    '2','3','4','5','6','7','8','9','T','J','Q','K','A'
]

hands = {
    'high_card': [],
    'pair': [],
    'two_pair': [],
    'three_kind': [],
    'full_house': [],
    'four_kind': [],
    'five_kind': [],
}

def calc_value(hand):
    output = ''
    for card in hand[0]:
        value = values.index(card) + 2
        if value <= 9:
            output = '{}0{}'.format(output, value)
        else:
            output = '{}{}'.format(output, value)
    return int(output)

for hand in file:
    hand = hand.split(' ')
    cards = {}
    bid = hand[1]
    for card in hand[0]:
        if not cards.get(card):
            cards[card] = 1
        else:
            cards[card] += 1

    pair = False
    three_kind = False
    card_added = False
    cards = dict(sorted(cards.items(), key=lambda x:x[1], reverse=True))
    for key, card in cards.items():
        if card == 5:
            hands['five_kind'].append([hand, calc_value(hand)])
            card_added = True
            break
        if card == 4:
            hands['four_kind'].append([hand, calc_value(hand)])
            card_added = True
            break
        if card == 3:
            if pair:
                hands['full_house'].append([hand, calc_value(hand)])
                card_added = True
                break
            three_kind = True
            continue
        if card == 2:
            if three_kind:
                hands['full_house'].append([hand, calc_value(hand)])
                card_added = True
                break
            if pair:
                hands['two_pair'].append([hand, calc_value(hand)])
                card_added = True
                break
            pair = True
            continue
    if not card_added and pair:
        hands['pair'].append([hand, calc_value(hand)])
    elif not card_added and three_kind:
        hands['three_kind'].append([hand, calc_value(hand)])
    elif not card_added:
        hands['high_card'].append([hand, calc_value(hand)])


sorted_hands = []

for idx, hand_type in hands.items():
    sorted_type = sorted(hand_type, key=lambda hand: hand[1]) 
    sorted_hands = sorted_hands + sorted_type

result = 0

for idx_sorted_hands in range(len(sorted_hands)):
    result += int(sorted_hands[idx_sorted_hands][0][1]) * (idx_sorted_hands + 1)

print(result)