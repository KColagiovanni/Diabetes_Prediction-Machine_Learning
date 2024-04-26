# Video Source: https://www.youtube.com/watch?v=7eh4d6sabA0&t=345s
# Linear Regression video: https://www.youtube.com/watch?v=lGg0LNZplVQ

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score
from sklearn.linear_model import LinearRegression
import joblib
from sklearn import tree


should_be_diabetic = [7, 150, 70, 35, 0, 35, 1, 50]
should_not_be_diabetic = [1, 99, 62, 0, 0, 27, .24, 24]


df = pd.read_csv('diabetes.csv')

# Prepare Data
X = df.drop(columns=['Outcome'])  # Input data
y = df['Outcome']  # Output data
neg = X[df['Outcome'] == 0]
pos = X[df['Outcome'] == 1]

print(f'Min Values: {X.min().to_numpy()}')
print(f'Avg Neg Values: {neg.mean().to_numpy()}')
print(f'Avg Pos Values: {pos.mean().to_numpy()}')
print(f'Max Values: {X.max().to_numpy()}')

# Split the data set into two random sets, one for training, one for testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Leaning and Predicting (Using Decision Tree)

# Define the data model
model = DecisionTreeClassifier()
# model = LinearRegression()
# model.fit(X, y)  # Train the model with csv data set
model.fit(X_train, y_train)  # Train the model with training data set
prediction = model.predict(X_test)  # Ask for a prediction with test data set
# prediction = model.predict([should_be_diabetic, should_not_be_diabetic])

# Calculating the Accuracy Score
ac_score = accuracy_score(y_test, prediction)

# Evaluate the performance of the model
r2 = r2_score(y_test, prediction)
# mean_sqr_err = mean_squared_error(y_test, prediction)
# mean_abs_err = mean_absolute_error(y_test, prediction)

# Persisting Models
# joblib.dump(model, 'diabetes_predictions.joblib')  # Save a binary file with trained model data

# model = joblib.load('diabetes_predictions.joblib')  # Load a binary file with trained model data
# predictions = model.predict([should_be_diabetic, should_not_be_diabetic])  # Ask for a prediction with defined data from loaded training model

# Visualizing a Data Tree
# tree.export_graphviz(
#     model,
#     out_file='diabetes_results.dot',
#     feature_names=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',  'BMI', 'DiabetesPedigreeFunction', 'Age'],
#     class_names=[str(yY) for yY in sorted(y.unique())],
#     label='all',
#     rounded=True,
#     filled=True
# )

# Dataframe
# print(f'Dataframe:\n{df}')

# Shape
# print(f'\nDF Shape: {df.shape}')

# Describe DF
print(f'\nDescribe DF:\n{X.describe()}')
print(f'\nDescribe neg:\n{neg.describe()}')
print(f'\nDescribe pos:\n{pos.describe()}')

# DF Values
# print(f'\nDF Values:\n{df.values}')

# Print Prepared Data
# print(f'Input Data Frame:\n{X}')

# Print the prediction(s)
print(f'\nPrediction(s):\n{prediction}')

# Model Performance
print(f'\nr2 Score: {r2}')
# print(f'Mean Squared Error: {mean_sqr_err}')
# print(f'Mean Absolute Error: {mean_abs_err}')

# Linear Regression
# print(f'Intercept: {model.intercept_}')
# print(f'Coefficient: {model.coef_}')

# Print the Accuracy Score
print(f'Accuracy Score: {ac_score}')


# ---------- Plot Data ----------
labels = [
    'Pregnancies',
    'Glucose',
    'BloodPressure',
    'SkinThickness',
    'Insulin',
    'BMI',
    'DiabetesPedigreeFunction',
    'Age'
]

fig, ax = plt.subplots(
    8,
    1,
    constrained_layout=True,
    figsize=(10, 6)
    #, height_ratios=[1.5, 1.5,1.5,1.5,1.5,1.5,1.5,1.5])
)

for data_point in range(len(labels)):
    ax[data_point].barh(1, X[labels[data_point]].max(), label="Max Data")
    ax[data_point].barh(1, pos[labels[data_point]].mean(), label="Has Diabetes Avg")
    ax[data_point].barh(1, neg[labels[data_point]].mean(), label="Doesn't Have Diabetes Avg")
    ax[data_point].barh(1, X[labels[data_point]].min(), label="Min Data")
    ax[data_point].set_title(labels[data_point])
    # Remove y-axis tick marks here

plt.legend()
plt.show()

# Scatter Plot CSV Data
# print(len(X['Age'].to_numpy()))
# print(sorted(X['Age'].to_numpy()))
for data_point in range(len(df.to_numpy())):
    # print(df['Outcome'].to_numpy())
    print(df[data_point].to_numpy())
    # if df.to_numpy()[data_point][8] == 0:
    #     color = 'green'
    # else:
    #     color = 'red'
    # plt.scatter(data_point, sorted(df.to_numpy[data_point[7]].to_numpy()), color=color)

# plt.scatter(range(len(X['Age'].to_numpy())), sorted(X['Age'].to_numpy()))
# plt.scatter(range(len(pos['Age'].to_numpy())), pos['Age'].to_numpy())
# plt.scatter(range(len(neg['Age'].to_numpy())), neg['Age'].to_numpy())
# plt.show()