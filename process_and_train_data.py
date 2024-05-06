import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error, mean_absolute_error
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ProcessAndTrainData(QWidget):

    def __init__(self, data_frame):
        super().__init__()

        self.data_frame = data_frame
        self.left = 100
        self.top = 100
        self.width = 450
        self.height = 300

        self.result_font_color = 'black'
        self.result_bg_color = 'lightgrey'
        self.result_margin = '10px'

        self.X = self.data_frame.drop(columns=['Outcome'])  # Input data
        self.neg = self.X[self.data_frame['Outcome'] == 0]  # Input data from women who don't have diabetes.
        self.pos = self.X[self.data_frame['Outcome'] == 1]  # Input data from women who do have diabetes.
        self.y = self.data_frame['Outcome']  # Output data

        self.labels = [
            'Pregnancies',
            'Glucose',
            'BloodPressure',
            'SkinThickness',
            'Insulin',
            'BMI',
            'DiabetesPedigreeFunction',
            'Age'
        ]

        # Average values from entire dataset
        self.all_data_mean_values = [
            self.data_frame[self.labels[0]].mean(),
            self.data_frame[self.labels[1]].mean(),
            self.data_frame[self.labels[2]].mean(),
            self.data_frame[self.labels[3]].mean(),
            self.data_frame[self.labels[4]].mean(),
            self.data_frame[self.labels[5]].mean(),
            self.data_frame[self.labels[6]].mean(),
            self.data_frame[self.labels[7]].mean()
        ]

        # Average values from negative (no diabetes) dataset
        self.negative_mean_values = [
            self.neg[self.labels[0]].mean(),
            self.neg[self.labels[1]].mean(),
            self.neg[self.labels[2]].mean(),
            self.neg[self.labels[3]].mean(),
            self.neg[self.labels[4]].mean(),
            self.neg[self.labels[5]].mean(),
            self.neg[self.labels[6]].mean(),
            self.neg[self.labels[7]].mean()
        ]

        # Average values from positive (has diabetes) dataset
        self.positive_mean_values = [
            self.pos[self.labels[0]].mean(),
            self.pos[self.labels[1]].mean(),
            self.pos[self.labels[2]].mean(),
            self.pos[self.labels[3]].mean(),
            self.pos[self.labels[4]].mean(),
            self.pos[self.labels[5]].mean(),
            self.pos[self.labels[6]].mean(),
            self.pos[self.labels[7]].mean()
        ]

        # _-_-_-_-_-_-_-_-_-_-_-_-_ Test Data _-_-_-_-_-_-_-_-_-_-_-_-_
        should_be_diabetic = [7, 150, 70, 35, 0, 35, 1, 50]
        should_not_be_diabetic = [1, 99, 62, 0, 0, 27, .24, 24]

        self.user_data_list = []

        self.initUI()

    def initUI(self):
        # Define the window title
        self.setWindowTitle('Predict Diabetes')

        # Define the window geometry
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_layout()

        # Horizontal layout (Widgets are stacked horizontally)
        predict_window_layout = QVBoxLayout()

        # Define groupbox and add it to the layout
        spinbox_groupbox = QGroupBox('Enter Data')

        predict_window_layout.addWidget(self.outcome_label)
        predict_window_layout.addWidget(self.default_value_dropdown)
        predict_window_layout.addWidget(spinbox_groupbox)

        # Vertical layout for the spin boxes (Widgets are stacked horizontally)
        spinbox_layout = QGridLayout()

        spinbox_groupbox.setLayout(spinbox_layout)

        # Adding the spin boxes and their labels to the spin box layout
        spinbox_layout.addWidget(self.pregnancy_spinbox_label, 0, 0)
        spinbox_layout.addWidget(self.pregnancy_spinbox, 1, 0)

        spinbox_layout.addWidget(self.glucose_spinbox_label, 2, 0)
        spinbox_layout.addWidget(self.glucose_spinbox, 3, 0)

        spinbox_layout.addWidget(self.blood_pressure_spinbox_label, 4, 0)
        spinbox_layout.addWidget(self.blood_pressure_spinbox, 5, 0)

        spinbox_layout.addWidget(self.skin_thickness_spinbox_label, 6, 0)
        spinbox_layout.addWidget(self.skin_thickness_spinbox, 7, 0)

        spinbox_layout.addWidget(self.insulin_spinbox_label, 0, 1)
        spinbox_layout.addWidget(self.insulin_spinbox, 1, 1)

        spinbox_layout.addWidget(self.bmi_spinbox_label, 2, 1)
        spinbox_layout.addWidget(self.bmi_spinbox, 3, 1)

        spinbox_layout.addWidget(self.diabetes_pedigree_function_spinbox_label, 4, 1)
        spinbox_layout.addWidget(self.diabetes_pedigree_function_spinbox, 5, 1)

        spinbox_layout.addWidget(self.age_spinbox_label, 6, 1)
        spinbox_layout.addWidget(self.age_spinbox, 7, 1)

        spinbox_layout.addWidget(self.predict_button, 8, 0, 1, 2)

        # Adding the button to the layout
        predict_window_layout.addWidget(self.close_predict_window_button)

        # Setting the layout
        self.setLayout(predict_window_layout)


    def create_layout(self):

        self.outcome_label = QLabel('Result: Waiting for User')
        self.outcome_label.setFrameStyle(QFrame.Panel)
        self.outcome_label.setAlignment(Qt.AlignHCenter)

        # Label border
        self.outcome_label.setStyleSheet(
            f'color: {self.result_font_color};'
            f'background-color: {self.result_bg_color};'
            f'border: 2px solid black;'
            f'margin: {self.result_margin}'
        )

        self.outcome_label.setFont(QFont('Default', 14))
        # self.outcome_label.setStyleSheet('background-color: red')

        self.default_value_dropdown = QComboBox(self)

        self.default_value_dropdown.addItems([
            'Entire Dataset (Default)',
            'Negative Dataset (Women who don\'t have diabetes)',
            'Positive Dataset (Women who do have diabetes)'
        ])

        # Defining the spin boxs and their labels
        self.pregnancy_spinbox_label = QLabel('Pregnancies')
        self.pregnancy_spinbox = QSpinBox(self)
        self.pregnancy_spinbox.setMinimum(self.data_frame[self.labels[0]].min())
        self.pregnancy_spinbox.setMaximum(self.data_frame[self.labels[0]].max())
        self.pregnancy_spinbox.setValue(int(self.data_frame[self.labels[0]].mean()))

        self.glucose_spinbox_label = QLabel('Glucose')
        self.glucose_spinbox = QSpinBox(self)
        self.glucose_spinbox.setMinimum(self.data_frame[self.labels[1]].min())
        self.glucose_spinbox.setMaximum(self.data_frame[self.labels[1]].max())
        self.glucose_spinbox.setValue(int(self.data_frame[self.labels[1]].mean()))

        self.blood_pressure_spinbox_label = QLabel('Blood Pressure')
        self.blood_pressure_spinbox = QSpinBox(self)
        self.blood_pressure_spinbox.setMinimum(self.data_frame[self.labels[2]].min())
        self.blood_pressure_spinbox.setMaximum(self.data_frame[self.labels[2]].max())
        self.blood_pressure_spinbox.setValue(int(self.data_frame[self.labels[2]].mean()))

        self.skin_thickness_spinbox_label = QLabel('Skin Thickness')
        self.skin_thickness_spinbox = QSpinBox(self)
        self.skin_thickness_spinbox.setMinimum(self.data_frame[self.labels[3]].min())
        self.skin_thickness_spinbox.setMaximum(self.data_frame[self.labels[3]].max())
        self.skin_thickness_spinbox.setValue(int(self.data_frame[self.labels[3]].mean()))

        self.insulin_spinbox_label = QLabel('Insulin')
        self.insulin_spinbox = QSpinBox(self)
        self.insulin_spinbox.setMinimum(self.data_frame[self.labels[4]].min())
        self.insulin_spinbox.setMaximum(self.data_frame[self.labels[4]].max())
        self.insulin_spinbox.setValue(int(self.data_frame[self.labels[4]].mean()))

        self.bmi_spinbox_label = QLabel('Body Mass Index')
        self.bmi_spinbox = QDoubleSpinBox(self)
        self.bmi_spinbox.setDecimals(1)
        self.bmi_spinbox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.bmi_spinbox.setMinimum(float(self.data_frame[self.labels[5]].min()))
        self.bmi_spinbox.setMaximum(float(self.data_frame[self.labels[5]].max()))
        self.bmi_spinbox.setValue(float(self.data_frame[self.labels[5]].mean()))

        self.diabetes_pedigree_function_spinbox_label = QLabel('Diabetes Pedigree Function')
        self.diabetes_pedigree_function_spinbox = QDoubleSpinBox(self)
        self.diabetes_pedigree_function_spinbox.setDecimals(2)
        self.diabetes_pedigree_function_spinbox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.diabetes_pedigree_function_spinbox.setMinimum(self.data_frame[self.labels[6]].min())
        self.diabetes_pedigree_function_spinbox.setMaximum(self.data_frame[self.labels[6]].max())
        self.diabetes_pedigree_function_spinbox.setValue(float(self.data_frame[self.labels[6]].mean()))

        self.age_spinbox_label = QLabel('Age')
        self.age_spinbox = QSpinBox(self)
        self.age_spinbox.setMinimum(self.data_frame[self.labels[7]].min())
        self.age_spinbox.setMaximum(self.data_frame[self.labels[7]].max())
        self.age_spinbox.setValue(int(self.data_frame[self.labels[7]].mean()))

        self.predict_button = QPushButton('Make Prediction')
        self.predict_button.clicked.connect(self.prediction_outcome)

        # Close window button
        self.close_predict_window_button = QPushButton('Close Window')

        # Adding action to the buttons
        self.close_predict_window_button.clicked.connect(self.close)

    # def prepare_data(self):
        # Prepare Data

        # # Print data from data frames
        # print(f'Min Values: {X.min().to_numpy()}')
        # print(f'Avg Neg Values: {neg.mean().to_numpy()}')
        # print(f'Avg Pos Values: {pos.mean().to_numpy()}')
        # print(f'Max Values: {X.max().to_numpy()}')
        #
        # # Describe DF
        # print(f'\nDescribe DF:\n{X.describe()}')
        # print(f'\nDescribe neg:\n{neg.describe()}')
        # print(f'\nDescribe pos:\n{pos.describe()}')

        # return X, y, neg, pos

    @staticmethod
    def train_data(X, y):
        # Split the data set into two random sets, one for training, one for testing.
        return train_test_split(X, y, test_size=0.2)  # returns X_train, X_test, y_train, y_test (in that order)

    # def predict_data(self, X_train, X_test, y_train, y_test, user_values):
    def predict_data(self, user_values):

        # print(f'X Train: {X_train}')
        # print(f'y Train: {y_train}')
        # print(f'X Test: {X_test}')
        # print(f'y Test: {y_test}')
        print(f'user_values: {user_values}')

        # Define the data model
        self.model = DecisionTreeClassifier()

        # model.fit(X_train, y_train)  # Train the model with training data set
        self.model.fit(self.X.values, self.y.values)  # Train the model with training data set
        prediction = self.model.predict(user_values)  # Ask for a prediction with test data set

        # Calculating the Accuracy Score
        # ac_score = accuracy_score(y, prediction)

        # Print the prediction(s)
        print(f'\nPrediction:\n{prediction}')

        outcome = ['Does not have diabetes', 'Has diabetes']

        # Print the Accuracy Score
        # print(f'Accuracy Score: {round(ac_score * 100, 2)}%')

        if prediction[0] == 0:
            self.result_font_color = 'green'
        else:
            self.result_font_color = 'red'

        self.outcome_label.setStyleSheet(
            f'color: {self.result_font_color};'
            f'background-color: {self.result_bg_color}'
        )

        self.outcome_label.setText(f'Result: {outcome[prediction[0]]}')  #(Accuracy: {round(ac_score * 100, 2)}%)')

    def create_persisting_model(self):
        # joblib.dump(self.model, )
        pass

    def load_persisting_model(self):
        # return joblib(self.model, )
        pass

    def prediction_outcome(self):

        self.user_data_list = [
            self.pregnancy_spinbox.value(),
            self.glucose_spinbox.value(),
            self.blood_pressure_spinbox.value(),
            self.skin_thickness_spinbox.value(),
            self.insulin_spinbox.value(),
            self.bmi_spinbox.value(),
            self.diabetes_pedigree_function_spinbox.value(),
            self.age_spinbox.value()
        ]

        # print(f'X: {self.X}')
        # print(f'y: {self.y}')
        # print(f'user_data_list: {self.user_data_list}')

        # print(f'self.train_data(self.prepare_data()[0], self.prepare_data()[1])[0] is: {self.train_data(self.prepare_data()[0], self.prepare_data()[1])[0],}')
        # print(f'self.train_data(self.prepare_data()[0], self.prepare_data()[1])[1] is: {self.train_data(self.prepare_data()[0], self.prepare_data()[1])[1],}')
        # print(f'self.train_data(self.prepare_data()[0], self.prepare_data()[1])[2] is: {self.train_data(self.prepare_data()[0], self.prepare_data()[1])[2],}')
        # print(f'self.train_data(self.prepare_data()[0], self.prepare_data()[1])[3] is: {self.train_data(self.prepare_data()[0], self.prepare_data()[1])[3],}')
        self.predict_data([self.user_data_list])
