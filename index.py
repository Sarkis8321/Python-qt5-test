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
        print(self.db.readDbNameList(self.db.readDb()))
    def btnClicked(self):
        if ((self.ui.lineEdit.text().strip() != '') and (self.ui.textEdit.toPlainText().strip())):
            try:
                with open('db/list.dat', 'r') as ff:
                    nums = ff.read().splitlines()
                ff.close()
                with open('db/list.dat', 'a') as ff:
                    ff.write(str(int(nums[-1])+1) + '\n')
                ff.close()
                with open('db/list/'+str(int(nums[-1])+1)+'.txt','w') as ff:
                    ff.write(self.ui.lineEdit.text().strip()+'\n')
                    ff.write(self.ui.textEdit.toPlainText().strip())
                ff.close()
            except Exception:
                print('ошибка подключения к базе данных')
            else: 
                print('данные успешно добавлены')
            

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())