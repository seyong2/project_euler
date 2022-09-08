import time as time

def values(hand):
    return [i[0] for i in hand]

def rank(hand):
    royals = ['A', 'J', 'K', 'Q', 'T']
    ranks = ['2', '3', '4', '5' , '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
    suits = [i[-1] for i in hand]
    vals = values(hand)
    hand_index = [ranks.index(v) for v in vals]
    counts = {v: vals.count(v) for v in set(vals)}
    
    # Royal flush: Ten, Jack, Queen, King, Ace, in same suit.
    if royals == sorted(suits):
        return 'RF'
    
    # Straight flush: All cards are consecutive values of same suit.
    elif (len(set(suits)) == 1) and (len(set(hand_index)) == 5) and (max(hand_index)-min(hand_index) == 4):
        return 'SF'
    
    # Four of a kind: Four cards of the same value
    elif 4 in counts.values():
        val_4k = list(counts.keys())[list(counts.values()).index(4)]
        return ["4K", ranks.index(val_4k)]
    
    # Full house: Three of a kind and a pair.
    elif {2, 3} == set(counts.values()):
        val_3 = list(counts.keys())[list(counts.values()).index(3)]
        #val_2 = list(counts.keys())[list(counts.values()).index(2)]
        return ["FH", ranks.index(val_3)]#, ranks.index(val_2)]
    
    # Flush: All cards of the same suit.
    elif len(set(suits)) == 1:
        return ["FL", max(hand_index)]
    
    # Straight: All cards are consecutive values.
    elif (len(set(hand_index)) == 5) and (max(hand_index)-min(hand_index) == 4):
        return ["ST", max(hand_index)]
    
    # Three of a kind: Three cards of the same value.
    elif 3 in counts.values():
        val_3 = list(counts.keys())[list(counts.values()).index(3)]
        #hand_index = list(set(hand_index))
        #hand_index.remove(ranks.index(val_3))
        return ["3K", ranks.index(val_3)]#, max(hand_index)]
    
    # Two pairs: Two different pairs.
    elif len([key for key, val in counts.items() if val == 2]) == 2:
        val_max = max([ranks.index(i) for i in [key for key, val in counts.items() if val == 2]])
        val_min = min([ranks.index(i) for i in [key for key, val in counts.items() if val == 2]])
        hand_index = list(set(hand_index))
        hand_index.remove(val_max)
        hand_index.remove(val_min)
        return ["2P", val_max, val_min, hand_index[0]]
    
    # One pair: Two cards of the same value.
    elif len([key for key, val in counts.items() if val == 2]) == 1:
        val_1p = list(counts.keys())[list(counts.values()).index(2)]
        hand_index = list(set(hand_index))
        hand_index.remove(ranks.index(val_1p))
        return ["1P", ranks.index(val_1p), max(hand_index)]
    
    # Highest card: Highest value card.
    else:
        return ["HC", max(hand_index)]

tic = time.time()
    
order = ['HC', '1P', '2P', '3K', 'ST', 'FL', 'FH', '4K', 'SF', 'RF']

win_1 = 0

with open('p054_poker.txt') as f:
    lines = f.readlines()
    
for i in range(0, len(lines)):
    cards = lines[i].strip('\n').split(' ')
    
    hand_1 = cards[:5] # the first five are Player 1's cards
    hand_2 = cards[-5:] # the last five are Player 2's cards
    
    order_hand_1 = order.index(rank(hand_1)[0]) # rank of the Player 1's cards
    order_hand_2 = order.index(rank(hand_2)[0]) # rank of the Player 2's cards
    
    if order_hand_1 == order_hand_2: # if the ranks are the same...
        j = 1
        while j < len(rank(hand_1)):
            if rank(hand_1)[j] > rank(hand_2)[j]:
                win_1 += 1
                break
            elif rank(hand_1)[j] == rank(hand_2)[j]:
                j += 1
            else:
                break
    elif order_hand_1 > order_hand_2:
        win_1 += 1

toc = time.time()
print(win_1)
print(toc - tic)
    