def InsertData():
    global LinkedList
    global FirstNode
    global FirstEmpty

    for _ in range(5):
        if FirstEmpty != -1:
            nextEmpty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = int(input())
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = nextEmpty

def OutputLinkedList():
    global LinkedList
    global FirstNode
    pointer = FirstNode

    while pointer != -1:
        print(LinkedList[pointer][0])
        pointer = LinkedList[pointer][1]

def RemoveData(DataToRemove):
    global LinkedList
    global FirstNode
    global FirstEmpty

    pointer = FirstNode
    isFound = False

    while pointer != -1 and not isFound:
        if LinkedList[pointer][0] == DataToRemove:
            if pointer == FirstNode:
                FirstNode = LinkedList[pointer][1]
            else:
                prevPointer = pointer + 1
                nextPointer = LinkedList[pointer][1]
                LinkedList[prevPointer][1] = nextPointer
            isFound = True

        else:
            pointer = LinkedList[pointer][1]

#main program
LinkedList = []
FirstNode = -1
FirstEmpty = 0

for i in range(1,20):
    LinkedList.append([-1,i])
LinkedList.append([-1,-1])

InsertData()
OutputLinkedList()

RemoveData(5)
print("After")
OutputLinkedList()

