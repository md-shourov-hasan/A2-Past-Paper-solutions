class NewRecord:
    def __init__(self,PKey, PItem1, PItem2):
        self.__Key = PKey #integer
        self.__Item1 = PItem1 #integer
        self.__Item2 = PItem2 #integer

    def GetKey(self):
        return self.__Key
    def GetItem1(self):
        return self.__GetItem1
    def GetItem2(self):
        return self.__GetItem2

global HashTable
global Spare

HashTable = [] #store 200 records
Spare = [] #stores 100 record

def Initialise():
    global HashTable
    global Spare

    empty = NewRecord(-1,-1,-1)

    for _ in range(200):
        HashTable.append(empty)
    for _ in range(100):
        Spare.append(empty)

def CalculateHash(KeyField):
    return KeyField % 200

def InsertIntoHash(Record):
    global Spare
    global HashTable

    index = CalculateHash(Record.GetKey())

    if HashTable[index].GetKey() == -1:
        HashTable[index] = Record
    else:
        for x in range(100):
            if Spare[x].GetKey() == -1:
                Spare[x] = Record
                break

def CreateHashTable():
    try:
        file = open("HashData.txt")

        for line in file:
            line = line.strip().split(",")
            New = NewRecord(int(line[0]), int(line[1]), int(line[2]))

            InsertIntoHash(New)

        file.close()

    except IOError:
        print("File not found!")

def PrintSpare():
    global Spare

    for i in range(100):
        key = Spare[i].GetKey()
        if key != -1:
            print(key)

Initialise()
CreateHashTable()
PrintSpare()
