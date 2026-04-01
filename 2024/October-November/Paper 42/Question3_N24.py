def ReadData():
    Array = []

    try:
        file = open("HighScoreTable.txt")

        line1 = file.readline().strip()

        while line1 != "":
            line2 = file.readline().strip()
            line3 = file.readline().strip()
            Array.append([line1, line2, line3])

            line1 = file.readline().strip()
        file.close()

        return Array
    except IOError:
        print("File not found!")


def OutputHighScores(Array):
    for i in Array:
        text = i[0] + " reached level " + i[1] + " with a score of " + i[2]
        print(text)


def SortScores(Array):
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(len(Array) - 1):
            if int(Array[i][1]) < int(Array[i + 1][1]):
                temp = Array[i]
                Array[i] = Array[i + 1]
                Array[i + 1] = temp
                isSorted = False

            elif int(Array[i][1]) == int(Array[i + 1][1]):
                if int(Array[i][2]) < int(Array[i + 1][2]):
                    temp = Array[i]
                    Array[i] = Array[i + 1]
                    Array[i + 1] = temp
                    isSorted = False

    return Array


# main program
HighScores = []

for _ in range(7):
    HighScores.append(["", "", ""])

HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After")
OutputHighScores(HighScores)
