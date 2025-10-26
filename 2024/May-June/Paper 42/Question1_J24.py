global WordArray, NumberOfAnswers
WordArray = []

def ReadWords(FileName):
    global NumberOfAnswers
    file = open(FileName,"r")
    WordArray.append(file.readline().strip())
    NumberOfAnswers = 0
    for line in file:
        WordArray.append(line.strip())
        NumberOfAnswers +=1
    file.close()
    Play()


def Play():

    CorrectAnswer = 0

    print(f"The main word is: {WordArray[0]}. The number of answers is {NumberOfAnswers}")
    word = input("Enter a word: ")

    while word != "no":
        Found = False
        for i in range(1,len(WordArray)):
            if WordArray[i] == word:
                Found = True
                WordArray[i] = ""
        if Found:
            CorrectAnswer += 1
            print(f"{word} is an answer!")
        else:
            print(f"{word} is not an answer!")
        word = input("Enter the next word: ")

    print("The percentage of answers entered: ", (CorrectAnswer/NumberOfAnswers)*100)
    for i in range(len(WordArray)):
        print(WordArray[i])


#main program
choice = input("Do you want the main word to be easy/medium/hard?: ")
if choice == "easy":
    ReadWords("Easy.txt")
elif choice == "medium":
    ReadWords("Medium.txt")
elif choice == "hard":
    ReadWords("Hard.txt")



