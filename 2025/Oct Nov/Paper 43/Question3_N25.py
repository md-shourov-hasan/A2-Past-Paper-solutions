def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    index = NumberElements - 1
    if NumberElements == 0:
        return 0
    if ArrayCopy[index] == DataToFind:
        NumberElements -= 1
        return 1 + RecursiveCount(ArrayCopy, NumberElements, DataToFind)
    else:
        NumberElements -= 1
        return RecursiveCount(ArrayCopy, NumberElements, DataToFind)


def SplitData(line):
    flag = ";"
    length = len(line)
    text = ""
    TextArray = []

    for i in range(length):
        if line[i] != flag:
            text += line[i]
        elif line[i] == flag:
            TextArray.append(text)
            text = ""
    return TextArray


# main program

DataArray = [0, 5, 1, 2, 5, 9, 9, 6, 5, 0]

print(RecursiveCount(DataArray, 10, 0))

Data = "x=0;y=1;x=x+y;y++;"

Returned_Array = SplitData(Data)

for i in Returned_Array:
    print(i)
