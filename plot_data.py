import matplotlib.pyplot as plt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from process_and_train_data import ProcessAndTrainData
import numpy as np


class PlotData(QWidget):

    def __init__(self, data_frame):
        super().__init__()

        # Define the data frame
        self.data_frame = data_frame

        # Define dimension variables
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 650
        canvas_width = 900
        canvas_height = 500
        self.graph_button_height = 40

        self.bg_color = 'lightgray'
        self.max_bar_color = 'red'
        self.pos_bar_color = 'orange'
        self.neg_bar_color = 'lightgreen'
        self.min_bar_color = 'lightblue'

        # Data frame columns
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

        # Define the figure
        self.figure = plt.figure(figsize=(canvas_width, canvas_height), layout='constrained')

        # Define the canvas widget that displays the 'figure'
        self.canvas = FigureCanvas(self.figure)

        # Define the window buttons
        self.bar_graph_button = QPushButton('Show Bar Graph')
        self.scatter_plot_button = QPushButton('Show Scatter Plot')
        self.new_plot_button = QPushButton('Show Histogram Graph')
        self.close_plot_window_button = QPushButton('Close Window')

        # Define a checkbox and label to show or hide zero values in plots
        self.hide_zero_values = QCheckBox('Hide data with a value of "0"')

        # Defining a label for the dropdown(ComboBox)

        self.select_a_plot_label = QLabel('Select Data to Plot:')
        self.horizontal_line = QLabel()

        # Define progress bar
        self.progress_bar = QProgressBar(self)

        # Dropdown menu to select which scatter plot tp display
        self.select_plot_dropdown = QComboBox(self)

        self.initialize_user_interface()

    def initialize_user_interface(self):

        # Define the window title
        self.setWindowTitle('Plot')

        # Define the prediction window geometry
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Call the method to
        self.modify_widgets()

        # Vertical layout (Widgets are stacked vertically)
        plot_window_layout = QVBoxLayout()

        # Horizontal layout (Widgets are stacked horizontally)
        plot_selection_layout = QHBoxLayout()

        # Define group box
        plot_groupbox = QGroupBox()
        plot_groupbox.setStyleSheet(f'background-color: {self.bg_color}')

        # Adding widgets to the plot selection horizontal layout
        # plot_selection_layout.addWidget(self.bar_graph_button)
        plot_selection_layout.addWidget(plot_groupbox)

        # Adding and defining layouts
        scatter_plot_groupbox_layout = QGridLayout()
        plot_groupbox.setLayout(scatter_plot_groupbox_layout)

        scatter_plot_groupbox_layout.addWidget(self.select_a_plot_label, 0, 0)
        scatter_plot_groupbox_layout.addWidget(self.select_plot_dropdown, 1, 0)
        scatter_plot_groupbox_layout.addWidget(self.hide_zero_values, 1, 2)
        scatter_plot_groupbox_layout.addWidget(self.horizontal_line, 2, 0, 1, 3)
        scatter_plot_groupbox_layout.addWidget(self.bar_graph_button, 3, 0)
        scatter_plot_groupbox_layout.addWidget(self.scatter_plot_button, 3, 1)
        scatter_plot_groupbox_layout.addWidget(self.new_plot_button, 3, 2)
        scatter_plot_groupbox_layout.addWidget(self.close_plot_window_button, 4, 0, 1, 3)

        # Adding widgets to the plot window vertical layout
        plot_window_layout.addWidget(self.canvas)
        plot_window_layout.addWidget(self.progress_bar)
        plot_window_layout.addLayout(plot_selection_layout)
        # plot_window_layout.addWidget(self.close_plot_window_button)

        # Setting the layout
        self.setLayout(plot_window_layout)

    def modify_widgets(self):

        # Adding action to the buttons
        self.bar_graph_button.clicked.connect(self.bar_graph)
        self.scatter_plot_button.clicked.connect(self.scatter_plot)
        self.new_plot_button.clicked.connect(self.histogram_plot)
        self.close_plot_window_button.clicked.connect(self.close)

        # Adding items to the dropdown(ComboBox)
        self.select_plot_dropdown.addItems(self.labels)

        self.hide_zero_values.setChecked(True)

        # Center the label text
        # self.select_a_plot_label.setAlignment(Qt.AlignHCenter)
        # self.select_a_plot_label.setAlignment(Qt.AlignLeft)
        self.horizontal_line.setFrameStyle(QFrame.HLine)

        # Setting button width
        # self.select_plot_dropdown.setFixedWidth(210)
        self.bar_graph_button.setFixedHeight(self.graph_button_height)
        self.scatter_plot_button.setFixedHeight(self.graph_button_height)
        self.new_plot_button.setFixedHeight(self.graph_button_height)

        self.close_plot_window_button.setFixedHeight(self.graph_button_height)

    def bar_graph(self):

        # ======================================= Original Code ========================================================
        # ptd = ProcessAndTrainData(self.data_frame)
        # # ptd.X, y, neg, pos = ptd.prepare_data()
        #
        # # Clearing figure so current one can be displayed
        # self.figure.clear()
        #
        # # Plot a bar graph that displays all the data.
        # for data_point in range(len(self.labels)):
        #
        #     progress_status = int(((data_point + 1) / len(self.labels)) * 100)
        #     self.progress_bar.setValue(progress_status)
        #     self.progress_bar.setFormat(f'Processing Data: {progress_status + int(100 / len(self.labels)) + 1}%')
        #     print(f'Bar Graph Loading Progress: {progress_status}%')
        #
        #     # Create an axis
        #     ax = self.figure.add_subplot(8, 1, data_point + 1)
        #
        #     # Plot data
        #     ax.barh(1, ptd.X[self.labels[data_point]].max(), color='red')
        #     ax.barh(1, ptd.pos[self.labels[data_point]].mean(), color='blue')
        #     ax.barh(1, ptd.neg[self.labels[data_point]].mean(), color='orange')
        #     ax.barh(1, ptd.X[self.labels[data_point]].min(), color='green')
        #     ax.set_title(self.labels[data_point], loc='left')
        #     ax.tick_params(left=False, labelleft=False)  # Remove y-axis tick marks and labels
        #
        # # Display the legend
        # self.figure.legend(['Max Values', 'Diabetes Avg', 'Non-Diabetes Avg', 'Min Values'])
        #
        # # Draw the graph on the canvas
        # self.canvas.draw()
        # self.progress_bar.reset()
        #
        # ==============================================================================================================

        # ========================================== New Code ==========================================================

        # def addlabels(x, y):
        #     for i in range(len(x)):
        #         plt.text(i, y[i], y[i], ha='center')

        ptd = ProcessAndTrainData(self.data_frame)

        # Clearing figure so current one can be displayed
        self.figure.clear()

        # Create an axis
        ax = self.figure.add_subplot(1, 1, 1)

        column_index = self.select_plot_dropdown.currentIndex()


        X_max = ptd.X[self.labels[column_index]].max()
        X_min = ptd.X[self.labels[column_index]].min()
        neg_avg = ptd.neg[self.labels[column_index]].mean()
        pos_avg = ptd.pos[self.labels[column_index]].mean()

        if self.labels[column_index] == 'BMI':
            X_max = round(X_max, 1)
            pos_avg = round(pos_avg, 1)
            neg_avg = round(neg_avg, 1)
            X_min = round(X_min, 1)
        elif self.labels[column_index] == 'DiabetesPedigreeFunction':
            X_max = round(X_max, 2)
            pos_avg = round(pos_avg, 2)
            neg_avg = round(neg_avg, 2)
            X_min = round(X_min, 2)
        else:
            X_max = int(X_max)
            pos_avg = int(pos_avg)
            neg_avg = int(neg_avg)
            X_min = int(X_min)

        # Plot data
        ax.bar(1, X_max, color=self.max_bar_color, width=1)
        ax.text(1, X_max / 2, str(X_max), ha='center')

        ax.bar(2, pos_avg, color=self.pos_bar_color, width=1)
        ax.text(2, pos_avg / 2, str(pos_avg), ha='center')

        ax.bar(3, neg_avg, color=self.neg_bar_color, width=1)
        ax.text(3, neg_avg / 2, str(neg_avg), ha='center')

        ax.bar(4, X_min, color=self.min_bar_color, width=1)
        if X_min < 0.1:
            ax.text(4, X_min, str(X_min), ha='center')
        else:
            ax.text(4, X_min / 2, str(X_min), ha='center')

        ax.set_title(self.labels[column_index], loc='center')
        ax.tick_params(bottom=False, labelbottom=False)  # Remove x-axis tick marks and labels

        # Display the legend
        self.figure.legend(['Max Values', 'Has Diabetes Avg', 'Doesn\'t Have Diabetes Avg', 'Min Values'])

        # Draw the graph on the canvas
        self.canvas.draw()

        # ==============================================================================================================

    def scatter_plot(self):

        zero_count = 0
        percent_dropped = 0
        column_index = self.select_plot_dropdown.currentIndex()
        min_data_frame_value = self.data_frame[self.labels[column_index]].max()

        # Clearing old figure
        self.figure.clear()

        ax = self.figure.add_subplot(1, 1, 1)

        ax.clear()

        print(f'\n\nStarting to process the {self.labels[column_index]} column')

        # Filter and plot each data point in the column.
        for data_point in range(len(self.data_frame.to_numpy())):

            # Progress bar
            progress_status = int(((data_point + 1) / self.data_frame.shape[0]) * 100)
            if progress_status <= 100:
                print(
                    f'Scatter Plot Loading Progress: {int(((data_point + 1) / len(self.data_frame.to_numpy())) * 100)}%'
                )
                self.progress_bar.setValue(progress_status)
                self.progress_bar.setFormat(f'Processing Data: {progress_status + 1}%')

            # Plot the data points in green when the patient doesn't have diabetes and red then they do.
            if self.data_frame.to_numpy()[data_point][8] == 0:  # Does not have diabetes.
                color = 'green'
            else:  # Has diabetes.
                color = 'red'

            # # Hide the zero values in all columns, EXCEPT pregnancies if user selected checkbox.
            # if self.show_data_with_zero_values.isChecked():
            #
            # Remove the data points with a 0 value in all columns, EXCEPT pregnancies.
            # if self.data_frame.to_numpy()[data_point][column_index] > 0 and self.labels[column_index] != 'Pregnancies':
            if self.labels[column_index] != 'Pregnancies':

                if self.hide_zero_values.isChecked():
                    if self.data_frame.to_numpy()[data_point][column_index] > 0:

                        # Determining the min value for the data frame
                        if self.data_frame.to_numpy()[data_point][column_index] < min_data_frame_value:
                            min_data_frame_value = self.data_frame.to_numpy()[data_point][column_index]
                        else:
                            self.data_frame.to_numpy()[data_point][column_index] = min_data_frame_value

                        # Calculating the steps to the x-axis ticks
                        if self.labels[column_index] == 'BMI':
                            steps = round(
                                (self.data_frame[self.labels[column_index]].max() - min_data_frame_value) / 10, 1)
                        elif self.labels[column_index] == 'DiabetesPedigreeFunction':
                            steps = round(
                                (self.data_frame[self.labels[column_index]].max() - min_data_frame_value) / 10, 2)
                        else:
                            steps = (self.data_frame[self.labels[column_index]].max() - min_data_frame_value) // 10

                        ax.scatter(self.data_frame.to_numpy()[data_point][column_index], data_point, color=color)
                        ax.xaxis.set_ticks(np.arange(min_data_frame_value, self.data_frame[self.labels[column_index]].max(), steps))

                        zero_count += 1
                else:
                    # Determining the min value for the data frame
                    if self.data_frame.to_numpy()[data_point][column_index] < min_data_frame_value:
                        min_data_frame_value = self.data_frame.to_numpy()[data_point][column_index]
                    else:
                        self.data_frame.to_numpy()[data_point][column_index] = min_data_frame_value

                    # Calculating the steps to the x-axis ticks
                    if self.labels[column_index] == 'BMI':
                        steps = round((self.data_frame[self.labels[column_index]].max() - min_data_frame_value) / 10, 1)
                    elif self.labels[column_index] == 'DiabetesPedigreeFunction':
                        steps = round((self.data_frame[self.labels[column_index]].max() - min_data_frame_value) / 10, 2)
                    else:
                        steps = (self.data_frame[self.labels[column_index]].max() - min_data_frame_value) // 10

                    ax.scatter(self.data_frame.to_numpy()[data_point][column_index], data_point, color=color)
                    ax.xaxis.set_ticks(
                        np.arange(min_data_frame_value, self.data_frame[self.labels[column_index]].max(), steps)
                    )

                percent_dropped = round((self.data_frame.shape[0] - zero_count) / self.data_frame.shape[0] * 100, 1)

            # Plot all pregnancy data.
            if self.labels[column_index] == 'Pregnancies':
                ax.scatter(self.data_frame.to_numpy()[data_point][column_index], data_point, color=color)
                ax.xaxis.set_ticks(np.arange(0, 18, 1))
                zero_count = self.data_frame.shape[0]
                percent_dropped = 0


        print(f'Showing the {self.labels[column_index]} plot. ({self.data_frame.shape[0] - zero_count}'
              f' zero points have been dropped({percent_dropped}%))')
        ax.legend(['Has diabetes', 'Does not have diabetes'], loc='upper right')
        ax.set_title(self.labels[column_index])
        ax.tick_params(left=False, labelleft=False)  # Remove y-axis tick marks and labels

        self.canvas.draw()
        self.progress_bar.reset()

    def histogram_plot(self):

        # Clearing old figure
        self.figure.clear()

        ax = self.figure.add_subplot(1, 1, 1)

        ax.clear()

        column_index = self.select_plot_dropdown.currentIndex()

        print(f'\n\nStarting to process the {self.labels[column_index]} column')

        ax.set_title(self.labels[column_index])

        # # Hide the zero values in all columns, EXCEPT pregnancies if user selected checkbox.
        # if self.show_data_with_zero_values.isChecked():
        #
        # Drop all zero values in every column, except for the pregnancy column. Also define # of bins and x ticks.
        if self.labels[column_index] == 'Pregnancies':
            bins = 17
            no_zeros_data_frame = self.data_frame[self.labels[column_index]]
            ax.xaxis.set_ticks(np.arange(0, bins, 1))

        elif self.hide_zero_values.isChecked():
            bins = 20
            no_zeros_data_frame = self.data_frame[
                self.labels[column_index]][self.data_frame[self.labels[column_index]] != 0]

        else:
            bins = 20
            no_zeros_data_frame = self.data_frame[self.labels[column_index]]

        if self.labels[column_index] == 'BMI':
            steps = round(((no_zeros_data_frame.max() - no_zeros_data_frame.min()) / 10), 1)
        elif self.labels[column_index] == 'DiabetesPedigreeFunction':
            steps = round(((no_zeros_data_frame.max() - no_zeros_data_frame.min()) / 10), 2)
        else:
            steps = (no_zeros_data_frame.max() - no_zeros_data_frame.min()) // 10

        ax.xaxis.set_ticks(np.arange(round(no_zeros_data_frame.min(), 2), no_zeros_data_frame.max(), steps))
        ax.hist(no_zeros_data_frame.to_numpy(), bins=bins)

        self.canvas.draw()
        # self.progress_bar.reset()
