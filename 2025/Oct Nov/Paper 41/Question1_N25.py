import random

Stack = [None for x in range(30)]
TopOfStack = -1


def Push(DataToPush):
    global TopOfStack
    global Stack

    if TopOfStack == 29:
        return False
    TopOfStack += 1

    Stack[TopOfStack] = DataToPush

    return True


def Pop():
    global Stack
    global TopOfStack

    if TopOfStack == -1:
        return -999

    Value = Stack[TopOfStack]
    TopOfStack -= 1
    return Value


def FindValues():
    max = min = Pop()

    ReturnedValue = min

    while ReturnedValue != -999:
        if ReturnedValue > max:
            max = ReturnedValue
        elif ReturnedValue < min:
            min = ReturnedValue

        ReturnedValue = Pop()
    print(f"The smallest number is: {min} and the largest number is: {max}")


# main program

for _ in range(40):
    number = random.randint(0, 1000)
    isEmpty = Push(number)
    if isEmpty == False:
        print("Stack full")
        break

FindValues()
