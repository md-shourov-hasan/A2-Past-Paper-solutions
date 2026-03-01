class Train:
    def __init__(self, PTrainIDNumber, PRoute):
        self.__TrainIDNumber = PTrainIDNumber  # string
        self.__Route = PRoute  # integer

    def GetTrainIDNumber(self):
        return self.__TrainIDNumber

    def GetRoute(self):
        return self.__Route


class Station:
    def __init__(self, PStationID, PNumberPlatforms):
        self.__StationID = PStationID  # string
        self.__NumberPlatforms = PNumberPlatforms  # integer
        self.__Trains = []  # Train, stores upto 10 elements
        self.__NumberTrains = 0  # integer

    def AddTrain(self, PTrain):
        if self.__NumberPlatforms >= self.__NumberTrains:
            return False
        self.__Trains.append(PTrain)
        self.__NumberTrains += 1

        return True

    def GetTrains(self):
        if self.__NumberTrains == 0:
            return "There are no trains"
        text = "The trains at station " + self.__StationID + " are:" + "\n"
        for i in range(self.__NumberTrains):
            text = text + self.__Trains[i].GetTrainIDNumber() + " on route number " + str(
                self.__Trains[i].GetRoute()) + "\n"

        return text


Train1 = Train("12ADV", 134)
Train2 = Train("33ART", 20)
Train3 = Train("9FKF", 3)
Train4 = Train("21VBC", 24)

Station1 = Station("STH", 2)
Station2 = Station("NTH", 1)

isAdded = Station1.AddTrain(Train1)
if not isAdded:
    print("Station is full")

isAdded = Station1.AddTrain(Train2)
if not isAdded:
    print("Station is full")

isAdded = Station1.AddTrain(Train3)
if not isAdded:
    print("Station is full")

isAdded = Station2.AddTrain(Train4)
if not isAdded:
    print("Station is full")

print(Station1.GetTrains())
print(Station2.GetTrains())
