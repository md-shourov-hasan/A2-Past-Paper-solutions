class Card:
    def __init__(self, Number, Colour):
        self.__Number = Number  # Integer
        self.__Colour = Colour  # String

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour


def ChooseCard():
    global SelectedCards

    index = int(input("Enter an index: "))

    while index < 1 or index > 30:
        index = int(input("Try again: "))

    while True:
        if SelectedCards[index-1] == False:
            SelectedCards[index-1] = True
            return index-1
        else:
            index = int(input("The card is chosen. Try again: "))


# main program

Cards = []  # Stores 30 elements of type Card

CardFile = open("CardValues.txt", "r")

line = CardFile.readline().strip()

while line != "":
    number = int(line.strip())
    Colour = CardFile.readline().strip()

    Cards.append(Card(number, Colour))
    line = CardFile.readline().strip()

CardFile.close()

SelectedCards = [False for _ in range(30)]

Player1 = [] #type Card
for i in range(4):
   index = ChooseCard()
   Player1.append(Cards[index])

   print("The number of the card is: ",Player1[i].GetNumber() )
   print("The color of the card is: ",Player1[i].GetColour())

