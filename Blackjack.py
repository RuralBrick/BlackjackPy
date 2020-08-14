import random

wallet = 10
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

    dealerHand.clear()
    playerHands = [[], []]
    didSplit = False
    currentHand = 0

    playerHands[0] += random.choice(cards)
    dealerHand += random.choice(cards)
    playerHands[0] += random.choice(cards)
    dealerHand += random.choice(cards)

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

def justEnd():
    global wallet
    global bets
    global dealerHand
    global playerHands
    global didSplit

    netGain = 0
    
    print("Dealer: {}".format(", ".join(dealerHand)))
    if didSplit:
        print("Hand 1: {}".format(", ".join(playerHands[0])))
        print("Bet: {}".format(bets[0])
        print("Hand 2: {}".format(", ".join(playerHands[1])))
        print("Bet: {}".format(bets[1])
    else:
        print("Player: {}".format(", ".join(playerHands[0])))
        print("Bet: {}".format(bets[0]))
        netGain -= bets[0]
    
    #if netGain 

def calcEnd():
    global wallet
    global bets
    global dealerHand
    global playerHands
    global didSplit
    global currentHand
    
    while calcHand(dealerHand) < 17:
        dealerHand += random.choice(cards)

    dealerVal = calcHand(dealerHand)
    netGain = 0

    print("Dealer: {}".format(", ".join(dealerHand)))
    if didSplit:
        print("Hand 1: {}".format(", ".join(playerHands[0])))
        print("Bet: {}".format(bets[0])
        print("Hand 2: {}".format(", ".join(playerHands[1])))
        print("Bet: {}".format(bets[1])
    else:
        print("Player: {}".format(", ".join(playerHands[0])))
        print("Bet: {}".format(bets[0]))
    
    if dealerVal > 21 or dealerVal < calcCurrent():
        print("You won {}!\n".format(netGain))
        wallet += netGain
    elif dealerVal > calcCurrent():
        print("You lost {}...\n".format(netGain))
        wallet -= netGain

def checkHand():
    pass
    
def checkBust():
    if calcCurrent() > 21:
        print("Your hand busted\n")
        return True
    else:
        return False
      
def endRound(net):
    print("Dealer: {}".format(", ".join(dealerHand)))
    if didSplit:
        print("Hand 1: {}".format(", ".join(playerHands[0])))
        print("Bet: {}".format(bets[0])
        print("Hand 2: {}".format(", ".join(playerHands[1])))
        print("Bet: {}".format(bets[1])
    else:
        print("Player: {}".format(", ".join(playerHands[0])))
        print("Bet: {}".format(bets[0]))

    if net == 0:
        print("No change")
    elif net > 0:
        print("You won {}!".format(net))
    else:
        print("You lost {}...".format(net))

def stand():
    if didSplit and currentHand == 0:
        currentHand = 1
    else:
        pass # end round

def hit():
    global playerHands
    playerHands[currentHand] += random.choice(cards)
    if checkBust():
        if didSplit and currentHand == 0:
            currentHand = 1
        else:
            pass #lose hand

def double():
    global bet
    global playerHands
    bet *= 2
    playerHands[currentHand] += random.choice(cards)
    if checkBust():
        if didSplit and currentHand == 0:
            currentHand = 1
        else:
            pass #lose hand
    else:
        pass #end round

def split():
    global playerHands
    global didSplit

    if not didSplit and len(playerHands[0]) == 2 and playerHands[0][0] == playerHands[0][1]:
        didSplit = True
        playerHands[1] += playerHands[0].pop()
        
        playerHands[0] += random.choice(cards)
        playerHands[1] += random.choice(cards)
    else:
        print("Split unavailable\n")

def surrender():
    global bet
    global playerHands
    global didSplit

    if not didSplit and len(playerHands[0]) == 2:
        bet //= 2
        # lose hand
    else:
        print("Surrender unavailable\n")

def showValue():
    print("Current value: {}\n".format(calcCurrent))

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
        print("Bet: {}".format(bet))
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
