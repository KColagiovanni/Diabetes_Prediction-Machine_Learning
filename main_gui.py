import sys
from PyQt5.QtWidgets import *
from plot_data import PlotData
from process_and_train_data import ProcessAndTrainData


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        widget_width = 150
        pos_x = 125

        # Define the window title
        self.setWindowTitle('Do you have diabetes?')

        # Define the window geometry
        self.setGeometry(0, 0, 400, 350)

        # Define accuracy label widget
        self.accuracy_label = QLabel("Accuracy: ", self)

        # Defining position and size of label
        self.accuracy_label.move(pos_x, 250)
        self.accuracy_label.resize(widget_width, 25)

        # Label border
        self.accuracy_label.setStyleSheet("border: 1px solid black;")

        # Show scatter plots button
        self.show_graphs_button = QPushButton(self)
        self.show_graphs_button.setText('Show Graphs')
        self.show_graphs_button.setFixedWidth(widget_width)
        self.show_graphs_button.move(pos_x, 150)
        self.show_graphs_button.clicked.connect(self.show_graphs)

        # Predict data button
        self.predict_button = QPushButton(self)
        self.predict_button.setText('Predict')
        self.predict_button.setFixedWidth(widget_width)
        self.predict_button.move(pos_x, 200)
        self.predict_button.clicked.connect(self.make_prediction)

        # Close button
        self.close_button = QPushButton(self)
        self.close_button.setText('Close')
        self.close_button.setFixedWidth(widget_width)
        self.close_button.move(pos_x, 300)
        self.close_button.clicked.connect(self.close_window)

        # Show the window and all the widgets
        print('Showing the main window.')
        self.show()

    def make_prediction(self):
        ptd = ProcessAndTrainData()
        data_frame = ptd.load_data('diabetes.csv')
        X, y, neg, pos = ptd.prepare_data(data_frame)
        X_train, X_test, y_train, y_test = ptd.train_data(X, y)
        accuracy_score = ptd.predict_data(X_train, X_test, y_train, y_test)
        self.accuracy_label.setText(f'Accuracy: {round(accuracy_score * 100, 2)}%')

    # @staticmethod
    def show_graphs(self):
        print('In show_graphs() method')
        self.pd = PlotData()
        self.pd.show()

    def close_window(self):

        print('Exiting Application')

        # Close the window
        self.close()


if __name__ == '__main__':

    # Create PyQt5 app
    App = QApplication(sys.argv)

    # Create the instance of the Window
    window = MainWindow()

    # Start the app loop
    sys.exit(App.exec())
