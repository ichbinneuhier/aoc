def get_type(hand): # types: 1-7 1 highest, 7 lowest
    d = {}
    possible = [7]
    for char in hand:
        d[char] = hand.count(char)
    val = list(d.values())
    val.append(0)
    if d.setdefault("J", 0):
        val.remove(d["J"])
    if d["J"] >= 3 or (2 in val and d["J"] >= 2) or (3 in val and d["J"] >= 1) or (3 in val and 2 in val) or (val.count(2)==2 and d["J"] >= 1): possible.append(3) # ful house
    for i in range(d["J"]+1,0,-1):
        try:
            if 5-i+1 in val: possible.append(1) # five of a kind
            if 4-i+1 in val: possible.append(2) # four of a kind
            if 3-i+1 in val: possible.append(4) # three of a kind
            if val.count(2) == 2-i+1: possible.append(5) # two pair
            if 2-i+1 in val: possible.append(6) # one pair
        except ValueError:
            pass
    
    return sorted(possible)[0]

def sort_cards(hands): # compare each digit, lower rank to higher rank
    idx_hand_rank = []
    for idx, hand in enumerate(hands):
        act_hand = hand[0]
        act_hand = act_hand.replace("T", "a").replace("J", "1").replace("Q", "c").replace("K", "d").replace("A", "e")
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
    "J": 14,
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