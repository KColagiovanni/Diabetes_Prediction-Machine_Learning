import matplotlib.pyplot as plt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from process_and_train_data import ProcessAndTrainData


class PlotData(QWidget):

    def __init__(self, data_frame):
        super().__init__()

        self.data_frame = data_frame

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
        self.setGeometry(100, 100, 1000, 650)

        self.figure = plt.figure(figsize=(900, 500), layout='constrained')

        # Canvas Widget that displays the 'figure'
        self.canvas = FigureCanvas(self.figure)

        # Vertical layout (Widgets are stacked vertically)
        plot_window_layout = QVBoxLayout()

        # Horizontal layout (Widgets are stacked horizontally)
        plot_selection_layout = QHBoxLayout()

        # Define group box
        scatter_plot_groupbox = QGroupBox()
        scatter_plot_groupbox.setFixedWidth(630)
        # scatter_plot_groupbox.setAlignment(Qt.AlignHCenter)  # Center groupbox text

        # Define the window buttons
        self.bar_graph_button = QPushButton('Show Bar Graph')
        self.scatter_plot_button = QPushButton('Show Scatter Plot')
        self.close_plot_window_button = QPushButton('Close Window')

        # Adding action to the buttons
        self.bar_graph_button.clicked.connect(self.bar_graph)
        self.scatter_plot_button.clicked.connect(self.scatter_plot)
        self.close_plot_window_button.clicked.connect(self.close)

        # Dropdown menu to select which scatter plot tp display
        self.scatter_plot_dropdown = QComboBox(self)

        # Adding items to the dropdown(ComboBox)
        self.scatter_plot_dropdown.addItems(self.labels)

        # Defining a label for the dropdown(ComboBox)
        self.scatter_plot_label = QLabel('Scatter Plot Selection')
        self.scatter_plot_label.setAlignment(Qt.AlignHCenter)

        # Define progress bar
        self.progress_bar = QProgressBar(self)

        # Setting button width
        self.scatter_plot_dropdown.setFixedWidth(210)
        self.bar_graph_button.setFixedHeight(45)
        self.scatter_plot_button.setFixedHeight(45)
        self.close_plot_window_button.setFixedHeight(45)

        # Adding widgets to the plot selection horizontal layout
        plot_selection_layout.addWidget(self.bar_graph_button)
        plot_selection_layout.addWidget(scatter_plot_groupbox)

        # Adding and defining layouts
        scatter_plot_groupbox_layout = QGridLayout()
        scatter_plot_groupbox.setLayout(scatter_plot_groupbox_layout)

        scatter_plot_groupbox_layout.addWidget(self.scatter_plot_button, 0, 0, 2, 1)
        scatter_plot_groupbox_layout.addWidget(self.scatter_plot_label, 0, 1)
        scatter_plot_groupbox_layout.addWidget(self.scatter_plot_dropdown, 1, 1)

        # Adding widgets to the plot window vertical layout
        plot_window_layout.addWidget(self.canvas)
        plot_window_layout.addWidget(self.progress_bar)
        plot_window_layout.addLayout(plot_selection_layout)  # Adding the horizontal layout to the vertical layout
        plot_window_layout.addWidget(self.close_plot_window_button)

        # Setting the layout
        self.setLayout(plot_window_layout)

    def bar_graph(self):

        ptd = ProcessAndTrainData(self.data_frame)
        # ptd.X, y, neg, pos = ptd.prepare_data()

        # Clearing figure so current one can be displayed
        self.figure.clear()

        # Plot a bar graph that displays all the data.
        for data_point in range(len(self.labels)):

            progress_status = int(((data_point + 1) / len(self.labels)) * 100)
            self.progress_bar.setValue(progress_status)
            self.progress_bar.setFormat(f'Processing Data: {progress_status + int(100 / len(self.labels)) + 1}%')
            print(f'Bar Graph Loading Progress: {progress_status}%')

            # Create an axis
            ax = self.figure.add_subplot(8, 1, data_point + 1)

            # Plot data
            ax.barh(1, ptd.X[self.labels[data_point]].max(), color='red')
            ax.barh(1, ptd.pos[self.labels[data_point]].mean(), color='blue')
            ax.barh(1, ptd.neg[self.labels[data_point]].mean(), color='orange')
            ax.barh(1, ptd.X[self.labels[data_point]].min(), color='green')
            ax.set_title(self.labels[data_point], loc='left')
            ax.tick_params(left=False, labelleft=False)  # Remove y-axis tick marks and labels

        # Display the legend
        self.figure.legend(['Max Values', 'Diabetes Avg', 'Non-Diabetes Avg', 'Min Values'])

        # Draw the graph on the canvas
        self.canvas.draw()
        self.progress_bar.reset()

    def scatter_plot(self):

        # Clearing old figure
        self.figure.clear()

        ax = self.figure.add_subplot(1, 1, 1)

        ax.clear()

        column_index = self.scatter_plot_dropdown.currentIndex()

        print(f'\n\nStarting to process the {self.labels[column_index]} column')

        zero_count = 0

        # PLot each data point in the column.
        for data_point in range(len(self.data_frame.to_numpy())):
            # print(column_index, data_point)

            progress_status = int(((data_point + 1) / len(self.data_frame.to_numpy())) * 100)

            if progress_status <= 100:
                # self.stacked_layout_for_scatter_plot_button_and_progress_bar.setCurrentIndex(1)
                print(
                    f'Scatter Plot Loading Progress: {int(((data_point + 1) / len(self.data_frame.to_numpy())) * 100)}%'
                )
                # self.scatter_plot_button.setText(
                #     f'Loading Plot: {int(((data_point + 1) / len(data_frame.to_numpy())) * 100)}%'
                # )
                self.progress_bar.setValue(progress_status)
                self.progress_bar.setFormat(f'Processing Data: {progress_status + 1}%')

            # Plot the data points in green when the patient doesn't have diabetes and red then they do.
            if self.data_frame.to_numpy()[data_point][8] == 0:  # Does not have diabetes.
                color = 'green'
            else:  # Has diabetes.
                color = 'red'

            # Remove the data points with a 0 value in all columns, EXCEPT pregnancies.
            if self.data_frame.to_numpy()[data_point][column_index] > 0 and column_index > 0:
                ax.scatter(self.data_frame.to_numpy()[data_point][column_index], data_point, color=color)
                zero_count += 1

            # Plot all pregnancy data.
            elif column_index == 0:
                ax.scatter(self.data_frame.to_numpy()[data_point][column_index], data_point, color=color)
                zero_count = len(self.data_frame.to_numpy())

        # self.stacked_layout_for_scatter_plot_button_and_progress_bar.setCurrentIndex(0)
        self.scatter_plot_button.setText('Scatter Plot')
        print(f'Showing the {self.labels[column_index]} plot. ({len(self.data_frame.to_numpy()) - zero_count}'
              ' zero points have been dropped)')
        ax.legend(['Has diabetes', 'Does not have diabetes'], loc='upper right')
        # ax.title(self.labels[column_index])
        # ax.yticks([])  # Remove the y-axis tick marks
        # print(f'Showing the {self.labels[column]} graph now...')
        ax.set_title(self.labels[column_index])
        ax.tick_params(left=False, labelleft=False)  # Remove y-axis tick marks and labels

        self.canvas.draw()
        self.progress_bar.reset()
