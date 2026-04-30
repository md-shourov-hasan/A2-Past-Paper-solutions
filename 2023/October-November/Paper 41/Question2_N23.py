class RecordData:
    def __init__(self,PID,PTotal):
        self.ID = PID #string
        self.Total = PTotal #integer

def Enqueue(DataToAdd):
    global Queue
    global HeadPointer
    global TailPointer

    if TailPointer > 49:
        print("The queue is full")
    else:
        if HeadPointer == -1:
            HeadPointer = 0

        Queue[TailPointer] = DataToAdd
        TailPointer += 1

def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer

    if HeadPointer == TailPointer or HeadPointer == -1:
        return "Empty"
    ReturnedValue = Queue[HeadPointer]

    HeadPointer += 1

    return ReturnedValue

def ReadData():
    global Queue

    try:
        file = open("QueueData.txt")

        for line in file:
            line = line.strip()
            Enqueue(line)
        file.close()
    except IOError:
        print("File is not found!")

def TotalData():
    global Records
    global NumberRecords

    DataAccessed = Dequeue()
    Flag = False

    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords += 1
    else:
        for x in range(0, NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total += 1
                Flag = True

    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords += 1

def OutputRecords():
    global Records
    global NumberRecords

    for i in range(NumberRecords):
        print(f"ID {Records[i].ID} Total {Records[i].Total}")

Queue = ["" for _ in range(50)] #stores 50 strings
HeadPointer = -1
TailPointer = 0

Records = [RecordData("",0) for _ in range(50)] #stores 50 items of type RecordData
NumberRecords = 0


#main program
ReadData()

while HeadPointer != TailPointer:
    TotalData()

OutputRecords()