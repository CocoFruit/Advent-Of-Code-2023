# hand = [type,[cards]]

cards = "AKQT98765432J"[::-1]


def custom_sort(hand):
    return [cards.index(card) for card in hand]

def check(hand):
    ogHand = hand.copy()
    thing = ""
    o = False
    t = False
    j = 0
    for card in hand:
        if hand.count(card) == 2:
            i = hand.index(card)
            hand.pop(i)
            i = hand.index(card)
            hand.pop(i)
            for card in hand[j:]:
                if hand.count(card) == 2:
                    thing = "Two pairs"
                    break
                else:
                    hand = ogHand
                j += 1
            if thing != "Two pairs": 
                thing = "One pair"
                o = True
            break
        j += 1
    
    # check for three of a kind
    for card in hand:
        if hand.count(card) == 3:
            thing = "Three of a kind"
            t = True

    # check for full house
    if t and o:
        thing = "Full house"

    # check for four of a kind
    for card in hand[:5]:
        if hand.count(card) == 4:
            thing = "Four of a kind"

    # check for five of a kind
    if hand.count(hand[0]) == 5:
        thing = "Five of a kind"

    # check for high card
    if thing == "":
        thing = "High card"

    return thing

def main():
    with open("Day 7/input.txt") as f:
        lines = f.readlines()

    handNums = {"High card":1, "One pair":2, "Two pairs":3, "Three of a kind":4, "Full house":5, "Four of a kind":6, "Five of a kind":7}

    bets = {}

    allHands = []

    for line in lines:
        line = line.strip().split(" ")
        hand = list(line[0])    
        ogHand = list(line[0])
        bet = int(line[1])
        bets["".join(hand)] = bet
        bestType = "High card"

        # check for pairs
        if "J" in "".join(hand):
            for possibleCard in cards:
                hand = "".join(ogHand)
                hand = hand.replace("J",possibleCard)
                hand = list(hand)
                thing =  check(hand)
                
                if handNums[thing] > handNums[bestType]:
                    bestType = thing
                hand = ogHand
        else:
            thing = check(hand)
            if handNums[thing] > handNums[bestType]:
                bestType = thing

        
        hand = "".join(ogHand)
        # convert hand to nums
        hand = [cards.index(card) for card in hand]

        allHands.append([handNums[bestType],hand])


    allHands = sorted(allHands, key=lambda x: (x[0],x[1]))
    total = 0
    for n,hand in enumerate(allHands):
        total+=bets["".join([cards[card] for card in hand[1]])]*(n+1)
        
    print(total)
            
if __name__ == "__main__":
    main()

