import random

global cards 
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def welcomeMessage():
    print("|---------------------------|")
    print("|                           |")
    print("|         BlackJack         |")
    print("|                           |")
    print("|---------------------------|")

def getCards(firstTime, deck):
    if (firstTime):
        for i in range(0, 2):
            index = random.randint(0, len(cards) - 1)
            deck.append(cards[index])
            i+= 1
    else:
        index = random.randint(0, len(cards) - 1)
        deck.append(cards[index])

    return deck

def sumCards(playerCards, crupierCards):
    hasAs = False
    for i in range(0, len(playerCards)):
        if playerCards[i] == "J" or playerCards[i] == "Q" or playerCards[i] == "K":
            playerCards[i] = '10'
        elif playerCards[i] == "A":
            hasAs = True
            playerCards[i] = '1'
        i+= 1

    for j in range(0, len(crupierCards)):
        if crupierCards[j] == "J" or crupierCards[j] == "Q" or crupierCards[j] == "K":
            crupierCards[j] = '10'
        elif crupierCards[j] == "A":
            crupierCards[j] = '1'
        elif crupierCards[j] == "?":
            crupierCards[j] = '0'
        j+= 1

    playerCards = convertToInt(playerCards)
    if hasAs and sum(playerCards) <= 21:
        playerTotal = sum(playerCards) + 10
    else:
        playerTotal = sum(playerCards)

    crupierCards = convertToInt(crupierCards)
    crupierTotal = sum(crupierCards)

    print(f"Crupier total: {crupierTotal}")
    print(f"Player total: {playerTotal}")
    
def convertToInt(stringList):
    integerList = [int(s) for s in stringList]
    return integerList

def main():
    playerCards = []
    crupierCards = []

    startGame = input("Please type 's' to start playing: ")
    
    if startGame == 's':
        firstTime = True

        crupierCards = getCards(False, crupierCards)
        crupierCards.append("?")

        playerCards = getCards(firstTime, playerCards)
        
        print(f"\n-> Crupier cards: {crupierCards}")
        print(f"-> Player deck: {playerCards}")

        sumCards(playerCards, crupierCards)

        
if __name__ == "__main__": 
    welcomeMessage()
    main()




