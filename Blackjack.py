import random

wallet = 10
bet = 0
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
    global wallet
    global bet
    global dealerHand
    global playerHands
    global didSplit
    global currentHand

    bet = 0
    dealerHand.clear()
    playerHands = [[], []]
    didSplit = False
    currentHand = 0

    playerHands[0] += random.choice(cards)
    dealerHand += random.choice(cards)
    playerHands[0] += random.choice(cards)
    dealerHand += random.choice(cards)

    while bet <= 0:
        print("Your current balance is {}".format(wallet))
        response = input("Place your bet: ")
        if response.isdigit():
            numIn = int(response)
            if numIn > wallet:
                print("Your bet can't exceed your balance\n")
            elif numIn <= 0:
                print("You can't bet nothing\n")
            else:
                bet = numIn
        else:
            print("Please type a whole number\n")

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

def checkEnd():
    pass

def stand():
    print('stand')
    # end round

def hit():
    global playerHands
    playerHands[currentHand] += random.choice(cards)
    pass

def double():
    global bet
    global playerHands
    bet *= 2
    playerHands[currentHand] += random.choice(cards)
    # end round

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
    pass

def surrender():
    global bet
    global playerHands
    global didSplit

    if not didSplit and len(playerHands[0]) == 2:
        bet //= 2
        # end round  # do not calculate win
    else:
        print("Surrender unavailable\n")

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
    'surrender': surrender
}

init()
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
