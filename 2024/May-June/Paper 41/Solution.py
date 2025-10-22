#Solution goes here
#Quesion 1

def Initialise():
    NumberItems = int(input("Enter quantity of numbers you want to enter: "))

    while NumberItems < 1 or NumberItems > 20:
        NumberItems = int(input("Enter quantity of numbers you want to enter: "))
    
    for i in range(NumberItems):
        DataStored.append(int(input("Enter the number: ")))
        NumberItems += 1


def BubbleSort():
    length = len(DataStored)
    for i in range(length-1):
        for x in range(length - 1 - i):
            if DataStored[x] > DataStored[x+1]:
                DataStored[x], DataStored[x+1] = DataStored[x+1], DataStored[x]


def BinarySearch(DataToFind):
    length = len(DataStored)
    start = 0
    end = length - 1

    while start <= end:
        mid = (start + end) // 2
        if DataToFind == DataStored[mid]:
            return mid
        elif DataToFind > DataStored[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1
    


#main program
DataStored = [] #Stores 20 integers
global NumberItems
NumberItems = 0

Initialise()
print(DataStored)

BubbleSort()
print(DataStored)

Search = int(input("Enter a number to search: "))
print(BinarySearch(Search))


#Question 2

class Tree:
    def __init__(self,TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen):
        self.__TreeName = TreeName #String
        self.__HeightGrowth = HeightGrowth #Integer
        self.__MaxHeight = MaxHeight #Integer
        self.__MaxWidth = MaxWidth #Integer
        self.__Evergreen = Evergreen #String
    
    def GetTreeName(self):
        return self.__TreeName
    def GetGrowth(self):
        return self.__HeightGrowth
    def GetMaxHeight(self):
        return self.__MaxHeight
    def GetMaxWidth(self):
        return self.__MaxWidth
    def GetEvergreen(self):
        return self.__Evergreen



def ReadData():
    DataArray = [] #Type Tree

    try:
        file = open("Tree.txt","r")

        for line in file:
            Data = line.strip()
            
            count = 1
            for i in range(len(Data)):
                if Data[i] == "," or Data[i] =="":
                    if count == 1:
                        TreeName = text
                        text = ""
                        count += 1
                    elif count == 2:
                        Growth = text
                        text = ""
                        count +=1
                    elif count == 3:
                        Height = text
                        text = ""
                        count +=1
                    elif count == 4:
                        Width = text
                        text = ""
                        count +=1
                    elif count == 5:
                        Evergreen = text
                        text = ""
                        count = 1                    
                else:
                    text = text + Data[i]
            DataArray.append(Tree(TreeName, Growth, Height, Width, Evergreen))

    except IOError:
        print("File not found!")