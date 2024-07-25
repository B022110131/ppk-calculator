import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel, QMenuBar, QAction, QMessageBox
from PyQt5.QtCore import Qt

class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PPK Technology Scientific Calculator")
        self.setGeometry(100, 100, 420, 650)
        self.setStyleSheet("background-color: white;")
        
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        self.txtDisplay = QLineEdit(self)
        self.txtDisplay.setFixedHeight(50)
        self.txtDisplay.setStyleSheet("font-size: 15px; font-weight: bold; color: lightyellow; background-color: black;")
        self.txtDisplay.setAlignment(Qt.AlignRight)
        self.txtDisplay.setText("0")
        mainLayout.addWidget(self.txtDisplay)

        gridLayout = QGridLayout()
        mainLayout.addLayout(gridLayout)

        numberpad = "7894561230"
        positions = [(i, j) for i in range(4, 8) for j in range(3)]

        for position, num in zip(positions, numberpad):
            button = QPushButton(num, self)
            button.setFixedSize(70, 70)
            button.setStyleSheet("font-size: 15px; font-weight: bold; color: black; background-color: lightyellow; border-radius: 10px;")
            button.clicked.connect(lambda _, x=num: self.numberEnter(x))
            gridLayout.addWidget(button, *position)

        btnClear = QPushButton('C', self)
        btnClear.setFixedSize(70, 70)
        btnClear.setStyleSheet("font-size: 15px; font-weight: bold; background-color: orangered; border-radius: 10px;")
        btnClear.clicked.connect(self.Clear_Entry)
        gridLayout.addWidget(btnClear, 4, 3)

        btnAllClear = QPushButton('CE', self)
        btnAllClear.setFixedSize(70, 70)
        btnAllClear.setStyleSheet("font-size: 15px; font-weight: bold; background-color: orangered; border-radius: 10px;")
        btnAllClear.clicked.connect(self.All_Clear_Entry)
        gridLayout.addWidget(btnAllClear, 4, 4)

        btnsq = QPushButton('√', self)
        btnsq.setFixedSize(70, 70)
        btnsq.setStyleSheet("font-size: 15px; font-weight: bold; background-color: honeydew; border-radius: 10px;")
        btnsq.clicked.connect(self.squared)
        gridLayout.addWidget(btnsq, 7, 3)

        btnAdd = QPushButton('+', self)
        btnAdd.setFixedSize(70, 70)
        btnAdd.setStyleSheet("font-size: 15px; font-weight: bold; background-color: honeydew; border-radius: 10px;")
        btnAdd.clicked.connect(lambda: self.operation("add"))
        gridLayout.addWidget(btnAdd, 6, 3)

        # Rest of the buttons
        operations = [
            ('-', 6, 4, lambda: self.operation("sub")),
            ('×', 5, 3, lambda: self.operation("multi")),
            ('÷', 5, 4, lambda: self.operation("divide")),
            #('0', 8, 0, lambda: self.numberEnter(0)),
            ('.', 7, 1, lambda: self.numberEnter('.')),
            ('±', 7, 2, self.mathPM),
            ('=', 7, 4, self.sum_of_total)
        ]

        for (text, row, col, func) in operations:
            button = QPushButton(text, self)
            button.setFixedSize(70, 70)
            button.setStyleSheet("font-size: 15px; font-weight: bold; background-color: honeydew; border-radius: 10px;")
            button.clicked.connect(func)
            gridLayout.addWidget(button, row, col)

        # Scientific buttons
        scientific_buttons = [
            ('π', 1, 0, self.pi), ('cos', 2, 2, self.cos), ('tan', 2, 4, self.tan), ('sin', 2, 3, self.sin),
            ('cosh', 1, 2, self.cosh), ('tanh', 1, 4, self.tanh), ('sinh', 1, 3, self.sinh),
            ('eˣ', 3, 1, self.exp), ('Mod', 3, 4, lambda: self.operation("mod")), ('e', 3, 2, self.e),
            ('log₁₀', 1, 1, self.log10), ('ln(1+x)', 2, 0, self.log1p), ('eˣ⁻¹', 3, 0, self.expm1),
            ('log₂', 2, 1, self.log2), ('deg', 3, 3, self.degrees)
        ]

        for (text, row, col, func) in scientific_buttons:
            button = QPushButton(text, self)
            button.setFixedSize(70, 70)
            button.setStyleSheet("font-size: 15px; font-weight: bold; color: black; background-color: honeydew; border-radius: 10px;")
            button.clicked.connect(func)
            gridLayout.addWidget(button, row, col)

        lblDisplay = QLabel("PPK Technology Scientific Calculator", self)
        lblDisplay.setStyleSheet("font-size: 14px; font-weight: bold; color: black;")
        lblDisplay.setAlignment(Qt.AlignCenter)
        gridLayout.addWidget(lblDisplay, 0, 0, 1, 5)

    def numberEnter(self, num):
        self.result = False
        firstnum = self.txtDisplay.text()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(self.txtDisplay.text())

    def display(self, value):
        self.txtDisplay.setText(str(value))

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(self.txtDisplay.text()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(self.txtDisplay.text()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(self.txtDisplay.text())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(self.txtDisplay.text())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(self.txtDisplay.text())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(self.txtDisplay.text())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(self.txtDisplay.text())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(self.txtDisplay.text())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(self.txtDisplay.text()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(self.txtDisplay.text()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(self.txtDisplay.text()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(self.txtDisplay.text()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(self.txtDisplay.text()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(self.txtDisplay.text()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(self.txtDisplay.text()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(self.txtDisplay.text()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(self.txtDisplay.text()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(self.txtDisplay.text()))
        self.display(self.current)

    def iExit(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    calc = Calc()
    calc.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

#End code Adha