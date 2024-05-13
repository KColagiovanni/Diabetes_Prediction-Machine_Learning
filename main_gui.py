import os.path
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from plot_data import PlotData
from process_and_train_data import ProcessAndTrainData
import pandas as pd


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.diabetes_dataset = 'diabetes.csv'

        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 250
        self.button_height = 40
        self.button_width = 400

        self.csv_loaded_label = QLabel()

        self.ptd = ''
        self.pldata = ''

        self.check_for_csv_file_button = QPushButton('Check for CSV File Again')
        self.show_graphs_button = QPushButton('Show Graphs')
        self.predict_button = QPushButton('Predict')
        self.close_button = QPushButton('Close')

        self.initialize_user_interface()

    def initialize_user_interface(self):

        # Define the window title
        self.setWindowTitle('Do you have diabetes?')

        # Define the window geometry
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Calling the method that creates the
        self.modify_widgets()

        main_window_layout = QVBoxLayout()

        # Add widgets to layout
        main_window_layout.addWidget(self.csv_loaded_label)
        main_window_layout.addWidget(self.check_for_csv_file_button)
        main_window_layout.addWidget(self.show_graphs_button)
        main_window_layout.addWidget(self.predict_button)
        main_window_layout.addWidget(self.close_button)

        self.setLayout(main_window_layout)

    def modify_widgets(self):

        self.csv_loaded_label.setAlignment(Qt.AlignCenter)

        self.check_for_csv_file_button.setFixedHeight(self.button_height)
        # self.check_for_csv_file_button.setFixedWidth(self.button_width)
        # self.check_for_csv_file_button.setToolTip('')

        self.show_graphs_button.setFixedHeight(self.button_height)
        # self.show_graphs_button.setFixedWidth(self.button_width)

        self.predict_button.setFixedHeight(self.button_height)
        # self.predict_button.setFixedWidth(self.button_width)

        self.close_button.setFixedHeight(self.button_height)
        # self.close_button.setFixedWidth(self.button_width)

        self.check_for_csv_file_button.clicked.connect(self.check_for_csv_file)
        self.show_graphs_button.clicked.connect(self.show_graphs)
        self.predict_button.clicked.connect(self.make_prediction)
        self.close_button.clicked.connect(self.close_window)

        self.check_for_csv_file()

    def check_for_csv_file(self):
        result = ''
        extra_details = ''

        if not os.path.isfile(self.diabetes_dataset):
            result = ' not'
            extra_details = f'\nPlease put "{self.diabetes_dataset}" in the same directory as this program.'
            self.check_for_csv_file_button.setHidden(False)
            self.predict_button.setDisabled(True)
            self.show_graphs_button.setDisabled(True)
        else:
            self.check_for_csv_file_button.setHidden(True)
            self.predict_button.setDisabled(False)
            self.show_graphs_button.setDisabled(False)

        self.csv_loaded_label.setText(f'The diabetes dataset CSV file has{result} been found!{extra_details}')

    @staticmethod
    def load_data(csv_data):
        return pd.read_csv(csv_data)

    def make_prediction(self):
        # print(self.load_data(self.diabetes_dataset))
        try:
            self.ptd = ProcessAndTrainData(self.load_data(self.diabetes_dataset))
        except FileNotFoundError:
            self.check_for_csv_file()
        else:
            self.ptd.show()
        # ptd = ProcessAndTrainData()
        # data_frame = ptd.load_data('diabetes.csv')
        # X, y, neg, pos = ptd.prepare_data(data_frame)
        # X_train, X_test, y_train, y_test = ptd.train_data(X, y)
        # accuracy_score = ptd.predict_data(X_train, X_test, y_train, y_test)
        # self.accuracy_label.setText(f'Accuracy: {round(accuracy_score * 100, 2)}%')

    # @staticmethod
    def show_graphs(self):
        try:
            self.pldata = PlotData(self.load_data(self.diabetes_dataset))
        except FileNotFoundError:
            self.check_for_csv_file()
        else:
            self.pldata.show()

    def close_window(self):

        print('Exiting Application')

        # Close the window
        self.close()


if __name__ == '__main__':

    # Create PyQt5 app
    App = QApplication(sys.argv)

    # Create the instance of the Window
    main_window = MainWindow()

    # Show the window and all the widgets
    print('Showing the main window.')
    main_window.show()

    # Start the app loop
    App.exec()
