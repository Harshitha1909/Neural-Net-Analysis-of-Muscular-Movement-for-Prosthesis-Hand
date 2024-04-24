# Importing necessary libraries
from PyQt5 import QtWidgets
import sys
import pandas as pd
from sklearn.naive_bayes import GaussianNB

# Importing the generated UI code
from GnbPreWindow import *

class GnbPreWindowApp(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(GnbPreWindowApp, self).__init__()
        self.setupUi(self)

        # Importing dataset and training the model
        df = pd.read_csv('exmeasureset.csv')
        data = df[["XMovement", "YMovement", "ZMovement", "AngClckMovemnt", "AngAnticlckMovemnt", "OMI"]].to_numpy()
        inputs = data[:, :-1]
        outputs = data[:, -1]
        training_inputs = inputs[:1000]
        training_outputs = outputs[:1000]

        self.classifier = GaussianNB()
        self.classifier.fit(training_inputs, training_outputs)

        # Connect the button click event to the prediction logic
        self.pushButton.clicked.connect(self.predict_and_display)

    def predict_and_display(self):
        # Get user input from the lineEdit widget
        user_input_text = self.textEdit.toPlainText()

        # Convert the user input to a list of float values (excluding empty strings)
        num_str = user_input_text.split(',')
        user_input_values = [float(num) for num in num_str]
        # Perform predictions using the trained model
        testSet = [user_input_values]
        test = pd.DataFrame(testSet)
        predictions = self.classifier.predict(test)

        # Display the predictions in the textEdit_2 widget
        result_text = 'GNB Prediction of Exercise Measure Index on the user input is: {}'.format(predictions)
        self.textEdit_2.setPlainText(result_text)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GnbPreWindowApp()
    window.show()
    sys.exit(app.exec_())
