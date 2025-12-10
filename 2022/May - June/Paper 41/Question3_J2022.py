def Enqueue(QueueArray, Head, Tail, NumberOfItems, DataToAdd):

    if NumberOfItems == 10:
        return False, QueueArray, Head, Tail, NumberOfItems

    QueueArray[Tail] = DataToAdd

    if Tail >= 9:
        Tail = 0
    else:
        Tail += 1

    NumberOfItems += 1

    return True, QueueArray, Head, Tail, NumberOfItems

def Dequeue():
    global NumberOfItems
    global QueueArray
    global Head


    if NumberOfItems == 0:
        return "FALSE"

    Result = QueueArray[Head]

    if Head >= 9:
        Head = 0
    else:
        Head += 1

    NumberOfItems -= 1

    return Result


QueueArray = ["" for i in range(10)] #Stores 10 string items

Head = 0 #integer
Tail = 0 #integer
NumberOfItems = 0 #integer

for _ in range(11):
    data = input("Enter a string value: ")

    Report, QueueArray, Head, Tail, NumberOfItems = Enqueue(QueueArray, Head, Tail, NumberOfItems, data)

    if Report:
        print("Successful")
    else:
        print("Not Successful")

print(Dequeue())
print(Dequeue())

