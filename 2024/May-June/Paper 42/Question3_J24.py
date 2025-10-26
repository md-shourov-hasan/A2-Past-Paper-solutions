def RecursiveInsertion(IntegerArray, NumberElements):
    global LastItem, CheckItem, LoopAgain

    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2

    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False

    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

def IterativeInsertiion(IntegerArray):

    for j in range(1,len(IntegerArray)):
        key = IntegerArray[j]
        i = j - 1
        while i >= 0 and key < IntegerArray[i]:
            IntegerArray[i+1] = IntegerArray[i]
            i -= 1
        IntegerArray[i+1] = key
    return IntegerArray

def BinarySearch(IntegerArray, First, Last, ToFind):

    if First > Last:
        return -1
    else:
         Mid = (First + Last)//2

    if IntegerArray[Mid] == ToFind:
        return Mid
    elif IntegerArray[Mid] > ToFind:
        return BinarySearch(IntegerArray, First, Mid - 1, ToFind)
    elif IntegerArray[Mid] < ToFind:
        return BinarySearch(IntegerArray,Mid + 1, Last, ToFind)




# #Main Program
#
NumberArray=[]
NumberArray.append(100)
NumberArray.append(85)
NumberArray.append(644)
NumberArray.append(22)
NumberArray.append(15)
NumberArray.append(8)
NumberArray.append(1)
#
#
# print("Recursive")
# print(RecursiveInsertion(NumberArray,len(NumberArray)))
#
#
print("iterative")
print(IterativeInsertiion(NumberArray))

print(BinarySearch(NumberArray,0,6,100))