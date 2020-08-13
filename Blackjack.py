import random

wallet = 10
bet = 0
bet2 = 0
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
    'A': 11
}
cards = list(values.keys())
dealerHand = []
playerHand = []
playerHand2 = []
didSplit = False
currentHand = 1

def init():
    global wallet
    global bet
    global dealerHand
    global playerHand
    global playerHand2
    global didSplit
    global currentHand

    dealerHand.clear()
    playerHand.clear()
    playerHand2.clear()
    didSplit = False
    currentHand = 1

    playerHand += random.choice(cards)
    dealerHand += random.choice(cards)
    playerHand += random.choice(cards)
    dealerHand += random.choice(cards)

def stand():
    print('stand')
    # end round

def hit():
    global playerHand
    playerHand += random.choice(cards)
    pass

def double():
    global playerHand
    playerHand += random.choice(cards)
    # end round

def split():
    global playerHand
    global playerHand2
    global didSplit

    if len(playerHand) == 2 and playerHand[0] == playerHand[1]:
        didSplit = True
        playerHand2 += playerHand.pop()
        
        playerHand += random.choice(cards)
        playerHand2 += random.choice(cards)
    else:
        print("Split unavailable")
    pass

def surrender():
    print('surrender')
    # end round

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
    print("Dealer: #, {}".format(dealerHand[1]))
    
    print("Player: {}".format(", ".join(playerHand)))
    if didSplit: print("        {}".format(", ".join(playerHand2)))
    
    print("Actions: (s)tand, (h)it, (d)ouble down, s(p)lit, s(u)rrender")
    action = input().lower()

    if action in actionDict:
        actionDict[action]()
    else:
        print("Invalid action")
