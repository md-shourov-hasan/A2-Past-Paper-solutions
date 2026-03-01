Queue = [-1 for x in range(20)]
HeadPointer = -1
TailPointer = -1
NumberItems = 0


def Enqueue(Data):
    global HeadPointer
    global TailPointer
    global Queue
    global NumberItems

    if NumberItems == 20:
        return False
    if TailPointer == -1:
        HeadPointer = 0
        TailPointer = 0
        Queue[TailPointer] = Data
    else:
        TailPointer += 1
        if TailPointer == 20:
            TailPointer = 0
        Queue[TailPointer] = Data
    NumberItems += 1
    return True


def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    global NumberItems

    if NumberItems == 0:
        return -1

    result = Queue[HeadPointer]
    HeadPointer += 1
    if HeadPointer == 20:
        HeadPointer = 0
    NumberItems -= 1

    if NumberItems == 0:
        HeadPointer = -1
        TailPointer = -1

    return result


# main program
for i in range(1, 26):
    isSuccessful = Enqueue(i)

    if isSuccessful:
        print(f"{i} Successful")
    else:
        print(f"{i} Unsuccessful")

print(f"The returned value is: {Dequeue()}")
print(f"The returned value is: {Dequeue()}")
