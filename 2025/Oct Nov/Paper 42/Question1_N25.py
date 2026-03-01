class Bird:
    def __init__(self, PSpecies, PDistancePerHour):
        self.__Species = PSpecies  # string
        self.__DistancePerHour = PDistancePerHour  # Real
        self.__XPosition = 500.0  # Real
        self.__YPosition = 500.0  # Real

    def GetSpecies(self):
        return self.__Species

    def GetPosition(self):
        return "X = " + str(self.__XPosition) + " Y = " + str(self.__YPosition)

    def Move(self, Direction, Minutes):
        distance = (self.__DistancePerHour / 60) * Minutes

        if Direction == 'N':
            self.__YPosition += distance
        elif Direction == 'S':
            self.__YPosition -= distance
        elif Direction == 'E':
            self.__XPosition += distance
        elif Direction == 'W':
            self.__XPosition -= distance


# main program
FirstBird = Bird("Cockatiel", 71.0)
SecondBird = Bird("Macaw", 56.0)

print(
    f"The species for first bird is: {FirstBird.GetSpecies()} and current X and Y position is {FirstBird.GetPosition()}")
print(
    f"The species for second bird is: {SecondBird.GetSpecies()} and current X and Y position is {SecondBird.GetPosition()}")

User_Bird = input("Select one of the birds to move: ")
while User_Bird != FirstBird.GetSpecies() and User_Bird != SecondBird.GetSpecies():
    User_Bird = input("Select one of the birds to move: ")

if User_Bird == FirstBird.GetSpecies():
    ChosenBird = FirstBird
else:
    ChosenBird = SecondBird

Direction = input("Enter the direction the bird has been travelling (N/S/E/W): ")

while Direction != 'N' and Direction != 'S' and Direction != 'E' and Direction != 'W':
    Direction = input("Enter the direction the bird has been travelling (N/S/E/W): ")

Time = int(input("Enter the time in nearest minute between 0 and 500 inclusive: "))

while Time < 0 or Time > 500:
    Time = int(input("Enter the time in nearest minute between 0 and 500 inclusive: "))

ChosenBird.Move(Direction, Time)

print(f"The updated bird position is: {ChosenBird.GetPosition()}")
