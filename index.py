from PyQt5 import QtWidgets
from main import Ui_MainWindow
from db import Database
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.db = Database('db/list.dat')
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
    def btnClicked(self):
        print(self.ui.lineEdit.text())

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())