class Employee:
    def __init__(self,PHourlyPay,PEmployeeNumber,PJobTitle):
        self.HourlyPay = PHourlyPay #real
        self.__EmployeeNumber = PEmployeeNumber #string
        self.JobTitle = PJobTitle #string
        self.PayYear2022 = [0.0 for _ in range(52)] #real

    def GetEmployeeNumber(self):
        return self__EmployeeNumber

    def SetPay(self,PWeekNumber,PHoursWorked):
        pay = self.HourlyPay * PHoursWorked
        self.PayYear2022[PWeekNumber-1] = pay

    def GetTotalPay(self):
        total = 0
        for i in range(52):
            total += self.PayYear2022[i]
        return total

class Manager(Employee):
    def __init__(self,PBonusValue,PHourlyPay,PEmployeeNumber,PJobTitle):
        super().__init__(PHourlyPay,PEmployeeNumber,PJobTitle)
        self.BonusValue = PBonusValue #real

    def SetPay(self,PWeekNumber, PHoursWorked):
        PHoursWorked = PHoursWorked + (PHoursWorked * self.BonusValue/100)
        super().SetPay(PWeekNumber, PHoursWorked)


