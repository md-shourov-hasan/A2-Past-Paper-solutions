class Character:
    def __init__(self, PName, PDOB, PIntl, PSpeed):
        self.__CharacterName = PName #string
        self.__DateOfBirth = PDOB #string
        self.__Intelligence = PIntl #real
        self.__Speed = PSpeed #integer

    def GetIntelligence(self):
        return self.__Intelligence
    def GetName(self):
        return self.__CharacterName

    def SetIntelligence(self, value):
        self.__Intelligence = value

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.10

    def ReturnAge(self):
        DOB = self.__DateOfBirth
        DOB = DOB.split(" ")
        BirthYear = DOB[2]

        Age = 2023 - int(BirthYear)
        return Age

class MagicCharacter(Character):
    def __init__(self,PElem,PName,PDob,PIntel,PSpeed):
        super().__init__(PName,PDob,PIntel,PSpeed)
        self.Element = PElem

    def Learn(self):
        intel = self.GetIntelligence()

        if self.Element == "fire" or self.Element == "water":
            intel = intel * 1.20
        elif self.Element == "earth":
            intel = intel * 1.30
        else:
            intel = intel * 1.10

        self.SetIntelligence(intel)


FirstCharacter = Character("Royal","1 January 2019", 70.0, 30)

FirstCharacter.Learn()

print("Name:", FirstCharacter.GetName())
print("Age:",FirstCharacter.ReturnAge())
print("Intelligence:",FirstCharacter.GetIntelligence())

FirstMagic = MagicCharacter("fire","Light", "3 March 2018", 75, 22)

FirstMagic.Learn()
print("Name:", FirstMagic.GetName())
print("Age:",FirstMagic.ReturnAge())
print("Intelligence:",FirstMagic.GetIntelligence())
