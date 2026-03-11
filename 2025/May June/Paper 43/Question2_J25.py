def InsertionSort(Array):
    for i in range(1, len(Array)):
        key = Array[i]
        prev = i - 1

        while prev >= 0 and key < Array[prev]:
            Array[prev + 1] = Array[prev]
            prev -= 1
        Array[prev + 1] = key

    return Array

def OutputArray(Array):
    text = ""
    for i in Array:
        text += str(i) + " "
    print(text)

def Search(DataArray,ItemToFind):
    start = 0
    end = len(DataArray) - 1
    while start <= end:
        mid = (start + end) // 2

        if DataArray[mid] == ItemToFind:
            return mid
        elif DataArray[mid] > ItemToFind:
            end = mid - 1
        else:
            start = mid + 1
    return -1




#main program

DataArray = []
DataArray.append(0)
DataArray.append(3)
DataArray.append(4)
DataArray.append(56)
DataArray.append(67)
DataArray.append(44)
DataArray.append(43)
DataArray.append(32)
DataArray.append(31)
DataArray.append(345)
DataArray.append(45)
DataArray.append(6)
DataArray.append(54)
DataArray.append(1)

OutputArray(DataArray)

Sorted_Array = InsertionSort(DataArray)
OutputArray(Sorted_Array)

test = Search(Sorted_Array,0)
if test == -1:
    print("The number is not found")
else:
    print("The number is found at index: ", test)

test = Search(Sorted_Array,345)

if test == -1:
    print("The number is not found")
else:
    print("The number is found at index: ", test)

test = Search(Sorted_Array,67)

if test == -1:
    print("The number is not found")
else:
    print("The number is found at index: ", test)

test = Search(Sorted_Array,2)

if test == -1:
    print("The number is not found")
else:
    print("The number is found at index: ", test)





