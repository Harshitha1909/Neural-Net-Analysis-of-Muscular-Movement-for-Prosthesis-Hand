# Combined code

# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from PyQt5 import QtCore, QtGui, QtWidgets
from NnAccWindow import *
import tensorflow as tf
from tensorflow.keras import backend as K


# Set random seed for reproducibility
seed_value = 42
np.random.seed(seed_value)
tf.random.set_seed(seed_value)

# Importing Warnings
import warnings
warnings.filterwarnings("ignore")

# Function for getting F1-Score
def get_precision(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2 * (precision * recall) / (precision + recall + K.epsilon())
    return precision

# Function to calculate accuracy
def calculate_accuracy():
    # Read the dataset into a dataframe
    df = pd.read_csv('exmeasureset.csv')

    # Creation of data as numpy array
    data = df[["XMovement", "YMovement", "ZMovement", "AngClckMovemnt", "AngAnticlckMovemnt", "OMI"]].to_numpy()

    # All columns except the last column are considered as inputs
    inputs = data[:, :-1]

    # Last Column is considered as outputs
    outputs = data[:, -1]

    # Normalizing input data
    inputs = (inputs - np.mean(inputs, axis=0)) / np.std(inputs, axis=0)

    # Split the data into training and testing sets
    training_data, test_data, training_labels, test_labels = train_test_split(inputs, outputs, test_size=0.2, random_state=seed_value)

    # Tensorflow Initiation
    tf.keras.backend.clear_session()

    # Configure the model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation=tf.nn.tanh),
        tf.keras.layers.Dense(64, activation=tf.nn.elu),
        tf.keras.layers.Dense(32, activation=tf.nn.relu),
        tf.keras.layers.Dense(10, activation='softmax')  # Use softmax for classification
    ])

    # Compile the model
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Creation of the model
    history = model.fit(training_data, training_labels, epochs=50, validation_split=0.2, verbose=2)

    # Plot training history
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.show()

    # Print Model's Loss and Accuracy on the test set
    accuracy_result = model.evaluate(test_data, test_labels)
    return accuracy_result

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1138, 861)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 60, 291, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:rgb(255, 255, 255);\n"
                                      "background-color:  rgb(0, 170, 0);\n")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(80, 260, 931, 511))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(0, 170, 0);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Neural Net Accuracy"))

        # Connect button click event to the calculate_and_display method
        self.pushButton.clicked.connect(self.calculate_and_display)

    def calculate_and_display(self):
        # Call the calculate_accuracy function
        accuracy_result = calculate_accuracy()

        # Display the result in the textEdit widget
        result_text = f"Model's Loss and Accuracy on the test set are {accuracy_result}"
        self.textEdit.setText(result_text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
