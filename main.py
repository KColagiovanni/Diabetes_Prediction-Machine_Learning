# Video Source: https://www.youtube.com/watch?v=7eh4d6sabA0&t=345s


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
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

# Split the data set into two random sets, one for training, one for testing.
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Leaning and Predicting (Using Decision Tree)
model = DecisionTreeClassifier()  # Define the data model
model.fit(X, y)  # Train the model with training data set
# model.fit(X_train, y_train)  # Train the model with training data set
# predictions = model.predict(X_test)  # Ask for a prediction with test data set
# predictions = model.predict([should_be_diabetic, should_not_be_diabetic])

# Calculating the Accuracy
# ac_score = accuracy_score(y_test, predictions)

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

# print(f'\nDataframe Averages:\n {df.mean()}')
# print(f'\nNegative Averages:\n {neg.mean()}')
# print(f'\nPositive Averages:\n {pos.mean()}')


# DF Values
# print(f'\nDF Values:\n{df.values}')


# Print Prepared Data
# print(f'Input Data Frame:\n{X}')


# Print the prediction(s)
# print(f'Prediction(s): {predictions}')


# Print the Accuracy Score
# print(f'Accuracy Score: {ac_score}')


# ---------- Plot Data ----------
labels = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',  'BMI', 'DiabetesPedigreeFunction', 'Age']
# plt.title('Diabetic vs Non-Diabetic Mean Values')
fig, ax = plt.subplots(8, 1)

# Pregnancies
ax[0].barh(1, pos['Pregnancies'].mean())
ax[0].barh(1, neg['Pregnancies'].mean())
# plt.subplot(8, 1, 1)
# plt.barh(1, pos['Pregnancies'].mean())
# plt.barh(1, neg['Pregnancies'].mean())
ax[0].set_title(labels[0])
# ax[0].yticks(ticks=[])

# # Glucose
# plt.subplot(8, 1, 2)
# plt.barh(1, pos['Glucose'].mean())
# plt.barh(1, neg['Glucose'].mean())
# plt.ylabel(labels[1])
# plt.yticks(ticks=[])
#
# # Blood Pressure
# plt.subplot(8, 1, 3)
# plt.barh(1, pos['BloodPressure'].mean())
# plt.barh(1, neg['BloodPressure'].mean())
# plt.ylabel(labels[2])
# plt.yticks(ticks=[])
#
# # Skin Thickness
# plt.subplot(8, 1, 4)
# plt.barh(1, pos['SkinThickness'].mean())
# plt.barh(1, neg['SkinThickness'].mean())
# plt.ylabel(labels[3])
# plt.yticks(ticks=[])
#
# # Insulin
# plt.subplot(8, 1, 5)
# plt.barh(1, pos['Insulin'].mean())
# plt.barh(1, neg['Insulin'].mean())
# plt.ylabel(labels[4])
# plt.yticks(ticks=[])
#
# # BMI
# plt.subplot(8, 1, 6)
# plt.barh(1, pos['BMI'].mean())
# plt.barh(1, neg['BMI'].mean())
# plt.ylabel(labels[5])
# plt.yticks(ticks=[])
#
# # 'Diabetes Pedigree Function'
# plt.subplot(8, 1, 7)
# plt.barh(1, pos['DiabetesPedigreeFunction'].mean())
# plt.barh(1, neg['DiabetesPedigreeFunction'].mean())
# plt.ylabel(labels[6])
# plt.yticks(ticks=[])
#
# # Age
# plt.subplot(8, 1, 8)
# plt.barh(1, pos['Age'].mean())
# plt.barh(1, neg['Age'].mean())
# plt.ylabel(labels[7])
# plt.yticks(ticks=[])

plt.xticks(ticks=[])
plt.yticks(ticks=[])
plt.show()
