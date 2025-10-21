#Question 3
global Queue, HeadPointer, TailPointer
Queue = [] #Stores upto 100 Integers
HeadPointer = 0
TailPointer = 0

def Enqueue(Data):
    global TailPointer
    if TailPointer == 100:
        return False
    else:
        Queue.append(Data)
        TailPointer += 1
        return True

for i in range(21):
    if Enqueue(i) == True:
        print("Successful")
    elif Enqueue(i) == False:
        print("Unsuccessful")

def IterativeOutput(Start):
    if Start < 1:
        return 0
    else:
        return 0 + Queue[Start - 1] + IterativeOutput(Start - 1)

print(IterativeOutput(TailPointer))
