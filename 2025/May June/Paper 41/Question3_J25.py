class Node:
    def __init__(self, PNodeData):
        self.__NodeData = PNodeData  # integer
        self.__LeftNode = None  # type Node
        self.__RightNode = None  # type Node

    def GetLeft(self):
        return self.__LeftNode

    def GetRight(self):
        return self.__RightNode

    def GetData(self):
        return self.__NodeData

    def SetLeft(self, Value):
        self.__LeftNode = Value

    def SetRight(self, Value):
        self.__RightNode = Value


class Tree:
    def __init__(self, PFirstNode):
        self.__FirstNode = PFirstNode  # Type Node

    def GetRootNode(self):
        return self.__FirstNode

    def Insert(self, PNode):

        Root = self.GetRootNode()
        Found = False

        while Found == False:

            if PNode.GetData() < Root.GetData():

                if Root.GetLeft() == None:
                    Root.SetLeft(PNode)
                    Found = True
                else:
                    Root = Root.GetLeft()

            elif PNode.GetData() >= Root.GetData():

                if Root.GetRight() == None:
                    Root.SetRight(PNode)
                    Found = True
                else:
                    Root = Root.GetRight()


# main program

def OutputInOrder(PNode):
    if PNode.GetLeft() != None:

        OutputInOrder(PNode.GetLeft())

    print(PNode.GetData())

    if PNode.GetRight() != None:

        OutputInOrder(PNode.GetRight())


Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)

Tree1 = Tree(Node1)
Tree1.Insert(Node2)
Tree1.Insert(Node3)
Tree1.Insert(Node4)
Tree1.Insert(Node5)
OutputInOrder(Node1)
