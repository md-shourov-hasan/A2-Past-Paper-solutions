def Initialise():
    global DataStored
    global NumberItems

    Quantity = int(input("Enter the quantity of numbers you want to enter: "))
    while Quantity < 1 or Quantity > 20:
        Quantity = int(input("Enter the quantity of numbers you want to enter: "))

    for i in range(Quantity):
        number = int(input("Enter a number: "))

        DataStored.append(number)
        NumberItems += 1


def BubbleSort():
    global DataStored
    global NumberItems

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(NumberItems - 1):
            if DataStored[i] > DataStored[i + 1]:
                temp = DataStored[i + 1]
                DataStored[i + 1] = DataStored[i]
                DataStored[i] = temp
                is_sorted = False


def BinarySearch(DataToFind):
    global DataStored
    global NumberItems

    start = 0
    end = NumberItems - 1

    while start <= end:
        mid = (start + end) // 2

        if DataStored[mid] == DataToFind:
            return mid
        elif DataStored[mid] > DataToFind:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# main program
DataStored = []  # stores upto 20 integers
NumberItems = 0  # integer

Initialise()
print(DataStored)
BubbleSort()
print(DataStored)

number = int(input("Enter a number to find: "))
print(BinarySearch(number))
