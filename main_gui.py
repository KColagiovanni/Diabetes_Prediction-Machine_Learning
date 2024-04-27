from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        button_width = 150
        button_x = 125

        # Define the window title
        self.setWindowTitle('Do you have diabetes?')

        # Define the window geometry
        self.setGeometry(0, 0, 400, 300)

        # creating a label widget
        # self.label = QLabel("Icon is set", self)

        # moving position
        # self.label.move(100, 100)

        # setting up border
        # self.label.setStyleSheet("border: 1px solid black;")

        # Show bar graph button
        self.bar_graph_button = QPushButton(self)
        self.bar_graph_button.setText('Show Bar Graph')
        self.bar_graph_button.setFixedWidth(button_width)
        self.bar_graph_button.move(button_x, 150)

        # Show scatter plots button
        self.scatter_plots_button = QPushButton(self)
        self.scatter_plots_button.setText('Show Scatter Plot')
        self.scatter_plots_button.setFixedWidth(button_width)
        self.scatter_plots_button.move(button_x, 200)

        # Close button
        self.close_button = QPushButton(self)
        self.close_button.setText('Close')
        self.close_button.setFixedWidth(button_width)
        self.close_button.move(button_x, 250)
        self.close_button.clicked.connect(self.close_window)

        # Show the window and all the widgets
        self.show()

    def close_window(self):
        print('Exiting Application')

        # close the window
        self.close()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())


if __name__ == '__main__':
    window()
