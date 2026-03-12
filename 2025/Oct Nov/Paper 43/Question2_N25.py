Queue = ["" for _ in range(100)]
QueueHead = -1
QueueTail = -1
NumberItems = 0
NewString = ""


def Enqueue(DataToAdd):
    global Queue
    global NumberItems
    global QueueTail
    global QueueHead

    if NumberItems == 100:
        return False
    if QueueHead == -1:
        QueueHead = 0

    QueueTail += 1
    Queue[QueueTail] = DataToAdd

    NumberItems += 1

    return True


def Dequeue():
    global NumberItems
    global Queue
    global QueueHead

    if NumberItems == 0:
        return "False"

    result = Queue[QueueHead]
    QueueHead += 1
    NumberItems -= 1

    return result


def ReadData():
    try:
        file = open("BinaryData.txt", "r")

        line = file.readline().strip()
        count = 0

        while line != "" and count < 100:
            isAdded = Enqueue(line)
            line = file.readline().strip()
            count += 1

        file.close()
    except IOError:
        print("File not found")


def Compress():
    global NewString

    Value = Dequeue()

    while Value != "False":

        if Value == "0":
            count = 0
            text = ""
            while Value == "0":
                count += 1
                Value = Dequeue()
            text = "0" + str(count)
            NewString += text

        if Value == "1":
            count = 0
            while Value == "1":
                count += 1
                Value = Dequeue()
            text = "1" + str(count)
            NewString += text


# main program
ReadData()
Compress()
print(NewString)
