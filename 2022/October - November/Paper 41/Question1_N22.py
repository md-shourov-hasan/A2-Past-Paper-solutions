global DataArray
DataArray = []  # Stores 100 integers


def ReadFile():
    try:
        file = open("IntegerData.txt")

        for line in file:
            DataArray.append(int(line.strip()))
        file.close()
    except IOError:
        print("File not found!")


def FindValues():
    global DataArray

    count = 0
    search = int(input("Enter a number: "))
    while search < 1 or search > 100:
        search = int(input("Enter a number: "))

    for i in range(100):
        if search == DataArray[i]:
            count += 1
    return count


def BubbleSort():
    global DataArray

    for i in range(len(DataArray) - 1):
        for j in range(len(DataArray) - i - 1):
            if DataArray[j] > DataArray[j + 1]:
                DataArray[j], DataArray[j + 1] = DataArray[j + 1], DataArray[j]
    return DataArray


# main program

ReadFile()
Result = FindValues()
print(f"The number appeared: {Result} times")

print(BubbleSort())
