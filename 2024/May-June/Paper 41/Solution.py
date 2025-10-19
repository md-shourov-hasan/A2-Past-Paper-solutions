#Solution goes here

def Initialise():
    NumberItems = int(input("Enter quantity of numbers you want to enter: "))

    while NumberItems < 1 or NumberItems > 20:
        NumberItems = int(input("Enter quantity of numbers you want to enter: "))
    
    for i in range(NumberItems):
        DataStored.append(int(input("Enter the number: ")))
        NumberItems += 1


def BubbleSort():
    length = len(DataStored)
    for i in range(length-1):
        for x in range(length - 1 - i):
            if DataStored[x] > DataStored[x+1]:
                DataStored[x], DataStored[x+1] = DataStored[x+1], DataStored[x]


def BinarySearch(DataToFind):
    length = len(DataStored)
    start = 0
    end = length - 1

    while start <= end:
        mid = (start + end) // 2
        if DataToFind == DataStored[mid]:
            return mid
        elif DataToFind > DataStored[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1
    


#main program
DataStored = [] #Stores 20 integers
global NumberItems
NumberItems = 0

Initialise()
print(DataStored)

BubbleSort()
print(DataStored)

Search = int(input("Enter a number to search: "))
print(BinarySearch(Search))
