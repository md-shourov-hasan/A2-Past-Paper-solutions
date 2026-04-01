class EventItem:
    def __init__(self, PEventName, PType, PDifficulty):
        self.__EventName = PEventName  # string
        self.__Type = PType  # string
        self.__Difficulty = PDifficulty  # integer

    def GetName(self):
        return self.__EventName

    def GetDifficulty(self):
        return self.__Difficulty

    def GetEventType(self):
        return self.__Type


class Character:
    def __init__(self, PCharacterName, PJump, PSwim, PRun, PDrive):
        self.__CharacterName = PCharacterName  # string
        self.__Jump = PJump  # integer
        self.__Swim = PSwim  # integer
        self.__Run = PRun  # integer
        self.__Drive = PDrive  # integer

    def GetName(self):
        return self.__CharacterName

    def CalculateScore(self, PType, PDifficulty):
        if PType == "jump":
            EventSkill = self.__Jump
        elif PType == "swim":
            EventSkill = self.__Swim
        elif PType == "run":
            EventSkill = self.__Run
        elif PType == "drive":
            EventSkill = self.__Drive

        if EventSkill >= PDifficulty:
            return 100
        else:
            difference = PDifficulty - EventSkill
            if difference == 1:
                return 80
            elif difference == 2:
                return 60
            elif difference == 3:
                return 40
            elif difference == 4:
                return 20


# main program
Group = []

Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))

Tarz = Character("Tarz", 5, 3, 5, 1)
Geni = Character("Geni", 2, 2, 3, 4)

# score calculation

Tarz_Score = 0
Geni_Score = 0

for i in range(5):
    Event = Group[i]
    Tarz_Chance = Tarz.CalculateScore(Event.GetEventType(), Event.GetDifficulty())
    Geni_Chance = Geni.CalculateScore(Event.GetEventType(), Event.GetDifficulty())

    if Tarz_Chance > Geni_Chance:
        Tarz_Score += 1
        print(Tarz.GetName(), " have won the event: ", Event.GetName())
    elif Tarz_Chance < Geni_Chance:
        Geni_Score += 1
        print(Geni.GetName(), " have won the event: ", Event.GetName())
    else:
        print("The event: ", Event.GetName(), " is a draw")

if Tarz_Score > Geni_Score:
    print(Tarz.GetName(), " have won with ", Tarz_Score, " points")
elif Tarz_Score < Geni_Score:
    print(Geni.GetName(), " have won with ", Geni_Score, " points")
else:
    print("The group is a draw")
