class Employee:
    def __init__(self,PHourlyPay,PEmployeeNumber,PJobTitle):
        self.HourlyPay = PHourlyPay #real
        self.__EmployeeNumber = PEmployeeNumber #string
        self.JobTitle = PJobTitle #string
        self.PayYear2022 = [0.0 for _ in range(52)] #real

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

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
        PHoursWorked = PHoursWorked + (PHoursWorked * (self.BonusValue/100))
        super().SetPay(PWeekNumber, PHoursWorked)


def EnterHours():
    global EmployeeArray

    try:
        file = open("HoursWeek1.txt")

        employnum = file.readline().strip()

        while employnum != "":
            hoursworked = float(file.readline().strip())

            for i in range(8):
                if EmployeeArray[i].GetEmployeeNumber() == employnum:
                    EmployeeArray[i].SetPay(1, hoursworked)
                    break
            employnum = file.readline().strip()

        file.close()
    except IOError:
        print("File not found!")



#main program

EmployeeArray = [None for _ in range(8)] #stores 8 data items of type Employee

try:
    file = open("Employees.txt")

    line1 = file.readline().strip()
    pointer = 0

    while line1 != "":
        line2 = file.readline().strip()
        line3 = file.readline().strip()
        isJob = line3[0].isalpha()

        if isJob:
            EmployeeArray[pointer] = Employee(float(line1), line2, line3)
            pointer += 1
            line1 = file.readline().strip()
        else:
            line4 = file.readline().strip()
            EmployeeArray[pointer] = Manager(float(line3), float(line1), line2, line4)
            pointer += 1
            line1 = file.readline().strip()

    file.close()
except IOError:
    print("File not found!")



EnterHours()
for i in range(8):
    print("Employee number: " + EmployeeArray[i].GetEmployeeNumber() + " Total Pay " + str(EmployeeArray[i].GetTotalPay()))


