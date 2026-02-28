TreeArray = []

for _ in range(50):
    TreeArray.append([-1,-1,-1])

RootPointer = -1
FreeNode = 0

def AddNode(DataToStore):
    global FreeNode
    global TreeArray
    global RootPointer

    if FreeNode == 50:
        print("The tree is full")

    elif FreeNode == 0:
        TreeArray[FreeNode][1] = DataToStore
        RootPointer = 0
        FreeNode += 1

    else:
        TreeArray[FreeNode][1] = DataToStore

        Pointer = RootPointer
        Found = False

        while Found == False:

            if DataToStore < TreeArray[Pointer][1]:
                if TreeArray[Pointer][0] == -1:
                    TreeArray[Pointer][0] = FreeNode
                    Found = True
                else:
                    Pointer = TreeArray[Pointer][0]

            elif DataToStore > TreeArray[Pointer][1]:
                if TreeArray[Pointer][2] == -1:
                    TreeArray[Pointer][2] = FreeNode
                    Found = True
                else:
                    Pointer = TreeArray[Pointer][2]
        FreeNode += 1

def WriteAllToFile():
    global TreeArray
    try:
        File = open("Tree.txt","w")
        length = len(TreeArray)

        for i in range(length):
            line = str(TreeArray[i][0]) + "," + str(TreeArray[i][1]) + "," + str(TreeArray[i][2]) + "\n"
            File.write(line)

        File.close()
    except:
        print("Cannot write file")



#main program
try:
    File = open("TreeData.txt","r")

    for line in File:
        number = int(line.strip())
        AddNode(number)

    File.close()
except IOError:
    print("File not found")

WriteAllToFile()