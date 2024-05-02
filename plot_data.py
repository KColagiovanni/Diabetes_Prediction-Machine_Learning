import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *
import sys


class PlotData(QDialog):

    def __init__(self):

        super().__init__()

        print('In PlotData __init__()')

        # Define the window title
        self.setWindowTitle('Plot')

        # Define the window geometry
        self.setGeometry(0, 0, 600, 600)

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

        plot_window_layout = QVBoxLayout()

        # self.plot_label = QLabel('Plot')
        # plot_window_layout.addWidget(self.plot_label)

        # adding canvas to the layout
        plot_window_layout.addWidget(self.canvas)

        # adding push button to the layout
        plot_window_layout.addWidget(self.bar_graph_button)

        # adding push button to the layout
        plot_window_layout.addWidget(self.scatter_plot_button)

        self.setLayout(plot_window_layout)

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

    def bar_graph(self, X, y, neg, pos):

        print('In bar_graph()')

        # Define the subplot
        # fig, ax = plt.subplots(
        #     8,
        #     1,
        #     constrained_layout=True,
        #     figsize=(10, 6)
        # )

        # PLot a bar graph that displays all the data.
        # for data_point in range(len(self.labels)):
        # clearing old figure
        self.figure.clear()

        for data_point in range(len(self.labels)):

            # create an axis
            ax = self.figure.add_subplot(8, 1, data_point + 1)

            # plot data
            # ax.barh(1, X[self.labels[data_point]].max())
            # ax.barh(1, pos[self.labels[data_point]].mean())
            # ax.barh(1, neg[self.labels[data_point]].mean())
            ax.barh(1, X[self.labels[data_point]].min())

            print(f'Displaying {self.labels[data_point]} now')

            # refresh canvas
            self.canvas.draw()

            # ax[data_point].barh(1, X[self.labels[data_point]].max(), label="Max Data")
            # ax[data_point].barh(1, pos[self.labels[data_point]].mean(), label="Has Diabetes Avg")
            # ax[data_point].barh(1, neg[self.labels[data_point]].mean(), label="Doesn't Have Diabetes Avg")
            # ax[data_point].barh(1, X[self.labels[data_point]].min(), label="Min Data")
            # ax[data_point].set_title(self.labels[data_point])
            # ax[data_point].tick_params(left=False, labelleft=False)  # Remove y-axis tick marks and labels

        # print('Showing the bar graph plot.')
        # plt.legend()
        # plt.show()

        # _-_-_-_-_-_-_-_-_-_-_-_-_-_ Testing to display the plot in a new window _-_-_-_-_-_-_-_-_-_-_-_-_-_
        # data = X['Pregnancies'].to_numpy()
        #
        # print(data)
        #
        # self.figure.clear()
        #
        # ax = self.figure.subplots(
        #     8,
        #     1,
        #     # constrained_layout=True,
        #     # figsize=(10, 6)
        # )
        #
        # ax = self.figure.add_subplot(111)
        #
        # ax.plot(data, '*-')
        #
        # self.canvas.draw()
        # _-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-__-_-_-_-_-_-_-_-_


    def scatter_plot(self, data_frame):

        # print(data_frame['Pregnancies'], data_frame['Pregnancies'].shape)
        plt.plot(data_frame['Pregnancies'])
        plt.show()

        # # Generate a scatter plot for each input data column.
        # for column in range(len(self.labels)):
        #     print(f'\n\nStarting to process the {self.labels[column]} column')
        #
        #     zero_count = 0
        #
        #     # PLot each data point in the column.
        #     for data_point in range(len(data_frame.to_numpy())):
        #
        #         # Plot the data points in green when the patient doesn't have diabetes and red then they do.
        #         if data_frame.to_numpy()[data_point][8] == 0:  # Does not have diabetes.
        #             color = 'green'
        #         else:  # Has diabetes.
        #             color = 'red'
        #
        #         # Remove the data points with a 0 value in all columns, EXCEPT pregnancies.
        #         if data_frame.to_numpy()[data_point][column] > 0 and column > 0:
        #             plt.scatter(data_frame.to_numpy()[data_point][column], data_point, color=color)
        #             zero_count += 1
        #
        #         # Plot all pregnancy data.
        #         elif column == 0:
        #             plt.scatter(data_frame.to_numpy()[data_point][column], data_point, color=color)
        #             zero_count = len(data_frame.to_numpy())
        #
        #     print(f'Showing the {self.labels[column]} plot. ({len(data_frame.to_numpy()) - zero_count}'
        #           ' zero points have been dropped)')
        #     # plt.legend(['Has diabetes', 'Does not have diabetes'], loc='upper right')
        #     # plt.title(self.labels[column])
        #     # plt.yticks([])  # Remove the y-axis tick marks
        #     print(f'Showing the {self.labels[column]} graph now...')
        #     plt.show()


# driver code
if __name__ == '__main__':

    # Create PyQt5 app
    App = QApplication(sys.argv)

    # Create the instance of our Window
    window = PlotData()

    window.show()

    # Start the app
    sys.exit(App.exec_())

# class PlotWindow(QWidget):
#
#
#         self.labels = [
#             'Pregnancies',
#             'Glucose',
#             'BloodPressure',
#             'SkinThickness',
#             'Insulin',
#             'BMI',
#             'DiabetesPedigreeFunction',
#             'Age'
#         ]
#
#     def show_bar_graph(self):
#
#         # self.figure.clear()
#
#         print('\n\nPreparing the bar graph')
#         ptd = ProcessAndTrainData()
#         # pd = PlotData()
#         data_frame = ptd.load_data('diabetes.csv')
#         X, y, neg, pos = ptd.prepare_data(data_frame)
#
#         fig, ax = plt.subplots(
#             8,
#             1,
#             constrained_layout=True,
#             figsize=(10, 6)
#         )
#
#         # PLot a bar graph that displays all the data.
#         for data_point in range(len(self.labels)):
#             ax[data_point].barh(1, X[self.labels[data_point]].max(), label="Max Data")
#             ax[data_point].barh(1, pos[self.labels[data_point]].mean(), label="Has Diabetes Avg")
#             ax[data_point].barh(1, neg[self.labels[data_point]].mean(), label="Doesn't Have Diabetes Avg")
#             ax[data_point].barh(1, X[self.labels[data_point]].min(), label="Min Data")
#             ax[data_point].set_title(self.labels[data_point])
#             ax[data_point].tick_params(left=False, labelleft=False)  # Remove y-axis tick marks and labels
#
#         print('Showing the bar graph plot.')
#         plt.legend()
#         plt.show()
#
#         # bg = pd.bar_graph(X, neg, pos)
#         # bg.show()
#
#         # # # create an axis
#         # ax = self.figure.add_subplot(111)
#
#         # plot data
#         # ax.barh(bg)
#
#         # refresh canvas
#         # self.canvas.draw()
#
#     def show_scatter_plots(self):
#         print('Preparing the scatter plots')
#         ptd = ProcessAndTrainData()
#         pd = PlotData()
#         data_frame = ptd.load_data('diabetes.csv')
#         pd.scatter_plot(data_frame)
