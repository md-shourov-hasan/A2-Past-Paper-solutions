class Tree:
    def __init__(self, PTreeName, PHeightGrowth, PMaxHeight, PMaxWidth, PEvergreen):
        self.__TreeName = PTreeName  # string
        self.__HeightGrowth = PHeightGrowth  # integer
        self.__MaxHeight = PMaxHeight  # integer
        self.__MaxWidth = PMaxWidth  # integer
        self.__Evergreen = PEvergreen  # string

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
    Tree_array = []  # Tree

    try:
        file = open("Trees.txt", "r")
        for line in file:
            text = line.strip().split(",")
            New_Tree = Tree(text[0], int(text[1]), int(text[2]), int(text[3]), text[4])
            Tree_array.append(New_Tree)
        return Tree_array

    except IOError:
        print("File not found!")


def PrintTrees(New_Tree):
    if New_Tree.GetEvergreen() == "Yes":
        print(New_Tree.GetTreeName() + " has a maximum height " + str(
            New_Tree.GetMaxHeight()) + " a maximum width " + str(New_Tree.GetMaxWidth()) + " and grows " + str(
            New_Tree.GetGrowth()) + " cm a year. It does not lose its leaves.")
    else:
        print(New_Tree.GetTreeName() + " has a maximum height " + str(
            New_Tree.GetMaxHeight()) + " a maximum width " + str(New_Tree.GetMaxWidth()) + " and grows " + str(
            New_Tree.GetGrowth()) + " cm a year. It loses its leaves each year.")


def ChooseTree(Tree_Array):
    maxHeight = int(input("Enter the maximum height the tree can be in cm: "))
    maxWidth = int(input("Enter the maximum width the tree can be in cm: "))
    isEvergreen = input("Do you want it to be evergreen? (Yes/No): ")

    length = len(Tree_Array)
    New_Array = []

    for i in range(length):
        if Tree_Array[i].GetEvergreen() == isEvergreen and Tree_Array[i].GetMaxHeight() <= maxHeight and Tree_Array[
            i].GetMaxWidth() <= maxWidth:
            New_Array.append(Tree_Array[i])
            PrintTrees(Tree_Array[i])
    if len(New_Array) == 0:
        print("No trees meet all the requirements.")

    User_TreeName = input("Enter the name of the tree that you would like to buy: ")
    User_TreeHeight = int(input("Enter the height of the tree in cm when it is bought: "))

    for i in New_Array:
        if i.GetTreeName() == User_TreeName:
            User_Tree = i
            break
    years = (User_Tree.GetMaxHeight() - User_TreeHeight) // User_Tree.GetGrowth()
    print("It will take " + str(years) + " years to reach it's maximum height.")


# main program
Returned_Array = ReadData()
PrintTrees(Returned_Array[0])

ChooseTree(Returned_Array)
