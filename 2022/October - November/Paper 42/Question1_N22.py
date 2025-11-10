# Questtion 1

global Jobs  # Integer, 100 by 2 elements
global NumberOfJobs  # integer

Jobs = []


def Initialise():
    global Jobs
    global NumberOfJobs
    NumberOfJobs = 0
    for x in range(100):
        Jobs.append([-1, -1])


def AddJob(JobNumber, Priority):
    global NumberOfJobs
    global Jobs

    if NumberOfJobs > 99:
        print("Not Added")
    else:
        Jobs[NumberOfJobs][0] = JobNumber
        Jobs[NumberOfJobs][1] = Priority
        NumberOfJobs += 1
        print("Added")


def InsertionSort():
    global NumberOfJobs
    global Jobs

    length = NumberOfJobs
    for i in range(1, length):
        key = Jobs[i][1]
        JobNumber = Jobs[i][0]
        previous = i - 1
        while previous >= 0 and key < Jobs[previous][1]:
            Jobs[previous + 1][1] = Jobs[previous][1]
            Jobs[previous + 1][0] = Jobs[previous][0]
            previous -= 1

        Jobs[previous + 1][1] = key
        Jobs[previous + 1][0] = JobNumber


def PrintArray():
    global Jobs
    global NumberOfJobs
    for i in range(NumberOfJobs):
        print(f"{Jobs[i][0]} priority {Jobs[i][1]}")


# Main
Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

InsertionSort()
PrintArray()
