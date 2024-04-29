import matplotlib.pyplot as plt


class PlotData:

    def __init__(self):

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

    def bar_graph(self, X, neg, pos):
        # Define the subplot
        fig, ax = plt.subplots(
            8,
            1,
            constrained_layout=True,
            figsize=(10, 6)
        )

        # PLot a bar graph that displays all the data.
        for data_point in range(len(self.labels)):
            ax[data_point].barh(1, X[self.labels[data_point]].max(), label="Max Data")
            ax[data_point].barh(1, pos[self.labels[data_point]].mean(), label="Has Diabetes Avg")
            ax[data_point].barh(1, neg[self.labels[data_point]].mean(), label="Doesn't Have Diabetes Avg")
            ax[data_point].barh(1, X[self.labels[data_point]].min(), label="Min Data")
            ax[data_point].set_title(self.labels[data_point])
            ax[data_point].tick_params(left=False, labelleft=False)  # Remove y-axis tick marks and labels

        print('Showing the bar graph plot.')
        plt.legend()
        # plt.show()
        return plt


    def scatter_plot(self, data_frame):
        # Generate a scatter plot for each input data column.
        for column in range(len(self.labels)):        # pw.show()


            zero_count = 0

            # PLot each data point in the column.
            for data_point in range(len(data_frame.to_numpy())):

                # Plot the data points in green when the patient doesn't have diabetes and red then they do.
                if data_frame.to_numpy()[data_point][8] == 0:  # Does not have diabetes.
                    color = 'green'
                else:  # Has diabetes.
                    color = 'red'
                # Remove the data points with a 0 value in all columns, EXCEPT pregnancies.
                if data_frame.to_numpy()[data_point][column] > 0 and column > 0:
                    plt.scatter(data_frame.to_numpy()[data_point][column], data_point, color=color)
                    zero_count += 1

                # Plot all pregnancy data.
                elif column == 0:
                    plt.scatter(data_frame.to_numpy()[data_point][column], data_point, color=color)

            if self.labels[column] == 'Pregnancies':
                zero_count = len(data_frame.to_numpy())

            print(
                f'Showing the {self.labels[column]} plot. ({len(data_frame.to_numpy()) - zero_count} zero points have been dropped)')
            plt.legend(['Has diabetes', 'Does not have diabetes'], loc='upper right')
            plt.title(self.labels[column])
            plt.yticks([])  # Remove the y-axis tick marks
            plt.show()
