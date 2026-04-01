class Queue:
    def __init__(self, PHead, PTail):
        self.QueueArray = []  # integer
        self.Headpointer = PHead  # integer
        self.Tailpointer = PTail  # integer


def Enqueue(AQueue, TheData):
    if AQueue.Headpointer == -1:
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Headpointer = 0
        AQueue.Tailpointer += 1
        return 1
    else:
        if AQueue.Tailpointer > 99:
            return -1
        else:
            AQueue.QueueArray[AQueue.Tailpointer] = TheData
            AQueue.Tailpointer += 1
            return 1


def Dequeue():
    global TheQueue

    if TheQueue.Headpointer == -1 or TheQueue.Headpointer == TheQueue.Tailpointer:
        return -1
    value = TheQueue.QueueArray[TheQueue.Headpointer]
    TheQueue.Headpointer += 1

    return value


def ReturnAllData():
    global TheQueue

    text = ""
    for i in range(TheQueue.Headpointer, TheQueue.Tailpointer):
        text = text + str(TheQueue.QueueArray[i]) + " "
    return text


# main program
TheQueue = Queue(-1, 0)
TheQueue.QueueArray = [-1 for _ in range(100)]

for _ in range(10):
    number = int(input("Enter an integer greater than or equal to 0: "))
    while number < 0:
        number = int(input("Try again: "))

    isAdded = Enqueue(TheQueue, number)

    if isAdded == -1:
        print("Queue is full!")
    else:
        print("The item is added to the Queue!")

print(ReturnAllData())

ReturnedValue = Dequeue()

if ReturnedValue == -1:
    print("Queue is empty")
else:
    print(ReturnedValue)

ReturnedValue = Dequeue()

if ReturnedValue == -1:
    print("Queue is empty")
else:
    print(ReturnedValue)

print(ReturnAllData())
