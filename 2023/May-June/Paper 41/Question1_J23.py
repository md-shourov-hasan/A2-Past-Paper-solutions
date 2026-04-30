DataArray = [] #stores 25 integers


def PrintArray(Array):
    line = ""
    for item in Array:
        line += str(item) + " "
    print(line)

def LinearSearch(Array, DataToFind):
    count = 0
    for item in Array:
        if item == DataToFind:
            count += 1
    return count



#main program

try:
    file = open("Data.txt")

    for line in file:
        data = int(line.strip())
        DataArray.append(data)
    file.close()
except IOError:
    print("File not found!")

PrintArray(DataArray)


number = int(input("Enter a number between 0 and 100: "))

while number < 0 or number > 100:
    number = int(input("Try again: "))

Returned_Value = LinearSearch(DataArray, number)

print("The number " + str(number) + " is found " + str(Returned_Value) + " times.")