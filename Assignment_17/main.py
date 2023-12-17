from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from functools import partial

def append_number(number):
    global first_number
    if window.text.text() == "0":
        window.text.setText("")

    current_text = window.text.text()
    first_number = current_text + number
    window.text.setText(first_number)

def sum(opr):
    global first_number, operation
    first_number = window.text.text()
    window.text.setText("0")
    operation = opr

def sub(opr):
    global first_number, operation
    first_number = window.text.text()
    window.text.setText("0")
    operation = opr

def mul(opr):
    global first_number, operation
    first_number = window.text.text()
    window.text.setText("0")
    operation = opr

def divide(opr):
    global first_number, operation
    first_number = window.text.text()
    window.text.setText("0")
    operation = opr

def equal():
    global first_number, second_number, operation
    current_text = window.text.text()
    second_number = current_text + first_number
    window.text.setText(second_number)
    if operation == "+":
        result = str(float(first_number) + float(second_number))
        window.text.setText(result)
    elif operation == "-":
        result = str(float(first_number) - float(second_number))
        window.text.setText(result)
    elif operation == "x":
        result = str(float(first_number) * float(second_number))
        window.text.setText(result)
    elif operation == "/":
        result = str(float(first_number) / float(second_number))
        window.text.setText(result)

def clear():
    window.text.setText("0")

app = QApplication([])

loader = QUiLoader()
window = loader.load("Assignment_17\main_window.ui")
window.show()

window.btn_number0.clicked.connect(partial(append_number, "0"))
window.btn_number1.clicked.connect(partial(append_number, "1"))
window.btn_number2.clicked.connect(partial(append_number, "2"))
window.btn_number3.clicked.connect(partial(append_number, "3"))
window.btn_number4.clicked.connect(partial(append_number, "4"))
window.btn_number5.clicked.connect(partial(append_number, "5"))
window.btn_number6.clicked.connect(partial(append_number, "6"))
window.btn_number7.clicked.connect(partial(append_number, "7"))
window.btn_number8.clicked.connect(partial(append_number, "8"))
window.btn_number9.clicked.connect(partial(append_number, "9"))
window.btn_dot.clicked.connect(partial(append_number, "."))

window.btn_sum.clicked.connect(partial(sum, "+"))
window.btn_sub.clicked.connect(partial(sub, "-"))
window.btn_multiple.clicked.connect(partial(mul, "x"))
window.btn_divide.clicked.connect(partial(divide, "/"))
window.btn_result.clicked.connect(equal)
window.btn_clear.clicked.connect(clear)

app.exec()
