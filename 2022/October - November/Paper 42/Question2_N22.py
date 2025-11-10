class Character:
    def __init__(self, Name, XCoordinate, YCoordinate):
        self.__Name = Name #String
        self.__XCoordinate = XCoordinate #Integer
        self.__YCoordinate = YCoordinate #Integer

    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange
#to be continued



