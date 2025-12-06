def ReadHighScores():
    global PlayerNames
    global Scores

    file = open("HighScore.txt")

    line = file.readline().strip()

    while line != "":
        line2 = file.readline().strip()

        PlayerNames.append(line)
        Scores.append(int(line2))

        line = file.readline().strip()

def OutputHighScores():
    global Scores
    global PlayerNames

    for i in range(len(PlayerNames)):
        print(PlayerNames[i] + " ", Scores[i])

def AddScore(Name, NewScore):
    global PlayerNames
    global Scores

    PlayerNames.append(Name)
    Scores.append(NewScore)

    length = len(Scores)

    for i in range(1, length):
        keyScore = Scores[i]
        keyName = PlayerNames[i]

        prev = i - 1

        while prev >= 0 and keyScore > Scores[prev]:
            Scores[prev + 1] = Scores[prev]
            PlayerNames[prev + 1] = PlayerNames[prev]

            prev -= 1
        Scores[prev + 1] = keyScore
        PlayerNames[prev + 1] = keyName

def WriteTopTen():
    global Scores
    global PlayerNames
    file = open("NewHighScore.txt", "w")

    for i in range(10):
        file.write(PlayerNames[i] + "\n")
        file.write(str(Scores[i]) + "\n")

    file.close()


#main program
global PlayerNames
global Scores

PlayerNames = [] #stores 11 strings
Scores = [] #stores 11 integers

ReadHighScores()
OutputHighScores()


NewPlayerName = input("Enter 3-character player name: ")

while len(NewPlayerName) != 3:
    NewPlayerName = input("Enter 3-character player name: ")


NewScore = int(input("Enter a score: "))

while NewScore < 1 or NewScore > 100000:
    NewScore = int(input("Enter a score: "))

AddScore(NewPlayerName, NewScore)
OutputHighScores()



