import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error, mean_absolute_error


class ProcessAndTrainData:

    def __init__(self):

        # _-_-_-_-_-_-_-_-_-_-_-_-_ Test Data _-_-_-_-_-_-_-_-_-_-_-_-_
        should_be_diabetic = [7, 150, 70, 35, 0, 35, 1, 50]
        should_not_be_diabetic = [1, 99, 62, 0, 0, 27, .24, 24]

    @staticmethod
    def load_data(csv_data):
        return pd.read_csv(csv_data)

    @staticmethod
    def prepare_data(data_frame):
        # Prepare Data
        X = data_frame.drop(columns=['Outcome'])  # Input data
        neg = X[data_frame['Outcome'] == 0]  # Input data from women who don't have diabetes.
        pos = X[data_frame['Outcome'] == 1]  # Input data from women who do have diabetes.
        y = data_frame['Outcome']  # Output data

        # Print data from data frames
        print(f'Min Values: {X.min().to_numpy()}')
        print(f'Avg Neg Values: {neg.mean().to_numpy()}')
        print(f'Avg Pos Values: {pos.mean().to_numpy()}')
        print(f'Max Values: {X.max().to_numpy()}')

        # Describe DF
        print(f'\nDescribe DF:\n{X.describe()}')
        print(f'\nDescribe neg:\n{neg.describe()}')
        print(f'\nDescribe pos:\n{pos.describe()}')

        return X, y, neg, pos

    @staticmethod
    def train_data(X, y):
        # Split the data set into two random sets, one for training, one for testing.
        return train_test_split(X, y, test_size=0.2)  # returns X_train, X_test, y_train, y_test (in that order)

    @staticmethod
    def predict_data(X_train, X_test, y_train, y_test):

        # print(f'X Train: {X_train}')
        # print(f'y Train: {y_train}')
        # print(f'X Test: {X_test}')
        # print(f'y Test: {y_test}')

        # Define the data model
        model = DecisionTreeClassifier()

        # model.fit(X, y)  # Train the model with csv data set
        model.fit(X_train, y_train)  # Train the model with training data set
        prediction = model.predict(X_test)  # Ask for a prediction with test data set
        # prediction = model.predict([should_be_diabetic, should_not_be_diabetic])

        # Calculating the Accuracy Score
        ac_score = accuracy_score(y_test, prediction)

        # Print the prediction(s)
        print(f'\nPrediction(s):\n{prediction}')

        # Print the Accuracy Score
        print(f'Accuracy Score: {round(ac_score * 100, 2)}%')

        return ac_score
