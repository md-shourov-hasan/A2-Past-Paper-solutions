Animal = []  # stores upto 20 elements
Colour = []  # stores upto 10 elements
global AnimalTopPointer
global ColourTopPointer

AnimalTopPointer = 0
ColourTopPointer = 0


def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer += 1
        return True


def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData


def ReadData():
    global AnimalTopPointer
    global ColourTopPointer
    try:
        AnimalFile = open("AnimalData.txt", "r")
        for line in AnimalFile:
            Animal.append(line.strip())
            AnimalTopPointer += 1
        AnimalFile.close()

    except IOError:
        print("Can't locate the file!")

    try:
        ColourFile = open("ColourData.txt", "r")
        for line in ColourFile:
            Colour.append(line.strip())
            ColourTopPointer += 1
        ColourFile.close()

    except IOError:
        print("Can't locate the file!")


def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer += 1
        return True


def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData


def OutputItem():
    AnimalData = PopAnimal()
    ColourData = PopColour()
    if AnimalData != "" and ColourData != "":

        print(ColourData, AnimalData)

    elif ColourData == "" :

        PushAnimal(AnimalData)
        print("No colour")

    elif AnimalData == "":

        PushColour(ColourData)
        print("No animal")

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()