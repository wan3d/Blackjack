import random

global cards 
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def welcomeMessage():
    print("|---------------------------|")
    print("|                           |")
    print("|         BlackJack         |")
    print("|                           |")
    print("|---------------------------|")
    startGame = input("Please type 's' to start playing: ")

    if not startGame == 's':
        return

def getCards():
    playerDeck = []
    croupierDeck = []

    for i in range (0, 2):
        playerDeck.append(cards[random.randint(0, len(cards) - 1)])
        croupierDeck.append(cards[random.randint(0, len(cards) - 1)])
        
    return playerDeck, croupierDeck

def sumList(listDeck):
    copyDeck = listDeck.copy()

    countAs = 0
    for i in range (0, len(copyDeck)):
        if copyDeck[i] in ['J', 'Q', 'K']:
            copyDeck[i] = '10'
        elif copyDeck[i] == 'A':
            countAs += 1
            copyDeck[i] = '11'

    # Convert string to int
    copyDeck = stringToInt(copyDeck)

    sumDeck = sum(copyDeck)
    for i in range(0, countAs):
        if sumDeck > 21:
            sumDeck = sumDeck - 10

    return sumDeck

def stringToInt(stringList):
    intList = list(map(int, stringList))

    return intList

def hideCard(croupierDeck):
    croupierDeck[1] = '?'
    return croupierDeck


def main():
    playerDeck, croupierDeck = getCards()

    copyCrouDeck = croupierDeck.copy()
    copyCrouDeck = hideCard(copyCrouDeck)

    sumPD = sumList(playerDeck)
    sumCD = sumList(croupierDeck)

    print(f"Player cards: {playerDeck}, Sum: {sumPD}", end=" ")
    print(f"Croupier cards: {copyCrouDeck}, Sum: ?")

    # Check early BlackJack
    if sumPD == 21 or sumCD == 21:
        if sumPD == sumCD:
            print("Tie!")
        elif sumPD == 21 and sumCD != 21:
            print("Player WINS by natural BlackJack!!")
        elif sumCD == 21 and sumPD != 21:
            print("Croupier WINS by natural BlackJack ://")
        return

    while True:
        print("-------------------------------")
        decisionPlayer = input("Hit (h) or stand (s)? ")
        
        if decisionPlayer == 'h':
            playerDeck.append(cards[random.randint(0, len(cards) - 1)]) 
            sumPD = sumList(playerDeck)
            print(f"{playerDeck}, Sum: {sumPD}")

            if sumPD > 21:
                print("Croupier wins")
                return
            
        elif decisionPlayer == 's':
            print("-------------------------------")
            while sumCD < 17:
                croupierDeck.append(cards[random.randint(0, len(cards) - 1)]) 
                sumCD = sumList(croupierDeck)
                print(f"{croupierDeck}, Sum: {sumCD}")

            if sumCD >= 17 and sumCD <= 21:
                if sumCD > sumPD:
                    print("Croupier wins")
                elif sumPD > sumCD:
                    print("Player wins")
                elif sumPD == sumCD:
                    print("Tie!") 
            elif sumCD > 21:
                print("Player wins")
            break
        
    
if __name__ == '__main__':
    welcomeMessage()
    main()
