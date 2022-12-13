from types import *
from math import *

class Summator:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b
        print("A = ", a, "B = ", b)
        self.setValueOperator()
        self.setMainComponents()
        self.transferToBin()
        self.setCodeValues()
    
    def getValueA(self) -> int:
        return self.a
    
    def getValueB(self) -> int:
        return self.b
    
    def setValueOperator(self) -> None:
        if (self.getValueA() > 0 and self.getValueB() < 0)\
             or (self.getValueA() < 0 and self.getValueB() > 0):
             self.operator = 1
        else:
            self.operator = 0
        print("C(operator) = ", self.operator)
    
    def getValueOperator(self) -> int:
        return self.operator

    def setMainComponents(self) -> None:
        if self.getValueOperator() == 1:
            self.mainValue = self.getValueA() if self.getValueA() > 0 else self.getValueB()
            self.sideValue = self.getValueA() if self.getValueA() < 0 else self.getValueB()
        else:
            self.mainValue = self.getValueA()
            self.sideValue = self.getValueB()
    
    def getMainValue(self) -> int:
        return self.mainValue
    
    def getSideValue(self) -> int:
        return self.sideValue
    
    def transferToBin(self) -> None:
        a = bin(abs(self.getMainValue()))[2:]
        b = bin(abs(self.getSideValue()))[2:]

        mant = max(len(a), len(b))

        self.mant = mant
        
        self.mainBin = "0"*(mant-len(a)) + a
        self.sideBin = "0"*(mant-len(b)) + b
        print("A(2) = ", self.mainBin, "B(2) = ", self.sideBin)

    def transferToCode(self, value: int, directCode: str) -> str:
        if value > 0:
            return directCode
        else:
            reverseCode = self.transferToReverse(directCode)
            return self.addValue(reverseCode, "0"*(len(reverseCode) - 1) + "1")
    
    def setCodeValues(self) -> None:
        if self.getValueOperator() == 0 and self.getMainValue() < 0:
            self.mainCode = self.transferToCode(abs(self.getMainValue()), self.mainBin)
            self.sideCode = self.transferToCode(abs(self.getSideValue()), self.sideBin)
            self.mainOperator = 0
            self.sideOperator = 0
        else:
            self.mainCode = self.transferToCode(self.getMainValue(), self.mainBin)
            self.sideCode = self.transferToCode(self.getSideValue(), self.sideBin)
            self.mainOperator = 0 if self.getMainValue() > 0 else 1
            self.sideOperator = 0 if self.getSideValue() > 0 else 1
        
        print("A(dop.code) = ", self.mainCode, "B(dop.code) = ", self.sideCode)
    
    def getMainCode(self) -> str:
        return self.mainCode
    
    def getSideCode(self) -> str:
        return self.sideCode
    
    def addValue(self, first: str, second: str) -> str:
        if len(first) != len(second):
            return ""
        else:
            string = ""
            ost = 0
            for i in range(len(first) - 1, -1, -1):
                value = int(first[i]) + int(second[i]) + ost
                if value == 0:
                    string = "0" + string
                    ost = 0
                elif value == 1:
                    string = "1" + string
                    ost = 0
                elif value == 2:
                    string = "0" + string
                    ost = 1
                elif value == 3:
                    string = "1" + string
                    ost = 1
            return string

    def transferToReverse(self, value: str) -> str:
        string = ""
        for i in range(len(value)):
            string += "1" if value[i] == "0" else "0"
        return string
    
    def getMainOperator(self) -> int:
        return self.mainOperator
    
    def getSideOperator(self) -> int:
        return self.sideOperator
    
    def getMant(self) -> int:
        return self.mant

    def shiftValue(self, value: str, operator: int) -> str:
        string = ""
        string += str(operator)
        for i in range(0, len(value) - 1):
            string += value[i]
        
        return string
    
    def deplyValues(self) -> str:
        C = "00" + "0"*(self.mant*2)
        print("C = 2*n bits = ", self.mant * 2)
        print("Deply Operation: ")
        print(C)
        C = self.addValue(C, "00" + "0" * self.getMant() + self.getSideCode())
        print(C + "\t"*10 + "C = C + B(dop)")
        for i in range(self.getMant()):
            el = C[-1]
            if el == '1':
                C = self.addValue(C, "00" + self.getMainCode() + "0"*self.getMant())
                print("+")
                print("00" + self.getMainCode() + "0"*self.getMant())
                print("_"*(len(C)))
                print(C + "\t"*10 + "C = C + A(dop)")
            C = self.shiftValue(C, self.getValueOperator())
            print(C + "\t"*10 + "C ->")
        return C
    
    def __str__(self):
        return self.deplyValues()