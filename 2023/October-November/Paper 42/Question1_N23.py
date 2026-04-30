StackVowel = ["" for _ in range(100)] #stores upto 100 letters
StackConsonant = ["" for _ in range(100)] #stores upto 100 letters

VowelTop = 0 #integer
ConsonantTop = 0 #integer



def PushData(DataToPush):
    global VowelTop
    global ConsonantTop
    global StackConsonant
    global StackVowel

    if DataToPush == 'a' or DataToPush == 'e' or DataToPush == 'i' or DataToPush == 'o' or DataToPush == 'u':
        if VowelTop > 99:
            print("Stack is full")
        else:
            StackVowel[VowelTop] = DataToPush
            VowelTop += 1
    else:
        if ConsonantTop > 99:
            print("Stack is full")
        else:
            StackConsonant[ConsonantTop] = DataToPush
            ConsonantTop += 1

def ReadData():
    try:
        file = open("StackData.txt")

        for line in file:
            line = line.strip()
            PushData(line)
        file.close()
    except IOError:
        print("File not found!")

def PopVowel():
    global StackVowel
    global VowelTop

    if VowelTop <= 0:
        return "No data"

    VowelTop -= 1

    return StackVowel[VowelTop]


def PopConsonant():
    global StackConsonant
    global ConsonantTop

    if ConsonantTop <= 0:
        return "No data"

    ConsonantTop -= 1

    return StackConsonant[ConsonantTop]


#main program
ReadData()

text = ""
for _ in range(5):
    choice = input("vowel or consonant: ")

    if choice == "vowel":
        text += PopVowel()
    else:
        text += PopConsonant()
print(text)

