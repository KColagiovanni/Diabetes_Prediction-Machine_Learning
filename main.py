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
print(f'\nDescribe DF:\n{df.describe()}')


print(f'\nNegative Results:\n {neg.mean()}')
print(f'\nPositive Results:\n {pos.mean()}')


# DF Values
# print(f'\nDF Values:\n{df.values}')


# Print Prepared Data
# print(f'Input Data Frame:\n{X}')


# Print the prediction(s)
# print(f'Prediction(s): {predictions}')


# Print the Accuracy Score
# print(f'Accuracy Score: {ac_score}')


labels = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',  'BMI', 'DiabetesPedigreeFunction', 'Age']
#---------- Plot Data ----------


# Pregnancies
plt.subplot(8, 1, 1)
plt.barh(1, pos['Pregnancies'].mean())
plt.barh(1, neg['Pregnancies'].mean())
plt.ylabel(labels[0])
plt.yticks(ticks=[])


# Glucose
plt.subplot(8, 1, 2)
plt.barh(1, pos['Glucose'].mean())
plt.barh(1, neg['Glucose'].mean())


# Blood Pressure
plt.subplot(8, 1, 3)
plt.barh(1, pos['BloodPressure'].mean())
plt.barh(1, neg['BloodPressure'].mean())


# Skin Thickness
plt.subplot(8, 1, 4)
plt.barh(1, pos['SkinThickness'].mean())
plt.barh(1, neg['SkinThickness'].mean())


# Insulin
plt.subplot(8, 1, 5)
plt.barh(1, pos['Insulin'].mean())
plt.barh(1, neg['Insulin'].mean())


# BMI
plt.subplot(8, 1, 6)
plt.barh(1, pos['BMI'].mean())
plt.barh(1, neg['BMI'].mean())


# 'Diabetes Pedigree Function'
plt.subplot(8, 1, 7)
plt.barh(1, pos['DiabetesPedigreeFunction'].mean())
plt.barh(1, neg['DiabetesPedigreeFunction'].mean())


# Age
plt.subplot(8, 1, 8)
plt.barh(1, pos['Age'].mean())
plt.barh(1, neg['Age'].mean())


plt.show()
