class Balloon:
    def __init__(self, DefenceItemName, BalloonColour):
        self.__DefenceItem = DefenceItemName #String
        self.__Colour = BalloonColour #String
        self.__Health = 100 #Integer

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, value):
        self.__Health += value

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False

def Defend(Object):
    strength = int(input("Enter the strength of the opponent: "))

    Object.ChangeHealth(-strength)

    print(f"The defence item of the balloon is {Object.GetDefenceItem()}")

    Health = Object.CheckHealth()

    if Health:
        print("There is no health remaining")
    else:
        print("There is health remaining")

    return Object





#Main Program

UserDefenceItem = input("Enter a defence item: ")
UserColour = input("Enter the colour: ")

Balloon1 = Balloon(UserDefenceItem, UserColour)

Defend(Balloon1)
