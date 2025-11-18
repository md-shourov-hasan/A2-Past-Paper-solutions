#Question 1



def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)
    for x in range(LengthString):
        FirstCharacter = Value[0:1]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total += 1
        Value = Value[1:len(Value)]

    return Total

print(IterativeVowels("house"))

def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    FirstCharacter = Value[0:1]
    if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
        Value = Value[1:len(Value)]
        return 1 + RecursiveVowels(Value)
    else:
        return RecursiveVowels(Value[1:len(Value)])

print(RecursiveVowels("imagine"))





