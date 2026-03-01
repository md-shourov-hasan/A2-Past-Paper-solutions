def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        Mid = (Lower + (Upper - 1)) // 2
        if SearchArray[Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)

    return -1


def OutputItems():
    global ArrayData

    for rows in range(10):
        print(ArrayData[rows])


# Main program
import random

ArrayData = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

OutputItems()

ArrayLength = 10

for x in range(0, ArrayLength):
    for y in range(0, ArrayLength - 1):
        for z in range(0, ArrayLength - y - 1):
            if ArrayData[x][z] > ArrayData[x][z + 1]:
                TempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z + 1]
                ArrayData[x][z + 1] = TempValue

print("After Bubble Sort: ")
OutputItems()

Test1 = int(input("Enter the number for first test: "))
Test2 = int(input("Enter a number for second test: "))

print(f"Test 1 results: {BinarySearch(ArrayData[0], 0, 10, Test1)} ")
print(f"Test 2 results: {BinarySearch(ArrayData[0], 0, 10, Test2)} ")
