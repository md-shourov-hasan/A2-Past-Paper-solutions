def ReadData():
    Data = []
    FileName = input("Enter a filename: ")

    try:
        file = open(FileName,"r")

        for line in file:
            line = line.strip()
            Data.append(line)
        file.close()

        return Data
    except IOError:
        print("File couldn't found!")

def SplitData(DataArray):
    Red = []
    Green = []
    Blue = []
    Orange = []
    Yellow = []
    Pink = []

    length = len(DataArray)

    for i in range(length):
        line = DataArray[i].split(",")

        if line[1].strip() == "red":
            Red.append(int(line[0]))

        elif line[1].strip() == "green":
            Green.append(int(line[0]))

        elif line[1].strip() == "blue":
            Blue.append(int(line[0]))

        elif line[1].strip() == "orange":
            Orange.append(int(line[0]))

        elif line[1].strip() == "yellow":
            Yellow.append(int(line[0]))

        elif line[1].strip() == "pink":
            Pink.append(int(line[0]))

    StoreData(Red,"Red.txt")
    StoreData(Blue, "Blue.txt")
    StoreData(Green, "Green.txt")
    StoreData(Orange, "Orange.txt")
    StoreData(Pink, "Pink.txt")
    StoreData(Yellow, "Yellow.txt")


def StoreData(DataToStore,FileName):
    try:
        file = open(FileName,"w")
        length = len(DataToStore)
        for i in range(length):
            file.write(str(DataToStore[i]) + "\n")

        file.close()

    except IOError:
        print("File not found!")

#main program
Data = ReadData()
SplitData(Data)