# Importing necessary libraries
import numpy as np
import pandas as pd
import tensorflow as tf
from PyQt5.QtWidgets import QApplication, QDialog, QTextEdit, QPushButton

# Importing NnPreWindow without modifying it
from NnPreWindow import Ui_Dialog as NnPreWindow

# Read the dataset into a dataframe
df = pd.read_csv('exmeasureset.csv')

# Creation of data as numpy array
data = df[["XMovement", "YMovement", "ZMovement", "AngClckMovemnt", "AngAnticlckMovemnt", "OMI"]].to_numpy()

# All columns except the last column are considered as inputs
inputs = data[:, :-1]

# Last Column is considered as outputs
outputs = data[:, -1]

# First Thousand rows are considered for training
training_data = inputs[:1000]

# Training labels are set to the last column values of the first thousand rows
training_labels = outputs[:1000]

# Remaining Rows, Beyond 1000 are considered for testing
test_data = inputs[1000:]

# Testing labels are set to the last column values of remaining rows
test_labels = outputs[1000:]

# Tensorflow Initiation
tf.keras.backend.clear_session()

# Configure the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=tf.nn.tanh),
    tf.keras.layers.Dense(64, activation=tf.nn.elu),
    tf.keras.layers.Dense(32, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softplus)
])

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Create the application and dialog
app = QApplication([])

# Initialize NnPreWindow dialog
dialog = QDialog()
ui = NnPreWindow()
ui.setupUi(dialog)

# Get references to required widgets
text_edit_input = ui.textEdit
text_edit_output = ui.textEdit_2
push_button_predict = ui.pushButton

# Function to perform predictions based on the input test set
def predict_and_display():
    # Get the test set input from the textEdit widget
    test_input_text = text_edit_input.toPlainText()
    test_set = [list(map(float, test_input_text.split(',')))]

    # Convert the test set to a Pandas DataFrame
    test_df = pd.DataFrame(test_set)

    # Perform prediction on the test set using the model
    predictions = model.predict(test_df)

    # Find the test set label
    classes = np.argmax(predictions, axis=1)

    # Display the prediction in the last textEdit widget
    output_text = f'Neural Net  Prediction on the test set is: {classes}'
    text_edit_output.setPlainText(output_text)

# Connect the button click event to the predict_and_display function
push_button_predict.clicked.connect(predict_and_display)

# Show the dialog
dialog.show()
app.exec_()
