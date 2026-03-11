class Node:
    def __init__(self, PTheData):
        self.__TheData = PTheData  # integer
        self.__NextNode = None # node

    def GetData(self):
        return self.__TheData

    def GetNextNode(self):
        return self.__NextNode

    def SetNextNode(self, PNode):
        self.__NextNode = PNode


class LinkedList:
    def __init__(self):
        self.HeadNode = Node(None)  # node

    def InsertNode(self, PInteger):
        NewNode = Node(PInteger)
        NewNode.SetNextNode(self.HeadNode)
        self.HeadNode = NewNode

    def Traverse(self):
        text = ""

        Pointer = self.HeadNode
        data = Pointer.GetData()
        while data != None:
            text += str(data) + " "
            Pointer = Pointer.GetNextNode()
            data = Pointer.GetData()
        return text

    def RemoveNode(self, PInteger):
        if self.HeadNode.GetData() == None:
            return False

        if self.HeadNode.GetData() == PInteger:
            self.HeadNode = self.HeadNode.GetNextNode()
            return True


        isFound = False
        Pointer = self.HeadNode

        while isFound == False and Pointer.GetNextNode().GetData() != None:

            if Pointer.GetNextNode().GetData() == PInteger:
                Pointer.SetNextNode(Pointer.GetNextNode().GetNextNode())
                isFound = True
            else:
                Pointer = Pointer.GetNextNode()
        return isFound

NewList = LinkedList()
NewList.InsertNode(10)
NewList.InsertNode(20)
NewList.InsertNode(30)
NewList.InsertNode(40)
NewList.InsertNode(50)

print(NewList.Traverse())
NewList.RemoveNode(30)
print(NewList.Traverse())
