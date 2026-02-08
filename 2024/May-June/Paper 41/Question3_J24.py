def Enqueue(DataToInsert):
    global QueueTail
    global QueueData
    global QueueHead

    if QueueTail == 19:
        return False
    elif QueueHead == -1:
        QueueHead = 0

    QueueTail += 1
    QueueData[QueueTail] = DataToInsert
    return True

def Dequeue():
    global QueueHead
    global QueueData

    if QueueHead < 0 or QueueHead > 20 or QueueHead > QueueTail:
        return "false"

    Value = QueueData[QueueHead]
    QueueHead += 1
    return Value

def StoreItems():
    counter = 0
    for _ in range(10):
        Text = input("Enter data: ")
        check_digit = str((int(Text[0]) + int(Text[2]) + int(Text[4]) + int(Text[1]) * 3 + int(Text[3]) * 3 + int(Text[5]) * 3) // 10)

        if check_digit == "10":
            check_digit = "X"

        if check_digit == Text[6]:
           Result = Enqueue(Text[:6])
           if Result:
                print("Item is inserted")
           else:
                print("Queue is full")
        else:
            counter += 1

    print(f"The total invalid items are: {counter}")

#Main Program

global QueueData
global QueueHead
global QueueTail

QueueData = ["" for x in range(20)] #stores 20 empty strings
QueueHead = -1
QueueTail = -1


StoreItems()
Value = Dequeue()

if Value == "false":
    print("Queue is empty")
else:
    print(Value)