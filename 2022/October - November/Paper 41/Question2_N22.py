class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number #integer
        self.__Colour = Colour #string

    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

class Hand:
    def __int__(self, Cards, FirstCard, NumberCards):
        self.__Cards = Cards #Array of Type Card
        self.__FirstCard = FirstCard #Integer
        self.__NumberCards = NumberCards #Integer







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



#to be continued
