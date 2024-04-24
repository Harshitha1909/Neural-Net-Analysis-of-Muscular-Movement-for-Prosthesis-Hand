# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GnbPreWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1125, 706)
        Dialog.setStyleSheet("color: rgb(0, 170, 0);\n"
"hover\n"
"{background-color: rgb(0, 170, 0)};\n"
"hover\n"
"{color: rgb(255, 255, 255)};")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(210, 30, 681, 171))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(230, 260, 641, 111))
        self.textEdit.setStyleSheet("color: rgb(0, 170, 0);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 410, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton:hover:enabled { color: white }\n"
"QPushButton:hover:enabled {background-color: rgb(0, 170, 0)}\n"
"QPushButton:enabled { color: rgb(0, 170, 0)}")
        self.pushButton.setObjectName("pushButton")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 550, 651, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setText(_translate("Dialog", "  Enter the 5 values of directions"))
        self.pushButton.setText(_translate("Dialog", "Predict"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
