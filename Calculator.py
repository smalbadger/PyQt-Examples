'''
Class:      Calculator
Author(s):  Sam Badger
Date:       January 3, 2018
Description:
            The python adaptation of the example given at:
            http://doc.qt.io/qt-5/qtwidgets-widgets-calculator-example.html
'''

import sys
import Math

from PySide2.QtWidgets import *
from PySide2.QtCore    import *
from PySide2.QtGui     import *

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.sumInMemory = 0.0
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.waitingForOperand = True
        
        self.display = QLineEdit("0")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        
        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)
        
        # ---------- CREATE BUTTONS ---------- #
        digitBtnGrp = QButtonGroup()
        digitBtnGrp.buttonClicked.connect(self._digitClicked)
        digitBtnGrp.setExclusive(True)
        
        digitBtns = []
        for i in range(10):
            btn = self._createButton(i)
            digitBtns.append(btn)
            digitBtnGrp.addButton(btn)
        
        pointBtn =       self._createButton(".",         self._pointClicked)
        changeSignBtn =  self._createButton("\302\261",  self._changeSignClicked)

        backspaceBtn =   self._createButton("Backspace", self._backspaceClicked)
        clearButton =    self._createButton("Clear",     self._clear)
        clearAllButton = self._createButton("Clear All", self._clearAll)
        
        clearMemoryBtn = self._createButton("MC",        self._clearMemory)
        readMemoryBtn =  self._createButton("MR",        self._readMemory)
        setMemoryBtn =   self._createButton("MS",        self._setMemory)
        addToMemoryBtn = self._createButton("M+",        self._addToMemory)
        
        divisionBtn =    self._createButton("\303\267")
        timesBtn =       self._createButton("\303\227")
        multiplicativeBtnGrp = QButtonGroup()
        multiplicativeBtnGrp.setExclusive(True)
        multiplicativeBtnGrp.addButton(divisionBtn)
        multiplicativeBtnGrp.addButton(timesBtn)
        multiplicativeBtnGrp.buttonClicked.connect(self._multiplicativeOperatorClicked)
        
        minusBtn =       self._createButton("-")
        plusBtn =        self._createButton("+")
        additiveBtnGrp = QButtonGroup()
        additiveBtnGrp.setExclusive(True)
        additiveBtnGrp.addButton(divisionBtn)
        additiveBtnGrp.addButton(timesBtn)
        additiveBtnGrp.buttonClicked.connect(self._additiveOperatorClicked)
        
        
        squareRootBtn =  self._createButton("Sqrt")
        powerBtn =       self._createButton("x\302\262")
        reciprocalBtn =  self._createButton("1/x")
        unaryBtnGrp = QButtonGroup()
        unaryBtnGrp.setExclusive(True)
        unaryBtnGrp.addButton(squareRootBtn)
        unaryBtnGrp.addButton(powerBtn)
        unaryBtnGrp.addButton(reciprocalBtn)
        unaryBtnGrp.buttonClicked.connect(self._unaryOperatorClicked)
        
        equalBtn =       self._createButton("=",         self._equalClicked)
        
        # ---------- CREATE LAYOUT ---------- #
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addWidget(self.display, 0, 0, 1, 6)
        mainLayout.addWidget(backspaceBtn, 1, 0, 1, 2)
        mainLayout.addWidget(clearBtn, 1, 2, 1, 2)
        mainLayout.addWidget(clearAllBtn, 1, 4, 1, 2)
        
        mainLayout.addWidget(clearMemoryBtn, 2, 0)
        mainLayout.addWidget(readMemoryBtn, 3, 0)
        mainLayout.addWidget(setMemoryBtn, 4, 0)
        mainLayout.addWidget(addToMemoryBtn, 5, 0)
        
        for i in range(1, 10):
            row = ((9-i) / 3) + 2
            col = ((i-1) % 3) + 1
            mainLayout.addWidget(digitBtns[i], row, col)
        
        mainLayout.addWidget(digitBtns[0], 5, 1)
        mainLayout.addWidget(pointBtn, 5, 2)
        mainLayout.addWidget(changeSignBtn, 5, 3)
        mainLayout.addWidget(divisionBtn, 2, 4)
        mainLayout.addWidget(timesBtn, 3, 4)
        mainLayout.addWidget(minusBtn, 4, 4)
        mainLayout.addWidget(plusBtn, 5, 4)
        mainLayout.addWidget(squareRootBn, 2, 5)
        mainLayout.addWidget(powerBtn, 3, 5)
        mainLayout.addWidget(reciprocalBtn, 4, 5)
        mainLayout.addWidget(equalBtn, 5, 5)
        
        self.setLayout(mainLayout)
        self.setWindowTitle("Calculator")
        
    def _createButton(self, text, member=None):
        button = QPushButton(str(text))
        if member != None:
            button.clicked.connect(member)
        return button
        
    def _abortOperation(self):
        pass
        
    def _calculate(self, rightOperand, pendingOperator):
        pass
    
    # ---------- PRIVATE SLOTS ---------- #
    def _digitClicked(self, digitBtn):
        digitValue = int(digitBtn.text())
        
        if self.display.text() != "0" and digitValue == 0:
            return
            
        if self.waitingForOperand:
            self.display._clear()
            self.waitingForOperand = False
            
        self.display.setText(self.display.text() + str(digitValue))
        
    def _unaryOperatorClicked(self, operatorBtn):
        clickedOperator = operatorBtn.text()
        operand = float(self.display.text())
        result = 0
        
        if clickedOperator = "Sqrt":
            if operand < 0:
                abortOperation()
                return
            result = Math.sqrt(operand)
            
        elif clickedOperator == "x\302\262":
            result = operand**2
            
        elif clickedOperator == "1/x"
            if operand == 0:
                abortOperation()
                return
            result = 1/operand
            
        self.display.setText(str(result))
        waitingForOperand = True
        
    def _additiveOperatorClicked(self, operatorBtn):
        clickedOperator = operatorBtn.text()
        operand = float(self.display.text())
        result = 0
        
        if not pendingMultiplicativeOperator.isEmpty():
            if not calculate(operand, pendingMultiplicativeOperator):
                abortOperation()
                return
            display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0
            pendingMultiplicativeOperator.clear()
            
        if not pendingAdditiveOperator.isEmpty():
            if not calculate(operand, pendingAdditiveOperator):
                abortOperation()
                return
            self.display.setText(self.sumSoFar)
        else:
            self.sumSoFar = operand
            
        pendingAdditiveOperator = clickedOperator
        waitingForOperand = True
        
    def _multiplicativeOperatorClicked(self, operatorBtn):
        pass
        
    def _equalClicked(self):
        pass
        
    def _pointClicked(self):
        pass
        
    def _changeSignClicked(self):
        pass
        
    def _backspaceClicked(self):
        pass
        
    def _clear(self):
        pass
        
    def _clearAll(self):
        pass
        
    def _clearMemory(self):
        pass
        
    def _readMemory(self):
        pass
        
    def _setMemory(self):
        pass
        
    def _addToMemory(self):
        pass
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    widget = Calculator()
    widget.show()
    
    sys.exit(app.exec_())  
