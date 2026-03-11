class SaleData:
    def __init__(self, ID, Quantity):
        self.ID = ID  # string
        self.Quantity = Quantity  # integer


def Enqueue(RecordToAdd):
    global CircularQueue, Tail, NumberOfItems
    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = RecordToAdd
        NumberOfItems += 1
        if Tail == 4:
            Tail = 0
        else:
            Tail = Tail + 1
        return 1


def Dequeue():
    global CircularQueue, Head, Tail, NumberOfItems
    if NumberOfItems == 0:
        return ""
    else:
        RecordRemoved = CircularQueue[Head]
        if Head == 4:
            Head = 0
        else:
            Head = Head + 1
        NumberOfItems -= 1
        return RecordRemoved


def EnterRecord():
    Id = input("Enter the ID: ")
    Qty = int(input("Enter the quantity: "))
    NewRecord = SaleData(Id, Qty)

    if Enqueue(NewRecord) == -1:
        print("Full")
    else:
        print("Stored")


# main program

global CircularQueue, Head, Tail, NumberOfItems
CircularQueue = []
Head = 0
Tail = 0
NumberOfItems = 0

for i in range(5):
    CircularQueue.append(SaleData("", -1))

for i in range(6):
    EnterRecord()

RemovedRecord = Dequeue()
if RemovedRecord == "":
    print("Queue is empty")
else:
    print(f"The ID is: {RemovedRecord.ID} and Quantity is: {RemovedRecord.Quantity}")

EnterRecord()

for i in range(5):
    print(f"The ID is: {CircularQueue[i].ID} and the Quantity is: {CircularQueue[i].Quantity}")
