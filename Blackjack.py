import sys
import math
import random

wallet = 100
bets = []
values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 1
}
cards = list(values.keys())
dealerHand = []
playerHands = [[], []]
didSplit = False
currentHand = 0

def init():
    global dealerHand
    global playerHands
    global didSplit
    global currentHand

    dealerHand = []
    playerHands = [[], []]
    didSplit = False
    currentHand = 0

    playerHands[0].append(random.choice(cards))
    dealerHand.append(random.choice(cards))
    playerHands[0].append(random.choice(cards))
    dealerHand.append(random.choice(cards))

    if len(dealerHand) != 2 or len(playerHands[0]) != 2:
        init()

def fullInit():
    global wallet
    global bets

    bets = [0]
    
    while bets[0] <= 0:
        print("Your current balance is {}".format(wallet))
        response = input("Place your bet: ")
        if response.isdigit():
            numIn = int(response)
            if numIn > wallet:
                print("Your bet can't exceed your balance\n")
            elif numIn <= 0:
                print("You can't bet nothing\n")
            else:
                bets[0] = numIn
        else:
            print("Please type a whole number\n")

    init()

def calcHand(hand):
    total = 0
    aces = 0
    for card in hand:
        total += values[card]
        if card == 'A':
            aces += 1
    for ace in range(aces):
        if (total + 10) <= 21:
            total += 10
    return total

def calcCurrent():
    return calcHand(playerHands[currentHand])

def checkBust():
    if calcCurrent() > 21:
        print("Your hand busted\n")
        return True
    else:
        return False

def playDealer():
    global bets
    global dealerHand
    global playerHands
    global didSplit
    
    while calcHand(dealerHand) < 17:
        dealerHand.append(random.choice(cards))
    dealerVal = calcHand(dealerHand)
    playerVal = calcHand(playerHands[0])
    
    net = 0

    if dealerVal == 21:
        if playerVal != 21:
            net -= bets[0]
        if didSplit and calcHand(playerHands[1]) != 21:
            net -= bets[1]
    elif dealerVal > 21:
        if playerVal == 21:
            net += math.ceil(1.5 * bets[0])
        elif playerVal < 21:
            net += bets[0]
        else:
            net -= bets[0]
        
        if didSplit:
            playerVal2 = calcHand(playerHands[1])
            if playerVal2 == 21:
                net += math.ceil(1.5 * bets[1])
            elif playerVal2 < 21:
                net += bets[1]
            else:
                net -= bets[1]
    else:
        if playerVal == 21:
            net += math.ceil(1.5 * bets[0])
        elif playerVal > 21 or playerVal < dealerVal:
            net -= bets[0]
        elif playerVal > dealerVal:
            net += bets[0]
        
        if didSplit:
            playerVal2 = calcHand(playerHands[1])
            if playerVal2 == 21:
                net += math.ceil(1.5 * bets[1])
            elif playerVal2 > 21 or playerVal2 < dealerVal:
                net -= bets[1]
            elif playerVal2 > dealerVal:
                net += bets[1]

    endRound(net)

def loseHand():
    global bets
    global dealerHand
    global playerHands
    global didSplit
    
    net = 0
    
    if didSplit:
        if calcHand(playerHands[0]) > 21:
            net -= bets[0]
            net -= bets[1]
            endRound(net)
        else:
            playDealer()
    else:
        net -= bets[0]
        endRound(net)

def endRound(net):
    global wallet
    global bets
    global dealerHand
    global playerHands
    global didSplit
    
    print("Dealer: {}".format(", ".join(dealerHand)))
    if didSplit:
        print("Hand 1: {}".format(", ".join(playerHands[0])))
        print("Bet: {}".format(bets[0]))
        print("Hand 2: {}".format(", ".join(playerHands[1])))
        print("Bet: {}".format(bets[1]))
    else:
        print("Player: {}".format(", ".join(playerHands[0])))
        print("Bet: {}".format(bets[0]))

    wallet += net
    
    if net == 0:
        print("No change")
    elif net > 0:
        print("You won {}!".format(net))
    else:
        print("You lost {}...".format(-net))

    if input("Play again? (y): ").lower() == 'y':
        fullInit()
    else:
        sys.exit()

def stand():
    global didSplit
    global currentHand
    
    if didSplit and currentHand == 0:
        currentHand = 1
    else:
        playDealer()

def hit():
    global playerHands
    global didSplit
    global currentHand
    
    playerHands[currentHand].append(random.choice(cards))
    if checkBust():
        if didSplit and currentHand == 0:
            currentHand = 1
        else:
            loseHand()

def double():
    global bets
    global playerHands
    global didSplit
    global currentHand
    
    bets[currentHand] *= 2
    playerHands[currentHand].append(random.choice(cards))
    if checkBust():
        if didSplit and currentHand == 0:
            currentHand = 1
        else:
            loseHand()
    else:
        playDealer()

def split():
    global bets
    global playerHands
    global didSplit

    if not didSplit and len(playerHands[0]) == 2 and playerHands[0][0] == playerHands[0][1]:
        didSplit = True
        bets.append(bets[0])
        
        playerHands[1] += playerHands[0].pop()
        playerHands[0].append(random.choice(cards))
        playerHands[1].append(random.choice(cards))
    else:
        print("Split unavailable\n")

def surrender():
    global bets
    global playerHands
    global didSplit

    if not didSplit and len(playerHands[0]) == 2:
        bets[0] //= 2
        loseHand()
    else:
        print("Surrender unavailable\n")

def showValue():
    print("Current value: {}\n".format(calcCurrent()))

def swapHand():
    global currentHand
    currentHand = 1 if currentHand == 0 else 0

def reset():
    init()

actionDict = {
    's': stand,
    'stand': stand,
    'h': hit,
    'hit': hit,
    'd': double,
    'double': double,
    'double down': double,
    'p': split,
    'split': split,
    'u': surrender,
    'surrender': surrender,
    'c': showValue,
    'calc': showValue,
    'calculate': showValue
}

def main():
    fullInit()
    while True:
        print("Bet: {}".format(bets[currentHand]))
        print("Dealer: #, {}".format(dealerHand[1]))
        
        if didSplit:
            print("Hand {}: {}".format(currentHand + 1, ", ".join(playerHands[currentHand])))
        else:
            print("Player: {}".format(", ".join(playerHands[0])))

        print("Actions: (s)tand, (h)it, (d)ouble down, s(p)lit, s(u)rrender")
        action = input().lower()

        if action in actionDict:
            actionDict[action]()
        else:
            print("Invalid action\n")

main()
