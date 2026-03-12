class BoardObject:
    def __init__(self, PCode, PValue):
        self.__Code = PCode  # string
        self.__value = PValue  # integer

    def GetCode(self):
        return self.__Code

    def GetValue(self):
        return self.__value


class Board:
    def __init__(self):
        self.__TheBoard = []  # BoardObject
        for _ in range(10):
            new_row = [BoardObject("-", 0) for _ in range(10)]
            self.__TheBoard.append(new_row)

    def GetObject(self, Row, Column):
        return self.__TheBoard[Row][Column]

    def SetObject(self, Object, Row, Column):
        self.__TheBoard[Row][Column] = Object

    def DisplayBoard(self):

        for rows in range(10):
            line = ""
            for columns in range(10):
                line += self.GetObject(rows, columns).GetCode()
            print(line)


# main program

Object1 = BoardObject("A", 2)
Object2 = BoardObject("B", 3)
Object3 = BoardObject("C", 5)
Object4 = BoardObject("D", 2)
Object5 = BoardObject("E", 7)

NewBoard = Board()
NewBoard.SetObject(Object1, 0, 0)
NewBoard.SetObject(Object2, 9, 9)
NewBoard.SetObject(Object3, 4, 5)
NewBoard.SetObject(Object4, 2, 2)
NewBoard.SetObject(Object5, 8, 7)

NewBoard.DisplayBoard()

Row = int(input("Enter a row number between 0 and 9: "))

while Row < 0 or Row > 9:
    Row = int(input("Try again: "))

Column = int(input("Enter a column number between 0 and 9: "))

while Column < 0 or Column > 9:
    Column = int(input("Try again: "))

returned_object = NewBoard.GetObject(Row, Column)

if returned_object.GetCode() == "-":
    print("Miss")
else:
    print("The code is:", returned_object.GetCode())
    print("The value is:", returned_object.GetValue())
