import sys
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import plot_data
import matplotlib.pyplot as plt
from process_and_train_data import ProcessAndTrainData


class PlotData(QWidget):

    def __init__(self):
        super().__init__()

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

        # Define the window title
        self.setWindowTitle('Plot')

        # Define the window geometry
        self.setGeometry(0, 0, 1000, 600)

        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure' it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # Just some button connected to 'plot' method
        self.bar_graph_button = QPushButton('Bar Graph')

        # adding action to the button
        self.bar_graph_button.clicked.connect(self.bar_graph)

        # Just some button connected to 'plot' method
        self.scatter_plot_button = QPushButton('Scatter Plot')

        # adding action to the button
        self.scatter_plot_button.clicked.connect(self.scatter_plot)

        # Dropdown menu to select which scatter plot tp display
        self.scatter_plot_dropdown = QComboBox()

        # Adding items to the dropdown(ComboBox)
        self.scatter_plot_dropdown.addItems(self.labels)

        self.loading_label = QLabel()

        # Just some button connected to 'plot' method
        self.close_plot_window_button = QPushButton('Close Window')

        # adding action to the button
        self.close_plot_window_button.clicked.connect(self.close)

        # Vertical layout (Widgets are stacked vertically)
        plot_window_layout = QVBoxLayout()

        # Horizontal layout (Widgets are stacked horizontally)
        plot_selection_layout = QHBoxLayout()

        # self.plot_label = QLabel('Plot')
        # plot_window_layout.addWidget(self.plot_label)

        # adding canvas to the layout
        plot_window_layout.addWidget(self.canvas)

        self.canvas.

        # adding push button to the layout
        plot_selection_layout.addWidget(self.bar_graph_button)

        # adding push button to the layout
        plot_selection_layout.addWidget(self.scatter_plot_button)

        # Adding a dropdown(combobox)
        plot_selection_layout.addWidget(self.scatter_plot_dropdown)

        # Adding the horizontal layout to the vertical layout
        plot_window_layout.addLayout(plot_selection_layout)

        plot_window_layout.addWidget(self.close_plot_window_button)

        self.setLayout(plot_window_layout)

    def bar_graph(self):

        ptd = ProcessAndTrainData()
        data_frame = ptd.load_data('diabetes.csv')
        X, y, neg, pos = ptd.prepare_data(data_frame)

        # Clearing old figure
        self.figure.clear()

        # Plot a bar graph that displays all the data.
        for data_point in range(len(self.labels)):

            # Create an axis
            ax = self.figure.add_subplot(8, 1, data_point + 1)

            # Plot data
            ax.barh(1, X[self.labels[data_point]].max(), label="Max Data")
            ax.barh(1, pos[self.labels[data_point]].mean(), label="Has Diabetes Avg")
            ax.barh(1, neg[self.labels[data_point]].mean(), label="Doesn't Have Diabetes Avg")
            ax.barh(1, X[self.labels[data_point]].min(), label="Min Data")
            ax.set_title(self.labels[data_point])
            ax.tick_params(left=False, labelleft=False)  # Remove y-axis tick marks and labels

            print(f'Displaying {self.labels[data_point]} now')

        # Display the legend
        self.figure.legend()

        # Draw the graph on the canvas
        self.canvas.draw()

    def scatter_plot(self):

        ptd = ProcessAndTrainData()
        data_frame = ptd.load_data('diabetes.csv')

        # Clearing old figure
        self.figure.clear()

        ax = self.figure.add_subplot(1, 1, 1)

        ax.clear()

        column_index = self.scatter_plot_dropdown.currentIndex()

        print(f'\n\nStarting to process the {self.labels[column_index]} column')

        zero_count = 0

        # PLot each data point in the column.
        for data_point in range(len(data_frame.to_numpy())):
            print(column_index, data_point)

            # Plot the data points in green when the patient doesn't have diabetes and red then they do.
            if data_frame.to_numpy()[data_point][8] == 0:  # Does not have diabetes.
                color = 'green'
            else:  # Has diabetes.
                color = 'red'

            # Remove the data points with a 0 value in all columns, EXCEPT pregnancies.
            if data_frame.to_numpy()[data_point][column_index] > 0 and column_index > 0:
                ax.scatter(data_frame.to_numpy()[data_point][column_index], data_point, color=color)
                zero_count += 1

            # Plot all pregnancy data.
            elif column_index == 0:
                ax.scatter(data_frame.to_numpy()[data_point][column_index], data_point, color=color)
                zero_count = len(data_frame.to_numpy())

        print(f'Showing the {self.labels[column_index]} plot. ({len(data_frame.to_numpy()) - zero_count}'
              ' zero points have been dropped)')
        # ax.legend(['Has diabetes', 'Does not have diabetes'], loc='upper right')
        # ax.title(self.labels[column_index])
        # ax.yticks([])  # Remove the y-axis tick marks
        # print(f'Showing the {self.labels[column]} graph now...')
        ax.set_title(self.labels[column_index])
        ax.tick_params(left=False, labelleft=False)  # Remove y-axis tick marks and labels

        self.canvas.draw()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        widget_width = 150
        pos_x = 125
        # pd = PlotData()

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

    # Create the instance of our Window
    window = MainWindow()

    # Start the app
    sys.exit(App.exec_())
