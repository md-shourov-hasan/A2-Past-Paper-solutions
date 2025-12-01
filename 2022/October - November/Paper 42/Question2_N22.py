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
        x = int(CharacterFile.readline())
        y = int(CharacterFile.readline())
        Character_Array.append(Character(name, x, y ))
        name = CharacterFile.readline()

    CharacterFile.close()
except IOError:
    print("File not found!")

#to be continued





