class Node:
    def __init__(self, PData):
        self.__LeftPointer = -1
        self.__Data = PData  # integer
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
        self.__Tree = [Node(-1)] * 20  # type Node 20 spaces
        self.__FirstNode = -1  # integer
        self.__NumberNodes = 0  # integer

    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes += 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            current_index = self.__FirstNode

            while current_index != -1:
                parent_index = current_index

                if NewNode.GetData() > self.__Tree[current_index].GetData():
                    direction = "right"
                    current_index = self.__Tree[current_index].GetRight()
                elif NewNode.GetData() < self.__Tree[current_index].GetData():
                    direction = "left"
                    current_index = self.__Tree[current_index].GetLeft()

            if direction == "left":
                self.__Tree[parent_index].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[parent_index].SetRight(self.__NumberNodes)

            self.__NumberNodes += 1

    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for i in range(self.__NumberNodes):
                print(
                    f"Left Pointer: {self.__Tree[i].GetLeft()} Data: {self.__Tree[i].GetData()} Right Pointer: {self.__Tree[i].GetRight()}")


TheTree = TreeClass()

TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))

TheTree.OutputTree()
