import sys
import os
from smp import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.gnb1.clicked.connect(self.gnbacc)
     self.ui.gnb2.clicked.connect(self.gnbpred)
     self.ui.nn1.clicked.connect(self.nnacc)
     self.ui.nn2.clicked.connect(self.nnpred)

  def gnbacc(self):
    os.system("python -W ignore Ui_GnbAccWindow.py")

  def gnbpred(self):
    os.system("python -W ignore Ui_GnbPreWindow.py")

  def nnacc(self):
    os.system("python -W ignore Ui_NnAccWindow.py")

  def nnpred(self):  
    os.system("python -W ignore Ui_NnPreWindow.py")

       
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
