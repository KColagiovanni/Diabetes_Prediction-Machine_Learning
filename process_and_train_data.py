from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import accuracy_score
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import glob
import time


class ProcessAndTrainData(QWidget):

    def __init__(self, data_frame):
        super().__init__()

        self.data_frame = data_frame
        self.left = 1000
        self.top = 0
        self.width = 450
        self.height = 300

        self.result_font_color = 'black'
        self.result_bg_color = 'lightgray'
        self.result_padding = '10px'
        self.result_border_thickness = '2px'

        self.X = self.data_frame.drop(columns=['Outcome'])  # Input data
        self.neg = self.X[self.data_frame['Outcome'] == 0]  # Input data from women who don't have diabetes.
        self.pos = self.X[self.data_frame['Outcome'] == 1]  # Input data from women who do have diabetes.
        self.y = self.data_frame['Outcome']  # Output data

        self.training_sample_size = 0.2
        self.ac_score = 0

        self.persisting_model_name = 'diabetes_predictions'
        self.persisting_model_filetype = 'joblib'

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

        self.user_data_list = []

        # Defining Label Widgets
        self.outcome_label = QLabel('Waiting for User to Enter Data')
        self.pregnancy_spinbox_label = QLabel('Pregnancies')
        self.glucose_spinbox_label = QLabel('Glucose')
        self.blood_pressure_spinbox_label = QLabel('Blood Pressure')
        self.skin_thickness_spinbox_label = QLabel('Skin Thickness')
        self.insulin_spinbox_label = QLabel('Insulin')
        self.bmi_spinbox_label = QLabel('Body Mass Index')
        self.diabetes_pedigree_function_spinbox_label = QLabel('Diabetes Pedigree Function')
        self.age_spinbox_label = QLabel('Age')
        self.dataset_selection_label = QLabel('Predefined Values: ')
        self.training_model_accuracy_label = QLabel('Training Model Accuracy:')
        self.horizontal_line1 = QLabel()
        self.horizontal_line2 = QLabel()
        self.horizontal_line3 = QLabel()

        # Defining Spinbox Widgets
        self.dataset_selection_dropdown = QComboBox(self)
        self.pregnancy_spinbox = QSpinBox(self)
        self.glucose_spinbox = QSpinBox(self)
        self.blood_pressure_spinbox = QSpinBox(self)
        self.skin_thickness_spinbox = QSpinBox(self)
        self.insulin_spinbox = QSpinBox(self)
        self.bmi_spinbox = QDoubleSpinBox(self)
        self.diabetes_pedigree_function_spinbox = QDoubleSpinBox(self)
        self.age_spinbox = QSpinBox(self)

        # Defining Button Widgets
        self.predict_button = QPushButton('Make Prediction')
        self.retrain_model_button = QPushButton('Retrain Model')
        self.close_predict_window_button = QPushButton('Close Window')

        # Define data models
        self.training_model = DecisionTreeClassifier()

        # Calling the method that initializes the User Interface layouts
        self.initialize_user_interface()

    def initialize_user_interface(self):

        # Define the window title
        self.setWindowTitle('Predict Diabetes')

        # Define the prediction window geometry
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Calling the method that creates the
        self.modify_widgets()

        # Vertical layout for the window widgets
        predict_window_layout = QVBoxLayout()

        # Horizontal layout for the dataset selection and it's label
        dataset_selection_layout = QHBoxLayout()

        # Horizontal layout for the training accuracy button and label
        training_accuracy_layout = QHBoxLayout()

        # Define groupbox and add it to the layout
        spinbox_groupbox = QGroupBox()

        dataset_selection_layout.addWidget(self.dataset_selection_label)
        dataset_selection_layout.addWidget(self.dataset_selection_dropdown)
        predict_window_layout.addWidget(self.outcome_label)
        predict_window_layout.addWidget(self.horizontal_line1)
        predict_window_layout.addLayout(dataset_selection_layout)
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

        predict_window_layout.addWidget(self.horizontal_line2)

        training_accuracy_layout.addWidget(self.retrain_model_button)
        training_accuracy_layout.addWidget(self.training_model_accuracy_label)

        predict_window_layout.addLayout(training_accuracy_layout)

        predict_window_layout.addWidget(self.horizontal_line3)

        # Adding the button to the layout
        predict_window_layout.addWidget(self.close_predict_window_button)

        # Setting the layout
        self.setLayout(predict_window_layout)

    def modify_widgets(self):

        self.outcome_label.setFont(QFont('Default', 14))
        self.outcome_label.setFrameStyle(QFrame.StyledPanel)
        self.outcome_label.setAlignment(Qt.AlignCenter)
        self.outcome_label.setStyleSheet(
            f'color: {self.result_font_color};'
            f'background-color: {self.result_bg_color};'
            f'border: {self.result_border_thickness} solid {self.result_font_color};'
            f'padding: {self.result_padding}'
        )

        self.horizontal_line1.setFrameStyle(QFrame.HLine)
        self.horizontal_line2.setFrameStyle(QFrame.HLine)
        self.horizontal_line3.setFrameStyle(QFrame.HLine)

        self.dataset_selection_dropdown.addItems([
            'Entire Dataset Average (Default)',
            'Negative Dataset Average (Women who don\'t have diabetes)',
            'Positive Dataset Average (Women who do have diabetes)',
            'Values that should indicate diabetes',
            'Values that should indicate no diabetes'
        ])
        self.dataset_selection_dropdown.currentIndexChanged.connect(
            self.get_current_dataset_selection_dropdown_selection
        )

        # Defining the spin boxs and their labels
        self.pregnancy_spinbox.setMinimum(self.data_frame[self.labels[0]].min())
        self.pregnancy_spinbox.setMaximum(self.data_frame[self.labels[0]].max())
        self.pregnancy_spinbox.setValue(int(self.data_frame[self.labels[0]].mean()))

        self.glucose_spinbox.setMinimum(int(self.data_frame[self.labels[1]].min()))
        self.glucose_spinbox.setMaximum(int(self.data_frame[self.labels[1]].max()))
        self.glucose_spinbox.setValue(int(self.data_frame[self.labels[1]].mean()))

        self.blood_pressure_spinbox.setMinimum(int(self.data_frame[self.labels[2]].min()))
        self.blood_pressure_spinbox.setMaximum(int(self.data_frame[self.labels[2]].max()))
        self.blood_pressure_spinbox.setValue(int(self.data_frame[self.labels[2]].mean()))

        self.skin_thickness_spinbox.setMinimum(int(self.data_frame[self.labels[3]].min()))
        self.skin_thickness_spinbox.setMaximum(int(self.data_frame[self.labels[3]].max()))
        self.skin_thickness_spinbox.setValue(int(self.data_frame[self.labels[3]].mean()))

        self.insulin_spinbox.setMinimum(int(self.data_frame[self.labels[4]].min()))
        self.insulin_spinbox.setMaximum(int(self.data_frame[self.labels[4]].max()))
        self.insulin_spinbox.setValue(int(self.data_frame[self.labels[4]].mean()))

        self.bmi_spinbox.setDecimals(2)
        self.bmi_spinbox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.bmi_spinbox.setMinimum(float(self.data_frame[self.labels[5]].min()))
        self.bmi_spinbox.setMaximum(float(self.data_frame[self.labels[5]].max()))
        self.bmi_spinbox.setValue(float(self.data_frame[self.labels[5]].mean()))

        self.diabetes_pedigree_function_spinbox.setDecimals(2)
        self.diabetes_pedigree_function_spinbox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.diabetes_pedigree_function_spinbox.setMinimum(self.data_frame[self.labels[6]].min())
        self.diabetes_pedigree_function_spinbox.setMaximum(self.data_frame[self.labels[6]].max())
        self.diabetes_pedigree_function_spinbox.setValue(float(self.data_frame[self.labels[6]].mean()))

        self.age_spinbox.setMinimum(self.data_frame[self.labels[7]].min())
        self.age_spinbox.setMaximum(self.data_frame[self.labels[7]].max())
        self.age_spinbox.setValue(int(self.data_frame[self.labels[7]].mean()))

        self.predict_button.clicked.connect(self.prediction_outcome)

        self.retrain_model_button.clicked.connect(self.train_model_and_check_accuracy_using_training_data)

        # Adding action to the buttons
        self.close_predict_window_button.clicked.connect(self.close_predict_window)

        # Check if a persisting model exists in the cwd. If not, train and save one, else, get the accuracy score of the
        # existing model.
        if len(glob.glob(f'{self.persisting_model_name}*{self.persisting_model_filetype}')) == 0:
            self.train_model_and_check_accuracy_using_training_data()
        else:
            persisting_filename = glob.glob(f'{self.persisting_model_name}*{self.persisting_model_filetype}')[0]
            ac_score = persisting_filename.split('_')[2][:-7]
            self.training_model_accuracy_label.setText(f'Training Model Accuracy: {ac_score}%')

    def get_current_dataset_selection_dropdown_selection(self):

        # Set spin boxes to the average values of the entire dataset if the user selects if from the dropdown
        if self.dataset_selection_dropdown.currentIndex() == 0:
            self.pregnancy_spinbox.setValue(int(self.X[self.labels[0]].mean()))
            self.glucose_spinbox.setValue(int(self.X[self.labels[1]].mean()))
            self.blood_pressure_spinbox.setValue(int(self.X[self.labels[2]].mean()))
            self.skin_thickness_spinbox.setValue(int(self.X[self.labels[3]].mean()))
            self.insulin_spinbox.setValue(int(self.X[self.labels[4]].mean()))
            self.bmi_spinbox.setValue(float(self.X[self.labels[5]].mean()))
            self.diabetes_pedigree_function_spinbox.setValue(float(self.X[self.labels[6]].mean()))
            self.age_spinbox.setValue(int(self.X[self.labels[7]].mean()))

        # Set spin boxes to the average values of the negative (women who don't have diabetes) dataset if the user
        # selects if from the dropdown
        if self.dataset_selection_dropdown.currentIndex() == 1:
            self.pregnancy_spinbox.setValue(int(self.neg[self.labels[0]].mean()))
            self.glucose_spinbox.setValue(int(self.neg[self.labels[1]].mean()))
            self.blood_pressure_spinbox.setValue(int(self.neg[self.labels[2]].mean()))
            self.skin_thickness_spinbox.setValue(int(self.neg[self.labels[3]].mean()))
            self.insulin_spinbox.setValue(int(self.neg[self.labels[4]].mean()))
            self.bmi_spinbox.setValue(float(self.neg[self.labels[5]].mean()))
            self.diabetes_pedigree_function_spinbox.setValue(float(self.neg[self.labels[6]].mean()))
            self.age_spinbox.setValue(int(self.neg[self.labels[7]].mean()))

        # Set spin boxes to the average values of the positive (women who do have diabetes) dataset if the user selects
        # if from the dropdown
        if self.dataset_selection_dropdown.currentIndex() == 2:
            self.pregnancy_spinbox.setValue(int(self.pos[self.labels[0]].mean()))
            self.glucose_spinbox.setValue(int(self.pos[self.labels[1]].mean()))
            self.blood_pressure_spinbox.setValue(int(self.pos[self.labels[2]].mean()))
            self.skin_thickness_spinbox.setValue(int(self.pos[self.labels[3]].mean()))
            self.insulin_spinbox.setValue(int(self.pos[self.labels[4]].mean()))
            self.bmi_spinbox.setValue(float(self.pos[self.labels[5]].mean()))
            self.diabetes_pedigree_function_spinbox.setValue(float(self.pos[self.labels[6]].mean()))
            self.age_spinbox.setValue(int(self.pos[self.labels[7]].mean()))

        # Set spin boxes to the average values of the entire dataset if the user selects if from the dropdown
        if self.dataset_selection_dropdown.currentIndex() == 3:
            self.pregnancy_spinbox.setValue(int(self.pos[self.labels[0]].mean()) + 5)
            self.glucose_spinbox.setValue(int(self.pos[self.labels[1]].mean()) + 20)
            self.blood_pressure_spinbox.setValue(int(self.pos[self.labels[2]].mean()) + 20)
            self.skin_thickness_spinbox.setValue(int(self.pos[self.labels[3]].mean()) + 10)
            self.insulin_spinbox.setValue(int(self.pos[self.labels[4]].mean()) + 20)
            self.bmi_spinbox.setValue(float(self.pos[self.labels[5]].mean()) + 10.0)
            self.diabetes_pedigree_function_spinbox.setValue(float(self.pos[self.labels[6]].mean()) + 0.5)
            self.age_spinbox.setValue(int(self.pos[self.labels[7]].mean()) + 10)

        # Set spin boxes to values that will not have diabetes if the user selects if from the dropdown
        if self.dataset_selection_dropdown.currentIndex() == 4:
            self.pregnancy_spinbox.setValue(2)
            self.glucose_spinbox.setValue(100)
            self.blood_pressure_spinbox.setValue(65)
            self.skin_thickness_spinbox.setValue(20)
            self.insulin_spinbox.setValue(70)
            self.bmi_spinbox.setValue(25.0)
            self.diabetes_pedigree_function_spinbox.setValue(0.40)
            self.age_spinbox.setValue(45)

    def split_training_data(self):
        # Split the data set into two random sets, one for training, one for testing. Returns X_train, X_test, y_train,
        # y_test (in that order)
        return train_test_split(self.X.values, self.y.values, test_size=self.training_sample_size)

    def train_model_and_check_accuracy_using_training_data(self):

        x_train, x_test, y_train, y_test = self.split_training_data()

        self.training_model.fit(x_train, y_train)  # Train the model with training dataset

        prediction = self.training_model.predict(x_test)  # Get a prediction with test dataset

        # Calculating the Accuracy Score
        self.ac_score = round(accuracy_score(y_test, prediction) * 100, 2)

        # Print the Accuracy Score
        print(f'Accuracy Score: {self.ac_score}%')

        self.training_model_accuracy_label.setText(f'Training Model Accuracy: {self.ac_score}%')

        self.save_persisting_model()

    def save_persisting_model(self):

        # Delete any existing joblib files
        joblib_files = glob.glob(f'{self.persisting_model_name}*{self.persisting_model_filetype}')
        for file in joblib_files:
            print(f'Deleting {file}...')
            os.remove(file)

        joblib.dump(
            self.training_model,
            f'{self.persisting_model_name}_{self.ac_score}.{self.persisting_model_filetype}'
        )
        print(f'"{self.persisting_model_name}_{self.ac_score}.{self.persisting_model_filetype}"'
              f' was saved to {os.getcwd()}.')

    def load_persisting_model(self):

        persisting_filename = glob.glob(f'{self.persisting_model_name}*{self.persisting_model_filetype}')[0]

        try:
            load_model = joblib.load(persisting_filename)

        except FileNotFoundError:
            print()
            print('?!' * 60)
            print(f'"{self.persisting_model_name}" was not found in {os.getcwd()}')
            print('?!' * 60)
            quit()

        else:
            return load_model

    def make_prediction_using_user_entered_data(self, user_values):

        trained_model = self.load_persisting_model()

        prediction = trained_model.predict(user_values)  # Ask for a prediction using the user data set

        outcome = ['It is Predicted that You Do Not Have Diabetes', 'It is Predicted that You Have Diabetes']

        # Print the prediction(s)
        print()
        print('=' * 70)
        print(f'Prediction: {outcome[prediction[0]]}')
        print('=' * 70)

        if prediction[0] == 0:
            self.result_font_color = 'green'
        else:
            self.result_font_color = 'red'

        self.outcome_label.setStyleSheet(
            f'color: {self.result_font_color};'
            f'background-color: {self.result_bg_color};'
            f'border: {self.result_border_thickness} solid {self.result_font_color};'
            f'padding: {self.result_padding}'
        )

        self.outcome_label.setText(outcome[prediction[0]])  # (Accuracy: {round(ac_score * 100, 2)}%)')

    def prediction_outcome(self):

        start = time.perf_counter()

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

        self.make_prediction_using_user_entered_data([self.user_data_list])

        end = time.perf_counter()

        print(f'The prediction was done in {(end - start) * 10 ** 3:0.4f} ms')


    def close_predict_window(self):

        print('Closing the Prediction Window')

        # Close the prediction window
        self.close()
