class Animal:
    def __init__(self, PName, PSound, PSize, PIntelligence):
        self.Name = PName  # string
        self.Sound = PSound  # string
        self.Size = PSize  # integer
        self.Intelligence = PIntelligence  # integer

    def Description(self):
        return "The animal's name is " + self.Name + ", it makes a " + self.Sound + ", its size is " + str(
            self.Size) + " and its intelligence level is " + str(self.Intelligence)


class Parrot(Animal):
    def __init__(self, PName, PSound, PSize, PIntelligence, PWingSpan, PNumberWords):
        super().__init__(PName, PSound, PSize, PIntelligence)
        self.WingSpan = PWingSpan  # integer
        self.NumberWords = PNumberWords  # integer

    def ChangeNumberWords(self, number):
        self.NumberWords += number

    def Description(self):
        return "The animal's name is " + self.Name + ", it makes a " + self.Sound + ", its size is " + str(
            self.Size) + " and its intelligence level is " + str(self.Intelligence) + ". It has a wingspan of " + str(
            self.WingSpan) + "cm and can say " + str(self.NumberWords) + " words."


class Wolf(Animal):
    def __init__(self, PName, PSound, PSize, PIntelligence, PTerritorySize):
        super().__init__(PName, PSound, PSize, PIntelligence)
        self.TerritorySize = PTerritorySize  # integer

    def SetTerritorySize(self, number):
        self.TerritorySize += number

    def Description(self):
        return "The animal's name is " + self.Name + ", it makes a " + self.Sound + ", its size is " + str(
            self.Size) + " and its intelligence level is " + str(self.Intelligence) + ". Its territory is " + str(
            self.TerritorySize) + " square miles."


Animal1 = Parrot("Chewie", "Squawk", 1, 10, 30, 29)
Animal2 = Wolf("Nighteyes", "Howl", 8, 7, 100)
Animal3 = Animal("Copper", "Neigh", 10, 6)

Animal2.SetTerritorySize(-20)
Animal1.ChangeNumberWords(2)

print(Animal1.Description())
print(Animal2.Description())
print(Animal3.Description())
