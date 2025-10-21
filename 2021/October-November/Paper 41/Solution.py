#Question 2
from pydoc import describe


class Picture:
    def __init__(self, Description, Width, Height, FrameColour):
        self.__Description = Description #String
        self.__Width = Width #Integer
        self.__Height = Height #Integer
        self.__FrameColour = FrameColour #String
    def GetDescription(self):
        return self.__Description
    def GetHeight(self):
        return self.__Height
    def GetWidth(self):
        return self.__Width
    def GetColour(self):
        return self.__FrameColour
    def SetDescription(self, NewDescription):
        self.__Description = NewDescription
        return self.__Description


def ReadData():
    try:
        file = open("Pictures.txt","r")
        #There are two ways to read the file
        description = file.readline().strip()
        while(description != ""):
            width = file.readline().strip()
            height = file.readline().strip()
            framecolour = file.readline().strip()
            Pictures.append(Picture(description,width,height,framecolour))
            description = file.readline().strip()
        # count = 1
        # for line in file:
        #     if count == 1 :
        #         description = line.strip()
        #     if count == 2:
        #         width = line.strip()
        #     if count == 3:
        #         height = line.strip()
        #     if count == 4:
        #         framecolour = line.strip()
        #         Pictures.append(Picture(description, width, height, framecolour))
        #         count = 0
        #     count += 1

    except IOError:
        print("File not found")

#main program
Pictures = [] #Stores 100 elements

ReadData()
print(Pictures[1].GetColour())
