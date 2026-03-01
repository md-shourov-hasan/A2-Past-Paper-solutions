class Record:
    def __init__(self, PKey, PData):
        self.Key = PKey  # integer
        self.Data = PData  # string


def Hash(Value):
    return Value % 100


def InsertData(NewRecord):
    global HashTable

    HashValue = Hash(NewRecord.Key)
    for i in range(10):
        if HashTable[HashValue][i] == None:
            HashTable[HashValue][i] = NewRecord
            break


def ReadData():
    try:
        file = open("HashTableData.txt")

        for line in file:
            line = line.strip().split(",")
            key = int(line[0])
            data = line[1]

            InsertData(Record(key, data))

        file.close()
    except IOError:
        print("File not found")


def GetRecord(KeyField):
    global HashTable

    HashValue = Hash(KeyField)
    for i in range(10):
        if HashTable[HashValue][i] == None:
            return "Not found"
        elif HashTable[HashValue][i].Key == KeyField:
            return HashTable[HashValue][i].Data
    return "Not found"


HashTable = []


def InitialiseHashTable():
    global HashTable
    for rows in range(100):
        HashTable.append([None, None, None, None, None, None, None, None, None, None])


InitialiseHashTable()
ReadData()

for _ in range(5):
    KeyField = int(input("Enter a key field value: "))
    print(GetRecord(KeyField))
