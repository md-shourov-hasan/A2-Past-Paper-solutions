class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number #integer
        self.__Colour = Colour #string

    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

class Hand:
    #Cards an array of type Card
    #FirstCard Integer
    #NumberCards Integer

    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
        self.__FirstCard = 0
        self.__NumberCards = 5

    def GetCard(self,index):
        return self.__Cards[index]


def CalculateValue(PlayerHand):
    Score = 0

    for i in range(5):
        CurrentCard = PlayerHand.GetCard(i)
        CardColour = CurrentCard.GetColour()

        if CardColour == "red":
            Score += 5
        elif CardColour == "blue":
            Score += 10
        elif CardColour == "yellow":
            Score += 15
        Score += CurrentCard.GetNumber()

    return Score






oneR = Card(1, "red")
twoR = Card(2, "red")
threeR = Card(3, "red")
fourR = Card(4, "red")
fiveR = Card(5, "red")

oneB = Card(1, "blue")
twoB = Card(2, "blue")
threeB = Card(3, "blue")
fourB = Card(4, "blue")
fiveB = Card(5, "blue")

oneY = Card(1, "yellow")
twoY = Card(2, "yellow")
threeY = Card(3, "yellow")
fourY = Card(4, "yellow")
fiveY = Card(5, "yellow")



Player1 = Hand(oneR, twoR, threeR, fourR, oneY)
Player2 = Hand(twoY, threeY, fourY, fiveY, oneB)

Player1_Score = CalculateValue(Player1)
Player2_Score = CalculateValue(Player2)

if Player1_Score > Player2_Score:
    print("Player 1 won the game")
elif Player2_Score > Player1_Score:
    print("Player 2 won the game")
else:
    print("It's a draw")

