# Question 1

def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    for X in range(LengthString):
        FirstCharacter = Value[0:1]
        if FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i" or FirstCharacter == "o" or FirstCharacter == "u":
            Total += 1
        Value = Value[1:len(Value)]

    return Total


def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0

    FirstCharacter = Value[0:1]

    if FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i" or FirstCharacter == "o" or FirstCharacter == "u":
        return 1 + RecursiveVowels(Value[1:len(Value)])
    else:
        return RecursiveVowels(Value[1:len(Value)])


# main program
print(IterativeVowels("house"))
print(RecursiveVowels("imagine"))

# Question 2

global Queue
global HeadPointer
global TailPointer

Queue = []  # stores 50 strings
HeadPointer = -1
TailPointer = 0


def Enqueue(DataToAdd):
    global TailPointer, HeadPointer

    if TailPointer > 49:
        print("Queue is full!")
    else:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue.append(DataToAdd)
        TailPointer += 1


def Dequeue():
    global HeadPointer
    if HeadPointer == -1:
        return "Empty"
    else:
        DataToRemove = Queue[HeadPointer]
        HeadPointer += 1
        return DataToRemove


def ReadData():
    file = open("QueueData.txt")
    for line in file:
        Enqueue(line.strip())
    file.close()


class RecordData:
    def __init__(self, ID, Total):
        self.ID = ID  # String
        self.Total = Total  # Integer


global Records, NumberRecords

Records = []  # Stores 50 items of type RecordData
NumberRecords = 0  # Integer


def TotalData():
    global Records, NumberRecords
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))
        Flag = True
        NumberRecords += 1
    else:
        for X in range(0, NumberRecords):
            if Records[X].ID == DataAccessed:
                Records[X].Total += 1
                Flag = True

    if Flag == False:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1


def OutputRecords():
    for _ in range(0, len(Records)):
        print(f"ID {Records[i].ID} Total {Records[i].Total}")


# main program
ReadData()

for i in range(0, len(Queue)):
    TotalData()

OutputRecords()


# Question 3

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
