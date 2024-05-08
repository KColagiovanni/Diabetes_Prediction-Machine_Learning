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
        self.width = 400
        self.height = 150

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

        main_window_layout = QGridLayout()

        # Add widgets to layout
        main_window_layout.addWidget(self.show_graphs_button, 0, 0)
        main_window_layout.addWidget(self.predict_button, 0, 1)
        main_window_layout.addWidget(self.close_button, 1, 0, 1, 2)

        self.setLayout(main_window_layout)

    def modify_widgets(self):

        self.show_graphs_button.clicked.connect(self.show_graphs)
        self.predict_button.clicked.connect(self.make_prediction)
        self.close_button.clicked.connect(self.close_window)

    @staticmethod
    def load_data(csv_data):
        return pd.read_csv(csv_data)

    def make_prediction(self):
        # print(self.load_data(self.diabetes_dataset))
        self.ptd = ProcessAndTrainData(self.load_data(self.diabetes_dataset))
        self.ptd.show()
        # ptd = ProcessAndTrainData()
        # data_frame = ptd.load_data('diabetes.csv')
        # X, y, neg, pos = ptd.prepare_data(data_frame)
        # X_train, X_test, y_train, y_test = ptd.train_data(X, y)
        # accuracy_score = ptd.predict_data(X_train, X_test, y_train, y_test)
        # self.accuracy_label.setText(f'Accuracy: {round(accuracy_score * 100, 2)}%')

    # @staticmethod
    def show_graphs(self):
        self.pldata = PlotData(self.load_data(self.diabetes_dataset))
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
