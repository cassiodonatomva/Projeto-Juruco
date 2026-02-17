import sys
import os
# Importamos o que é necessário de cada módulo específico
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt6.QtCore import Qt

# Tentativa de importar a interface. 
# Se o seu arquivo ainda se chamar 'untitled.py', troque 'login' por 'untitled'
try:
    from login import Ui_Login
except ModuleNotFoundError:
    # Caso você ainda não tenha renomeado o arquivo gerado pelo Qt Designer
    from untitled import Ui_Login
    from Principal import Ui_MainWindow


class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        





class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.login)    

    def login(self):
        admin = "admin"
        senha = "admin"
        User = ""
        passD = ""
        User = self.ui.lineEdit.text()
        passD = self.ui.lineEdit_2.text()
        if User == admin and passD == senha:
            QMessageBox.information(self, "Login realizado", "Nao deu certo")
            self.window = Principal()
            self.window.show()
            self.accept()
        else:
            QMessageBox.information(self, "login Errado", "Nao entou com sucesso")
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Criamos a janela
    window = Login()
    window.show()
    
    # Em PyQt6, usamos exec() sem o underline final
    sys.exit(app.exec())