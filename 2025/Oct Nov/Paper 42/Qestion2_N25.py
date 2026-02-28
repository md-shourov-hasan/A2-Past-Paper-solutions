import random

TheArray = []
for _ in range(20):
    TheArray.append(random.randint(0,100))

def PrintArray(Array):
    text = ""
    for i in range(len(Array)):
        text += str(Array[i]) + " "
    print(text)

def BubbleSort(Array):
    length = len(Array)
    for j in range(length-1):
        for i in range(length-1-j):
            if Array[i] > Array[i+1]:
                temp = Array[i]
                Array[i] = Array[i+1]
                Array[i+1] = temp
    return Array

def RecursiveBinarySearch(Array, Lower, Upper, ToFind):
    Mid = (Lower + Upper)//2
    if Array[Mid] == ToFind:
        return Mid
    elif Lower > Upper:
        return -1

    elif Array[Mid] < ToFind:
        return RecursiveBinarySearch(Array,Mid + 1, Upper, ToFind)
    elif Array[Mid] > ToFind:
        return RecursiveBinarySearch(Array,Lower, Mid -1, ToFind)




#main program
PrintArray(TheArray)
BubbleSort(TheArray)
print("Sorted")
PrintArray(TheArray)

number = int(input("Enter a number: "))
ReturnedValue = RecursiveBinarySearch(TheArray,0,19,number)

if ReturnedValue == -1:
    print("Not found")
else:
    print("Found at position ", ReturnedValue)


