class Character:
    def __init__(self, Name, XPosition, YPosition):
        self.__Name = Name  # String
        self.__XPosition = XPosition  # Integer
        self.__YPosition = YPosition  # Integer

    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self, value):
        if value > 10000:
            value = 10000
        elif value < 0:
            value = 0
        self.__XPosition = value

    def SetYPosition(self, value):
        if value > 10000:
            value = 10000
        elif value < 0:
            value = 0
        self.__YPosition = value

    def Move(self, Direction):
        if Direction == "up":
            self.SetYPosition(self.GetYPosition() + 10)
        elif Direction == "down":
            self.SetYPosition(self.GetYPosition() - 10)
        elif Direction == "left":
            self.SetXPosition(self.GetXPosition() - 10)
        elif Direction == "right":
            self.SetXPosition(self.GetXPosition() + 10)


class BikeCharacter(Character):
    def __init__(self, Name, XPosition, YPosition):
        super().__init__(Name, XPosition, YPosition)

    def Move(self, Direction):
        if Direction == "up":
            self.SetYPosition(self.GetYPosition() + 20)
        elif Direction == "down":
            self.SetYPosition(self.GetYPosition() - 20)
        elif Direction == "left":
            self.SetXPosition(self.GetXPosition() - 20)
        elif Direction == "right":
            self.SetXPosition(self.GetXPosition() + 20)


Jack = Character("jack", 50, 50)
Karla = BikeCharacter("karla", 100, 50)

Name = input("Enter the name of the character you want to move: ")

if Name == "jack":
    Direction = input("Enter the direction you want to move: ")
    if Direction != "up" and Direction != "down" and Direction != "left" and Direction != "right":
        print("Invalid Direction")
    else:
        Jack.Move(Direction)
        print(f"Jack's new position is X = {Jack.GetXPosition()} Y = {Jack.GetYPosition()}")
elif Name == "karla":
    Direction = input("Enter the direction you want to move: ")
    if Direction != "up" and Direction != "down" and Direction != "left" and Direction != "right":
        print("Invalid Direction")
    else:
        Karla.Move(Direction)
        print(f"Karla's new position is X = {Karla.GetXPosition()} Y = {Karla.GetYPosition()}")
else:
    print("Character not found!")