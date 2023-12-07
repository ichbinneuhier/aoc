def get_type(hand): # types: 1-7 1 highest, 7 lowest
    d = {}
    possible = [1,2,3,4,5,6,7]
    for char in hand:
        d[char] = hand.count(char)
    val = list(d.values())
    if 5 not in val: possible.remove(1) # five of a kind
    if 4 not in val: possible.remove(2) # four of a kind
    if 3 not in val or 2 not in val: possible.remove(3) # full house
    if 3 not in val: possible.remove(4) # three of a kind
    if val.count(2) != 2: possible.remove(5) # two pair
    if 2 not in val: possible.remove(6) # one pair
    
    return possible[0]

def sort_cards(hands): # compare each digit, lower rank to higher rank
    idx_hand_rank = []
    for idx, hand in enumerate(hands):
        act_hand = hand[0]
        act_hand = act_hand.replace("T", "a").replace("J", "b").replace("Q", "c").replace("K", "d").replace("A", "e")
        idx_hand_rank.append((hand, int(act_hand, base=16)))
    idx_hand_rank.sort(key=lambda x: x[-1])
    final = []
    for elem in idx_hand_rank:
        final.append(elem[0])
    return final

with open("aoc-7-input.txt") as f:
    rank = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "J": 4,
    "T": 5,
    "9": 6, 
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13
    }
    hands = []
    final_sorted = []
    final = 0
    
    for line in f:
        hand, bid = line.split()
        hands.append((hand,get_type(hand),bid))
        
    hands.sort(key=lambda x: x[1])
    
    for i in (1,2,3,4,5,6,7):
        temp = []
        for hand in hands:
            if hand[1] == i:
                temp.append(hand)
        if len(temp) == 1:
            final_sorted.append(temp[0])
            continue
        if len(temp) == 0:
            continue
        sorted_temp = reversed(sort_cards(temp)) # idk why
        for hand in sorted_temp:
            final_sorted.append(hand)
    
    for idx, hand in enumerate(reversed(final_sorted)):
        final += (idx+1)*int(hand[-1])
        
    print(final)