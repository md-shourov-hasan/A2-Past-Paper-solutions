def Enqueue(DataToInsert):
    global QueueHead
    global QueueTail
    global QueueData

    if QueueTail == 19:
        return False

    if QueueHead == -1:
        QueueHead = 0
    QueueTail += 1
    QueueData[QueueTail] = DataToInsert

    return True


def Dequeue():
    global QueueHead
    global QueueTail
    global QueueData

    if QueueHead == -1:
        return "false"
    ReturnedValue = QueueData[QueueHead]
    QueueHead += 1

    return ReturnedValue


def StoreItems():
    invalid_counter = 0
    for _ in range(10):
        user_text = input("Enter a 7-character string: ")
        check_digit = str((int(user_text[0]) * 1 + int(user_text[1]) * 3 + int(user_text[2]) * 1 + int(
            user_text[3]) * 3 + int(user_text[4]) * 1 + int(user_text[5]) * 3) // 10)

        if check_digit == "10":
            check_digit = "X"
        if check_digit == user_text[6]:
            isAdded = Enqueue(user_text[0:6])

            if isAdded:
                print("The item is inserted!")
            else:
                print("Queue is full!")
        else:
            invalid_counter += 1
    print("There were " + str(invalid_counter) + " invalid inputs")


# main program
QueueData = ["" for _ in range(20)]  # stores 20 strings
QueueHead = -1
QueueTail = -1

StoreItems()
removedItem = Dequeue()

if removedItem == "false":
    print("The Queue is empty")
else:
    print("The returned value is: ", removedItem)
