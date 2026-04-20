def ReadData():
    DataArray = ["" for _ in range(45)]

    try:
        file = open("Data.txt")
        pointer = 0

        for line in file:
            line = line.strip()
            DataArray[pointer] = line
            pointer += 1

        file.close()

        return DataArray
    except IOError:
        print("File not found")

def FormatArray(DataArray):
    text = ""
    for item in DataArray:
        text = text + item + " "
    return text

def CompareStrings(Item1, Item2):
    pointer = 0

    while True:
        if Item1[pointer] == Item2[pointer]:
            pointer += 1
        elif Item2[pointer] > Item1[pointer]:
            return 1
        else:
            return 2

def Bubble(DataArray):
    length = len(DataArray)
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(length - 1):
            if CompareStrings(DataArray[i], DataArray[i+1]) == 2:
                temp = DataArray[i]
                DataArray[i] = DataArray[i+1]
                DataArray[i+1] = temp
                isSorted = False
    return DataArray


#main program
ReturnedArray = ReadData()
print(FormatArray(ReturnedArray))

print(FormatArray(Bubble(ReturnedArray)))




