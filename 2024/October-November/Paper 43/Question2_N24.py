class Horse:
    def __init__(self, Name, MaxFenceHeight, PercentageSuccess):
        self.__Name = Name  # String
        self.__MaxFenceHeight = MaxFenceHeight  # Integer
        self.__PercentageSuccess = PercentageSuccess  # Integer

    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight

    # 2(d)
    def Success(self, FenceHeight, risk):
        if (FenceHeight > self.__MaxFenceHeight):
            return self.__PercentageSuccess * 0.20
        else:
            if (risk == 1):
                return self.__PercentageSuccess
            elif (risk == 2):
                return self.__PercentageSuccess * 0.9
            elif (risk == 3):
                return self.__PercentageSuccess * 0.8
            elif (risk == 4):
                return self.__PercentageSuccess * 0.7
            elif (risk == 5):
                return self.__PercentageSuccess * 0.6


class Fence:
    def __init__(self, Height, Risk):
        self.__Height = Height
        self.__Risk = Risk

    def GetHeight(self):
        return self.__Height

    def GetRisk(self):
        return self.__Risk


# 2(c)

Course = []

for i in range(4):
    Height = int(input("Enter the height in cm: "))
    while Height < 70 or Height > 180:
        Height = int(input("Enter the height in cm: "))
    Risk = int(input("Enter the risk: "))
    while Risk < 1 or Risk > 5:
        Risk = int(input("Enter the risk: "))
    Course.append(Fence(Height, Risk))

# main program

Horses = []

Horses.append(Horse("Beauty", 150, 72))
Horses.append(Horse("Jet", 160, 65))

print(Horses[0].GetName())
print(Horses[1].GetName())

max_avg = 0

for h in range(2):
    total = 0
    avg = 0
    for f in range(4):
        chances = Horses[h].Success(Course[f].GetHeight(), Course[f].GetRisk())
        total += chances

        print(f"The horse {Horses[h].GetName()} at fence {f + 1} has a {chances}% chance of success")
    avg = total / 4
    print(f"The horse {Horses[h].GetName()} has an average {avg}% chance of jumping over all four fences")
    if avg > max_avg:
        max_avg = avg
        maxHorseIndex = h

print(f"The horse {Horses[maxHorseIndex].GetName()} has the highest average chance of success.")
