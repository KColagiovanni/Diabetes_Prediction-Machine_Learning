# importing various libraries
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score


# main window
# which inherits QDialog
class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # Define the window title
        self.setWindowTitle('Plot')

        # Define the window geometry
        self.setGeometry(0, 0, 600, 600)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        # self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to 'plot' method
        self.button = QPushButton('Plot')

        # adding action to the button
        self.button.clicked.connect(self.plot)

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding tool bar to the layout
        # layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        layout.addWidget(self.button)

        # setting layout to the main window
        self.setLayout(layout)

        # Define a list with the input column names.
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

    # action called by the push button
    def plot(self):

        # random data
        # data = [random.random() for i in range(10)]
        df = pd.read_csv('diabetes.csv')

        # Prepare Data
        X = df.drop(columns=['Outcome'])  # Input data
        y = df['Outcome']  # Output data
        neg = X[df['Outcome'] == 0]
        pos = X[df['Outcome'] == 1]

        # clearing old figure
        self.figure.clear()

        for data_point in range(len(self.labels)):

            # create an axis
            ax = self.figure.add_subplot(8, 1, data_point + 1)

        # Define the subplot
        # fig, ax = plt.subplots(
        #     8,
        #     1,
        #     constrained_layout=True,
        #     figsize=(10, 6)
        # )

        # PLot a bar graph that displays all the data.
        # for data_point in range(len(self.labels)):
        #     ax[data_point].barh(1, X[self.labels[data_point]].max(), label="Max Data")
        #     ax[data_point].barh(1, pos[self.labels[data_point]].mean(), label="Has Diabetes Avg")
        #     ax[data_point].barh(1, neg[self.labels[data_point]].mean(), label="Doesn't Have Diabetes Avg")
        #     ax[data_point].barh(1, X[self.labels[data_point]].min(), label="Min Data")
        #     ax[data_point].set_title(self.labels[data_point])
        #     ax[data_point].tick_params(left=False, labelleft=False)  # Remove y-axis tick marks and labels

            print('Showing the bar graph plot.')
        # plt.legend()
        # plt.show()

            # plot data
            ax.barh(1, X[self.labels[data_point]].mean())

            # refresh canvas
            self.canvas.draw()


# driver code
if __name__ == '__main__':
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Window()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())
