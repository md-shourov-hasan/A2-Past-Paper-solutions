def Enqueue(DataToAdd):
    global Queue
    global TailPointer
    global HeadPointer

    if TailPointer == 49:
        return False
    elif TailPointer == -1:
        HeadPointer = 0

    TailPointer += 1
    Queue[TailPointer] = DataToAdd
    return True


def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer

    if HeadPointer <= TailPointer and HeadPointer != -1:
        ReturnedValue = Queue[HeadPointer]
        HeadPointer += 1
        return ReturnedValue
    else:
        return -1


def CreateQueue():
    try:
        file = open("QueueData.txt")
        for line in file:
            line = line.strip()
            isAdded = Enqueue(int(line))

            if not isAdded:
                print("Queue full")
        file.close()
    except IOError:
        print("File not found!")


# main program
Queue = [-1 for _ in range(50)]
HeadPointer = -1
TailPointer = -1



CreateQueue()
total = 0
ReturnedValue = Dequeue()

while ReturnedValue != -1:
    total += ReturnedValue
    ReturnedValue = Dequeue()

print(total)
