#Question 1

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

    if FirstCharacter == "a" or FirstCharacter == "e"or FirstCharacter == "i" or FirstCharacter == "o"or FirstCharacter == "u":
        return 1 + RecursiveVowels(Value[1:len(Value)])
    else:
        return RecursiveVowels(Value[1:len(Value)])



#main program
print(IterativeVowels("house"))
print(RecursiveVowels("imagine"))

#Question 2

global Queue
global HeadPointer
global TailPointer

Queue = [] #stores 50 strings
HeadPointer = -1
TailPointer = 0

#need to fix some issues here
def Enqueue(DataToAdd):
    global TailPointer, HeadPointer
    HeadPointer = 0

    if TailPointer > 49:
        print("Queue is full!")
    else:
        Queue.append(DataToAdd)
        TailPointer += 1

def Dequeue():
    global  HeadPointer
    if HeadPointer == -1:
        print("Empty")
    else:
        DataToRemove = Queue[HeadPointer]
        HeadPointer -= 1
        return DataToRemove     

def ReadData():
    file = open("QueueData.txt")
    for line in file:
        Enqueue(line.strip())
    file.close()
    


#Question 3

class Character:
    def __init__(self, Name, XPosition, YPosition):
        self.__Name = Name #String
        self.__XPosition = XPosition # Integer
        self.__YPosition = YPosition # Integer
    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self, value):
        if value > 10000:
            value = 10000
            self.__XPosition = value
        elif value < 0 :
            value = 0
            self.__XPosition = value
    def SetYPosition(self, value):
        if value > 10000:
            value = 10000
            self.__YPosition = value
        elif value < 0 :
            value = 0
            self.__YPosition = value

    #to be continued


