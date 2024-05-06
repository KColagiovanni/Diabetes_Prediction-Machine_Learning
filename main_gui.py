import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from plot_data import PlotData
from process_and_train_data import ProcessAndTrainData
import pandas as pd


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        widget_width = 150
        pos_x = 125
        self.diabetes_dataset = 'diabetes.csv'

        # Define the window title
        self.setWindowTitle('Do you have diabetes?')

        # Define the window geometry
        self.setGeometry(0, 0, 400, 150)

        main_window_layout = QGridLayout()

        # Show scatter plots button
        show_graphs_button = QPushButton('Show Graphs')
        show_graphs_button.clicked.connect(self.show_graphs)
        main_window_layout.addWidget(show_graphs_button, 0, 0)

        # Predict data button
        predict_button = QPushButton('Predict')
        predict_button.clicked.connect(self.make_prediction)
        main_window_layout.addWidget(predict_button, 0, 1)

        # Close button
        close_button = QPushButton('Close')
        close_button.clicked.connect(self.close_window)
        main_window_layout.addWidget(close_button, 1, 0, 1, 2)

        self.setLayout(main_window_layout)

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
