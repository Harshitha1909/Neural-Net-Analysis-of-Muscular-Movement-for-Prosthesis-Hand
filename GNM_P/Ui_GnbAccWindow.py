from PyQt5 import QtCore, QtGui, QtWidgets
from GnbAccWindow import *
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1134, 621)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 100, 241, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(85, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(300, 370, 521, 91))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect the button click event to the custom function
        self.pushButton.clicked.connect(self.perform_calculations)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Calculate "))

    def perform_calculations(self):
        try:
            # Your import and calculation code here
            import numpy as np
            import pandas as pd
            from sklearn.naive_bayes import GaussianNB
            from sklearn.metrics import accuracy_score

            df = pd.read_csv('exmeasureset.csv')
            data = df[["XMovement", "YMovement", "ZMovement", "AngClckMovemnt", "AngAnticlckMovemnt", "OMI"]].to_numpy()
            inputs = data[:, :-1]
            outputs = data[:, -1]
            training_inputs = inputs[:1000]
            training_outputs = outputs[:1000]
            testing_inputs = inputs[1000:]
            testing_outputs = outputs[1000:]
            df = pd.DataFrame(data=testing_outputs)
            testing_outputs = df.to_numpy()
            classifier = GaussianNB()
            classifier.fit(training_inputs, training_outputs)
            predictions = classifier.predict(testing_inputs)
            accuracy = 100.0 * accuracy_score(testing_outputs, predictions)

            # Display the result in the QTextEdit
            result_text = f"The accuracy of Gaussian NaiveBayes Classifier on testing data is: {accuracy:.2f}%"
            self.textEdit.setPlainText(result_text)

        except Exception as e:
            # Handle exceptions, e.g., if the file is not found or the data format is incorrect
            error_text = f"Error: {str(e)}"
            self.textEdit.setPlainText(error_text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
