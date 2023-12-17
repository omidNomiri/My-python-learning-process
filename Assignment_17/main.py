from functools import partial
from decimal import Decimal
from mpmath import sin,cos,tan,cot,log,sqrt,radians
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

class Calculator:
    def __init__(self):
        self.current_text = "0"
        self.first_number = Decimal("0")
        self.operation = ""

    def append_number(self, number):
        if self.current_text == "0":
            self.current_text = ""

        self.current_text += number
        window.text.setText(self.current_text)

    def set_operation(self, opr):
        self.first_number = Decimal(self.current_text)
        self.current_text = "0"
        window.text.setText(self.current_text)
        self.operation = opr

    def choice_operation(self):
        second_number = Decimal(self.current_text)

        if self.operation == "+":
            result = self.first_number + second_number
        elif self.operation == "-":
            result = self.first_number - second_number
        elif self.operation == "x":
            result = self.first_number * second_number
        elif self.operation == "/":
            if second_number != Decimal("0"):
                result = self.first_number / second_number
            else:
                result = "Error: Division by zero"

        window.text.setText(str(result))

    def append_number_another_window(self, number):
        if more_window.text.text() == "0":
            self.current_text = ""

        self.current_text += number
        more_window.text.setText(self.current_text)

    def set_operation_more_window(self, opr):
        self.first_number = Decimal(self.current_text)
        self.current_text = "0"
        more_window.text.setText(self.current_text)
        self.operation = opr

    def more_Mathematics(self):
        self.first_number = radians.self.first_number
        if self.operation == "sin":
            result = sin(self.first_number)
        elif self.operation == "cos":
            result = cos(self.first_number)
        elif self.operation == "tan":
            result = tan(self.first_number)
        elif self.operation == "cot":
            result = cot(self.first_number)
        elif self.operation == "log":
            result = log(self.first_number)
        elif self.operation == "sqrt":
            result = sqrt(self.first_number)

        more_window.text.setText(result)

    def open_another_window(self):
        window.close()
        more_window.show()

    def open_main_window(self):
        more_window.close()
        window.show()

    def clear(self):
        self.current_text = "0"
        self.first_number = Decimal("0")
        self.operation = ""
        window.text.setText(self.current_text)

app = QApplication([])

loader = QUiLoader()
window = loader.load("Assignment_17/main_window.ui")
more_window = loader.load("Assignment_17/more_window.ui")
window.show()

calculator = Calculator()

window.btn_number0.clicked.connect(partial(calculator.append_number, "0"))
window.btn_number1.clicked.connect(partial(calculator.append_number, "1"))
window.btn_number2.clicked.connect(partial(calculator.append_number, "2"))
window.btn_number3.clicked.connect(partial(calculator.append_number, "3"))
window.btn_number4.clicked.connect(partial(calculator.append_number, "4"))
window.btn_number5.clicked.connect(partial(calculator.append_number, "5"))
window.btn_number6.clicked.connect(partial(calculator.append_number, "6"))
window.btn_number7.clicked.connect(partial(calculator.append_number, "7"))
window.btn_number8.clicked.connect(partial(calculator.append_number, "8"))
window.btn_number9.clicked.connect(partial(calculator.append_number, "9"))
window.btn_dot.clicked.connect(partial(calculator.append_number, "."))

window.btn_sum.clicked.connect(partial(calculator.set_operation, "+"))
window.btn_sub.clicked.connect(partial(calculator.set_operation, "-"))
window.btn_multiple.clicked.connect(partial(calculator.set_operation, "x"))
window.btn_divide.clicked.connect(partial(calculator.set_operation, "/"))
window.btn_result.clicked.connect(calculator.choice_operation)
window.btn_more.clicked.connect(calculator.open_another_window)
window.btn_clear.clicked.connect(calculator.clear)

more_window.btn_number0.clicked.connect(partial(calculator.append_number_another_window, "0"))
more_window.btn_number1.clicked.connect(partial(calculator.append_number_another_window, "1"))
more_window.btn_number2.clicked.connect(partial(calculator.append_number_another_window, "2"))
more_window.btn_number3.clicked.connect(partial(calculator.append_number_another_window, "3"))
more_window.btn_number4.clicked.connect(partial(calculator.append_number_another_window, "4"))
more_window.btn_number5.clicked.connect(partial(calculator.append_number_another_window, "5"))
more_window.btn_number6.clicked.connect(partial(calculator.append_number_another_window, "6"))
more_window.btn_number7.clicked.connect(partial(calculator.append_number_another_window, "7"))
more_window.btn_number8.clicked.connect(partial(calculator.append_number_another_window, "8"))
more_window.btn_number9.clicked.connect(partial(calculator.append_number_another_window, "9"))
more_window.btn_dot.clicked.connect(partial(calculator.append_number_another_window, "."))

more_window.btn_sin.clicked.connect(partial(calculator.set_operation_more_window, "sin"))
more_window.btn_cos.clicked.connect(partial(calculator.set_operation_more_window, "cos"))
more_window.btn_tan.clicked.connect(partial(calculator.set_operation_more_window, "tan"))
more_window.btn_cot.clicked.connect(partial(calculator.set_operation_more_window, "cot"))
more_window.btn_log.clicked.connect(partial(calculator.set_operation_more_window, "log"))
more_window.btn_sqrt.clicked.connect(partial(calculator.set_operation_more_window, "sqrt"))
more_window.btn_less.clicked.connect(calculator.open_main_window)
more_window.btn_clear.clicked.connect(calculator.clear)


app.exec()
