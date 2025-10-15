#Question 1
def ReadData():
    Data_array = [] #stores 45 items
    file = open("Data.txt","r")
    for line in file:
        Data_array.append(line.strip())
    file.close()
    return Data_array


def FormatArray(String_Array):
    size = len(String_Array)
    concatenated_string = ""

    for i in range(0,size):
        concatenated_string = concatenated_string + String_Array[i] + " "

    return concatenated_string

print(FormatArray(ReadData()))

def CompareStrings(firstString,secondString):
    index = 0

    while True:
        if firstString[index] == secondString[index]:
            index += 1
        else:
            if firstString[index] > secondString[index]:
                return 1
            else: 
                return 2
    
def Bubble(Data_array):
#to be continued


Question 2

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

    
