class Vehicle:
    def __init__(self, PID, PMax, PIncreaseAmount):
        self.__ID = PID # string
        self.__MaxSpeed = PMax # integer
        self.__IncreaseAmount = PIncreaseAmount # integer
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def SetCurrentSpeed(self, Value):
        self.__CurrentSpeed = Value
    def SetHorizontalPosition(self, Value):
        self.__HorizontalPosition = Value

    def IncreaseSpeed(self):
        self.__CurrentSpeed += self.__IncreaseAmount

        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition += self.__CurrentSpeed


class Helicopter(Vehicle):
    def __init__(self, PID, PMax, PIncreaseAmount, PVChange, PMaxHeight):
        super().__init__(PID, PMax, PIncreaseAmount)
        self.__VerticalPosition = 0 #integer
        self.__VerticalChange = PVChange # integer
        self.__MaxHeight = PMaxHeight # integer

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange

        if self.__VerticalPosition > self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight

        updatedSpeed = self.GetCurrentSpeed() + self.GetIncreaseAmount()

        if updatedSpeed > self.GetMaxSpeed():
            updatedSpeed = self.GetMaxSpeed()

        updatedHorizontalPosition = self.GetHorizontalPosition() + updatedSpeed
        self.SetCurrentSpeed(updatedSpeed)
        self.SetHorizontalPosition(updatedHorizontalPosition)

def OutputDetails(Data):
    try:
        verticalPosition = Data.GetVerticalPosition()
        print(f"The horizontal position is: {Data.GetHorizontalPosition()}")
        print(f"The speed of the vehicle is: {Data.GetCurrentSpeed()}")
        print(f"The vertical position is: {verticalPosition}")

    except:
        print(f"The horizontal position is: {Data.GetHorizontalPosition()}")
        print(f"The speed of the vehicle is: {Data.GetCurrentSpeed()}")

#main program
Car1 = Vehicle("Tiger", 100, 20)
Hel1 = Helicopter("Lion", 350, 40, 3, 100)

Car1.IncreaseSpeed()
Car1.IncreaseSpeed()
OutputDetails(Car1)

Hel1.IncreaseSpeed()
Hel1.IncreaseSpeed()
OutputDetails(Hel1)