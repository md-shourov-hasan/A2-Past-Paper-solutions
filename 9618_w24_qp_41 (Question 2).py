class Horse:
    def __init__(self,Name,MaxFenceHeight,PercentageSuccess):
        self.__Name = Name #String
        self.__MaxFenceHeight = MaxFenceHeight #Integer
        self.__PercentageSuccess = PercentageSuccess #Integer

    def GetName(self):
        return self.__Name
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight


Horses = []

Horses.append(Horse("Beauty", 150, 72))
Horses.append(Horse("Jet", 160, 65))

print(Horses[0].GetName())
print(Horses[1].GetName())


class Fence:
    def __init__(self,Height,Risk):
        self.__Height = Height
        self.__Risk = Risk

    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk

#2(c)

Course = []

for i in range(4):
    Height = int(input("Enter the height: "))
    while Height < 70 or Height > 180:
        Height = int(input("Enter the height: "))
    Risk = int(input("Enter the risk: "))
    while Risk < 1 or Risk > 5:
        Risk = int(input("Enter the risk: "))

    Course.append(Fence(Height,Risk))

    
