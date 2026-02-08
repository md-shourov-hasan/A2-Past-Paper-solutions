class Node:
    def __init__(self, PData):
        self.__LeftPointer = -1
        self.__Data = PData #integer
        self.__RightPointer = -1

    def GetLeft(self):
        return self.__LeftPointer

    def GetRight(self):
        return self.__RightPointer

    def GetData(self):
        return self.__Data

    def SetLeft(self, value):
        self.__LeftPointer = value

    def SetRight(self, value):
        self.__RightPointer = value

    def SetData(self, value):
        self.__Data = value


class TreeClass:
    def __init__(self):
        self.__Tree = [Node(-1)] * 20 #type Node 20 spaces
        self.__FirstNode = -1
        self.__NumberNodes = 0
#to be continued

