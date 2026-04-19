def ReadData():
    Data_array = []  # stores 45 items
    file = open("Data.txt", "r")
    for line in file:
        Data_array.append(line.strip())
    file.close()
    return Data_array


def FormatArray(String_Array):
    size = len(String_Array)
    concatenated_string = ""

    for i in range(0, size):
        concatenated_string = concatenated_string + String_Array[i] + " "

    return concatenated_string


def CompareStrings(firstString, secondString):
    index = 0

    while True:
        if firstString[index] == secondString[index]:
            index += 1
        else:
            if firstString[index] < secondString[index]:
                return 1
            else:
                return 2


def Bubble(Data_array):
    length = len(Data_array)

    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, length - 1):
            if CompareStrings(Data_array[i], Data_array[i + 1]) == 2:
                Data_array[i], Data_array[i + 1] = Data_array[i + 1], Data_array[i]
                sorted = False


# main program
Main_array = ReadData()
print(FormatArray(Main_array))

Bubble(Main_array)
print(FormatArray(Main_array))