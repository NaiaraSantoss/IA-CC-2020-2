import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QSpinBox, QApplication
#Análise de risco
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton

def dinheiro_pouco():
    if spinBox_1.value() <= 0 or spinBox_1.value() < 30:
        return 1
    elif spinBox_1.value() > 30 and spinBox_1.value() <= 50:
        pouco = (float(abs(50 - spinBox_1.value()) / (50 - 30)))
        return pouco
    elif spinBox_1.value() > 50:
        return 0


def dinheiro_razoavel():
    if spinBox_1.value() <= 30:
        return 0
    elif spinBox_1.value() > 30 and spinBox_1.value() <= 50:
        razoavel =  (float(abs(spinBox_1.value() - 30) / (50 - 30)))
        return razoavel
    elif spinBox_1.value() > 70:
        return 0




def dinheiro_adequado():
    if spinBox_1.value() <= 50:
        return 0
    elif 50 < spinBox_1.value() and spinBox_1.value() <= 70:
        adequado =  1 - (float(abs(spinBox_1.value() - 50) / (70 - 30)))
        return adequado
    elif spinBox_1.value() > 70:
        return 1



def pessoal_insuficiente():
    if spinBox_2.value() <= 30:
        return 1
    elif spinBox_2.value() > 30 and spinBox_2.value()<= 70:
        insuficiente =  (float(abs(70 - spinBox_2.value()) / (70 - 30)))
        return insuficiente
    elif spinBox_2.value() > 70:
        return 1




def pessoal_satisfatorio():
    if spinBox_2.value() <= 30:
        return 1
    elif spinBox_2.value() > 30 and spinBox_2.value() <= 70:
        satisfatorio =  (float(abs(spinBox_2.value() - 30) / (70 - 30)))
        return satisfatorio
    elif spinBox_2.value() > 70:
        return 1
    print("----------------------")




def resultado():
    cog = (((40 + 50 + 60) * (pessoal_insuficiente())) + ((70 + 80 + 90) * (0.75))) / (
            dinheiro_razoavel() + pessoal_insuficiente() + dinheiro_razoavel() + dinheiro_pouco() + pessoal_satisfatorio() + dinheiro_pouco())
    print(cog)

    if cog > 70:
        label_resposta1.setText("Risco Alto: " + str(cog))
        return True

    if cog < 70 and cog > 30:
        label_resposta1.setText("Risco Médio: " + str(cog))
        return True

    if cog <30:
        label_resposta1.setText("Risco Baixo: " + str(cog))
        return True




if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute((QtCore.Qt.AA_ShareOpenGLContexts))
    app = QApplication([])
    window = uic.loadUi("logica__fuzzy.ui")
    label_resposta1 = window.findChild(QLabel, 'label_resposta')
    spinBox_1 = window.findChild(QSpinBox, 'spinBox_1')
    spinBox_2 = window.findChild(QSpinBox, 'spinBox_2')
    calculate_btn = window.findChild(QPushButton, 'pushButton')
    calculate_btn.clicked.connect(resultado)
    window.show()
    sys.exit(app.exec_())

