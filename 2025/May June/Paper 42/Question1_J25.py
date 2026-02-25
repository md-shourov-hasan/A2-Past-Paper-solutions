global Stack
global TopOfStack

Stack = ["-1"]*20 #stores upto 20 elements
TopOfStack = -1

def Push(DataToPush):
    global TopOfStack
    global Stack

    if TopOfStack == 19:
        return -1
    TopOfStack += 1

    Stack[TopOfStack] = DataToPush

    return 1

def Pop():
    global TopOfStack
    global Stack

    if TopOfStack == -1:
        return "-1"

    Data = Stack[TopOfStack]
    TopOfStack -= 1

    return  Data

def ReadData(FileName):
    try:
        file = open(FileName,"r")

        for line in file:
            insert = Push(line.strip())
            if insert == -1:
                print("Stack full")
        file.close()

    except IOError:
        print("File not found")

def Calculate():

    returnedValue = Pop()

    while returnedValue != "-1":

        if returnedValue == "+":
            total = total + int(Pop())

        elif returnedValue == "-":
            total = total - int(Pop())

        elif returnedValue == "/":
            total = total / int(Pop())

        elif returnedValue == "*":
            total = total * int(Pop())

        elif returnedValue == "^":
            total = total ** int(Pop())

        else:
            total = int(returnedValue)

        returnedValue = Pop()

    return total

FileName = input("Enter a filename: ")
ReadData(FileName)
result = Calculate()
print("The total is: ", result)