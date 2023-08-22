import typing
from PyQt5.QtWidgets import QWidget
from regex_processing import simplex_response
from response_check import is_constraint_true, solution_print
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic

target_equation = "1*x1 +2*x2"
constraints = "-3*x1 +2*x2 <= 2\n-1*x1 +2*x2 <= 4\n1*x1 +1*x2<= 5"

simple_constraint = "x1 >= 0\nx2 >= 0"

is_max = True

resp = simplex_response(target_equation, constraints, is_max)

print("response = ", resp)

if is_constraint_true(simple_constraint, target_equation, resp):
    res = solution_print(target_equation, resp)
    print("Solution =", res)
else:
    print("non solution")


class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("simplex.ui", self)
        self.show()

        self.simplex_calcul.clicked.connect(self.calcul_simplex)
        self.reset_button.clicked.connect(self.reset_data)

    def check_but(self):
        if self.max.checked:
            return True
        else:
            return False

    def check_constraint(self, resp):
        if is_constraint_true(self.simple_constraint.toPlainText(), self.obj_function.text(), resp):
            var_res, res = solution_print(target_equation, resp)
            return var_res, res
        else:
            return "non solution"

    def calcul_simplex(self):
        resp = simplex_response(self.obj_function.text(), self.constraints_data.toPlainText(), self.check_but)
        var_resp, final_resp = self.check_constraint(resp)
        self.response.setPlainText(str(var_resp))
        self.response.append(str(final_resp))

    def reset_data(self):
        self.obj_function.clear()
        self.constraints_data.clear()
        self.simple_constraint.clear()


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()