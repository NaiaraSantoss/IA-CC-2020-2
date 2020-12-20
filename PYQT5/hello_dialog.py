from PyQt5.QtWidgets import QLineEdit, QPushButton, QApplication,\
    QVBoxLayout, QDialog



class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.edit = QLineEdit("Escreva seu nome aqui!")
        self.button = QPushButton("Mostrar Cumprimentos")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print("Hello %s" % self.edit.text())


if __name__ == '__main__':
    app = QApplication([])

    form = Form()
    form.show()

    app.exec_()