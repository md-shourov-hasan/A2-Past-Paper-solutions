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
            text = line.strip().split(",")
            DataArray.append(Tree(text[0], int(text[1]), int(text[2]), int(text[3]), text[4]))
        file.close()
        return DataArray

    except IOError:
        print("File not found!")

def PrintTrees(TreeObject):
    if TreeObject.GetEvergreen() == "Yes":
        print(f"{TreeObject.GetTreeName()} has a maximum height {TreeObject.GetMaxHeight()} a maximum width {TreeObject.GetMaxWidth()} and grows {TreeObject.GetGrowth()} cm a year. It does not lose its leaves.")
    else:
        print(f"{TreeObject.GetTreeName()} has a maximum height {TreeObject.GetMaxHeight()} a maximum width {TreeObject.GetMaxWidth()} and grows {TreeObject.GetGrowth()} cm a year. It loses its leaves each year.")



def ChooseTree(Array):
    New_Array = []
    user_height = int(input("Enter the maximum height the tree can be in cm: "))
    user_width = int(input("Enter the maximum width the tree can be in cm: "))
    is_evergreen = input("Do you want the tree to be evergreen? Yes or No?: ")

    for i in range(len(Array)):
        if (user_height >= Array[i].GetMaxHeight()) and (user_width >= Array[i].GetMaxWidth()) and (is_evergreen == Array[i].GetEvergreen()):

            New_Array.append(Array[i])
            PrintTrees(Array[i])

    if len(New_Array) != 0:

        Name = input("Enter the name of the tree that you would like to buy: ")
        Height = int(input("Enter the height of the tree in cm: "))

        for k in range(len(New_Array)):
            if New_Array[k].GetTreeName() == Name:
                Years = (New_Array[k].GetMaxHeight() - Height) // New_Array[k].GetGrowth()
                print(f"It will take {Years} years to reach its maximum height.")

    else:
        print("No trees meet all the requirements.")

#main program

Tree_Array = ReadData()
PrintTrees(Tree_Array[0])
ChooseTree(Tree_Array)

