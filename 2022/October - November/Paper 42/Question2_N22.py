class Character:
    def __init__(self, Name, XCoordinate, YCoordinate):
        self.__Name = Name #String
        self.__XCoordinate = XCoordinate #Integer
        self.__YCoordinate = YCoordinate #Integer

    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange


#Main program

Character_Array = []#stores 10 elements of type Character

try:
    CharacterFile = open("Characters.txt")

    name = CharacterFile.readline().strip()

    while name != "":
        x = int(CharacterFile.readline().strip())
        y = int(CharacterFile.readline().strip())

        Character_Array.append(Character(name, x, y ))
        name = CharacterFile.readline().strip()

    CharacterFile.close()

except IOError:
    print("File not found!")

position = -1

while position == -1 :
    CharacterName = input("Enter the character name: ")
    for index in range(10):
        if CharacterName.lower() == Character_Array[index].GetName().lower():
            position = index


move = input("Enter a move: ")

while move != "A" and move != "S" and move != "W" and move != "D":
    move = input("Enter a move: ")

if move == "A":
    Character_Array[position].ChangePosition(-1,0)
elif move == "W":
    Character_Array[position].ChangePosition(0,1)
elif move == "S":
    Character_Array[position].ChangePosition(0,-1)
else:
    Character_Array[position].ChangePosition(1,0)


print(f"{CharacterName} has changed coordinates to X = {Character_Array[position].GetX()} and Y = {Character_Array[position].GetY()}")





