def OutputItems():
    global StackData
    global StackPointer

    for i in range(10):
        print(StackData[i])
    print("The StackPointer Value is: ", StackPointer)


def Push(DataToPush):
    global StackData
    global StackPointer

    if StackPointer > 9:
        return False

    StackData.append(DataToPush)
    StackPointer += 1
    return True

def Pop():
    global StackData
    global StackPointer

    if StackPointer == 0:
        return -1
    StackPointer -= 1

    Data = StackData[StackPointer]



#main program

global StackData
global StackPointer

StackData = [] #Stores 10 integers
StackPointer = 0

for _ in range(11):
    Result = Push(int(input("Enter a number: ")))

    if Result:
        print("Successfully Added")
    else:
        print("Not added")

OutputItems()

Pop()
Pop()

OutputItems()

#it has some error