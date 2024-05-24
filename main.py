import os.path
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from plot_data import PlotData
from process_and_train_data import ProcessAndTrainData
import pandas as pd
import numpy as np


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Define variables
        self.diabetes_dataset = 'diabetes.csv'

        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 300
        self.button_height = 40
        self.button_width = 400

        self.ptd = ''
        self.pldata = ''

        # Define widgets
        self.csv_loaded_label = QLabel()

        self.check_for_csv_file_button = QPushButton('Check for CSV File Again')
        self.dataset_selection_label = QLabel('Select a dataset to use: ')
        self.dataset_selection_combobox = QComboBox(self)
        self.show_graphs_button = QPushButton('Show Graphs')
        self.predict_button = QPushButton('Predict')
        self.close_button = QPushButton('Close')

        # Call the method to initialize the widgets
        self.initialize_user_interface()

    def initialize_user_interface(self):

        # Define the window title
        self.setWindowTitle('Diabetes Predictor')

        # Define the window geometry
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Calling the method that creates the
        self.modify_widgets()

        # Define the layout types
        main_window_layout = QVBoxLayout()
        dataset_selection_layout = QHBoxLayout()

        # Add widgets to the dataset selection layout
        dataset_selection_layout.addWidget(self.dataset_selection_label)
        dataset_selection_layout.addWidget(self.dataset_selection_combobox)

        # Add widgets to layout
        main_window_layout.addWidget(self.csv_loaded_label)
        main_window_layout.addLayout(dataset_selection_layout)
        main_window_layout.addWidget(self.check_for_csv_file_button)
        main_window_layout.addWidget(self.show_graphs_button)
        main_window_layout.addWidget(self.predict_button)
        main_window_layout.addWidget(self.close_button)

        self.setLayout(main_window_layout)

    def modify_widgets(self):

        # Define the CSV loaded label alignment to be centered
        self.csv_loaded_label.setAlignment(Qt.AlignCenter)

        # Add items to the dataset selection combobox
        self.dataset_selection_combobox.addItems(['Original Dataset', 'Cleaned Dataset'])

        # Define the height of the buttons
        self.check_for_csv_file_button.setFixedHeight(self.button_height)
        self.show_graphs_button.setFixedHeight(self.button_height)
        self.predict_button.setFixedHeight(self.button_height)
        self.close_button.setFixedHeight(self.button_height)

        # Defining the methods to be called upon a button glick for the given buttons
        self.check_for_csv_file_button.clicked.connect(self.check_for_csv_file)
        self.show_graphs_button.clicked.connect(self.show_graphs)
        self.predict_button.clicked.connect(self.make_prediction)
        self.close_button.clicked.connect(self.close_window)

        # Check for the csv dataset file
        self.check_for_csv_file()

    def check_for_csv_file(self):

        result = ''
        extra_details = ''

        # If the csv dataset file is not found
        if not os.path.isfile(self.diabetes_dataset):
            result = ' not'
            extra_details = f'\nPlease put "{self.diabetes_dataset}" in the same directory as this program.'

            # Show the "Check for CSV File" button and disable the predict and plot buttons
            self.check_for_csv_file_button.setHidden(False)
            self.predict_button.setDisabled(True)
            self.show_graphs_button.setDisabled(True)

        # If the csv file dataset is found
        else:

            # Hide the "Check for CSV File" button and enable the predict and plot buttons
            self.check_for_csv_file_button.setHidden(True)
            self.predict_button.setDisabled(False)
            self.show_graphs_button.setDisabled(False)

        print(f'The diabetes dataset CSV file has{result} been found!{extra_details}')
        self.csv_loaded_label.setText(f'The diabetes dataset CSV file has{result} been found!{extra_details}')

    def load_data(self, csv_data):

        # Use Pandas to load the csv dataset file
        selected_dataframe = pd.read_csv(csv_data)

        # Return the original dataframe if it was selected from the dataset selection combobox
        if self.dataset_selection_combobox.currentIndex() == 0:
            print('\nOriginal data set has been loaded')
            return selected_dataframe

        # Return a modified dataframe if it was selected from the dataset selection combobox
        if self.dataset_selection_combobox.currentIndex() == 1:

            # Copy the original dataframe
            selected_dataframe_copy = selected_dataframe.copy(deep=True)

            # Replace all 0 values in the given columns with "NaN"
            selected_dataframe_copy[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = (
                selected_dataframe_copy[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(
                    0, np.NaN
                ))

            # Replace all "NaN" values to the average value of the given column
            selected_dataframe_copy['Glucose'].fillna(selected_dataframe_copy['Glucose'].mean(), inplace=True)
            selected_dataframe_copy['BloodPressure'].fillna(
                selected_dataframe_copy['BloodPressure'].mean(), inplace=True
            )
            selected_dataframe_copy['SkinThickness'].fillna(
                selected_dataframe_copy['SkinThickness'].mean(), inplace=True
            )
            selected_dataframe_copy['Insulin'].fillna(selected_dataframe_copy['Insulin'].mean(), inplace=True)
            selected_dataframe_copy['BMI'].fillna(selected_dataframe_copy['BMI'].mean(), inplace=True)
            print('Cleaned data set has been loaded')

            return selected_dataframe_copy

    def make_prediction(self):

        # Open the prediction window only if the dataset file is found
        try:
            self.ptd = ProcessAndTrainData(self.load_data(self.diabetes_dataset))
        except FileNotFoundError:
            self.check_for_csv_file()
        else:
            print('Opening the Prediction Window')
            self.ptd.show()

    def show_graphs(self):

        # Open the graph window only if the dataset file is found
        try:
            self.pldata = PlotData(self.load_data(self.diabetes_dataset))
        except FileNotFoundError:
            self.check_for_csv_file()
        else:
            print('Opening the Graph Window')
            self.pldata.show()

    @staticmethod
    def close_window():

        print('Exiting Main Application')

        # Close the main window and any other child windows
        QApplication.closeAllWindows()


if __name__ == '__main__':

    # Create PyQt5 app
    App = QApplication(sys.argv)

    # Create the instance of the Window
    main_window = MainWindow()

    # Show the window and all the widgets
    print('\nShowing the Main Window.')
    main_window.show()

    # Start the app loop
    App.exec()
