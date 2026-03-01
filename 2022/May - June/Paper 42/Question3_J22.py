class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number  # Integer
        self.__Colour = Colour  # String

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


def ChooseCard():
    index = int(input("Enter an index: "))

    while index >= 1 and index <= 30:


# main program

Cards = []  # Stores 30 elements of type Card

CardFile = open("CardValues.txt", "r")

for line in CardFile:
    number = int(line.strip())
    Colour = CardFile.readline().strip()

    Cards.append(Card(number, Colour))

CardFile.close()

ChosenCards = []
