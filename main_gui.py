from PyQt5.QtWidgets import *
import sys
from process_and_train_data import ProcessAndTrainData


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        widget_width = 150
        pos_x = 125

        # Define the window title
        self.setWindowTitle('Do you have diabetes?')

        # Define the window geometry
        self.setGeometry(0, 0, 400, 350)

        # Creating an accuracy label widget
        self.accuracy_label = QLabel("Accuracy: ", self)

        # Defining position
        self.accuracy_label.move(pos_x, 250)

        self.accuracy_label.resize(widget_width, 25)

        # setting up border
        self.accuracy_label.setStyleSheet("border: 1px solid black;")

        # Show bar graph button
        self.bar_graph_button = QPushButton(self)
        self.bar_graph_button.setText('Show Bar Graph')
        self.bar_graph_button.setFixedWidth(widget_width)
        self.bar_graph_button.move(pos_x, 100)
        self.bar_graph_button.clicked.connect(self.show_bar_graph)

        # Show scatter plots button
        self.scatter_plots_button = QPushButton(self)
        self.scatter_plots_button.setText('Show Scatter Plot')
        self.scatter_plots_button.setFixedWidth(widget_width)
        self.scatter_plots_button.move(pos_x, 150)
        self.scatter_plots_button.clicked.connect(self.show_scatter_plots)

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
        self.show()

    def make_prediction(self):
        pt = ProcessAndTrainData()
        data_frame = pt.load_data('diabetes.csv')
        X, y, neg, pos = pt.prepare_data(data_frame)
        X_train, X_test, y_train, y_test = pt.train_data(X, y)
        accuracy_score = pt.predict_data(X_train, X_test, y_train, y_test)
        self.accuracy_label.setText(f'Accuracy: {round(accuracy_score * 100, 2)}%')

    def show_bar_graph(self):
        print('Bar Graph')

    def show_scatter_plots(self):
        print('Scatter Plot')

    def close_window(self):
        print('Exiting Application')

        # Close the window
        self.close()

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())


if __name__ == '__main__':
    window()
