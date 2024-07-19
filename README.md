# Diabetes Prediction using Machine Learning
## Project Description
### Solution Summary

The problem is that diabetes is on the rise, and doctors and their staff will need help diagnosing diabetes quickly and accurately. This application proposes to use machine learning to help doctors quickly and accurately detect diabetes in patients based on a number of data points. With input from doctors and some code adjustment, it could also be used for early detection of diabetes. The application will provide the solution to this problem by using the patient’s medical data as input data entered by medical staff and output if the patient has diabetes or not. It uses a diabetes dataset consisting of 768 rows, with 8 input values(columns) and one target value(column) which is either true(1) indicating that the patient does have diabetes, or false(0) indicating that the patient does not have diabetes. There is also functionality to graph the input data to help visualize the dataset.

### Data Summary
The source of the data for the proposed project is [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

The method for the data collection was through direct medical examinations and tests administered by health professionals. This would typically involve measuring blood glucose levels, blood pressure, BMI, and other relevant health indicators through standard medical procedures. 

There are technically no missing values in the dataset but that is actually not a true story as in this particular dataset all the missing values were given 0 as a value which is not good for the authenticity of the dataset. The data will be prepared for use by the machine learning algorithm from part C2 for my proposed project by replacing all 0 values with NAN values and then replacing the NAN values with the mean value of that specific column. The following shows the percentage of 0 values in the dataset:

* Pregnancies - 0% (There are 0 values in this column, but it means the patient has never given birth)
* Glucose - 0.7%
* Blood Pressure - 4.6%
* Skin Thickness - 29.6%
* Insulin - 48.7%
* BMI - 1.4%
* Degree Pedigree Function - 0%
* Age - 0%

### Machine Learning
The application uses a dataset from the National Institute of Diabetes and Digestive and Kidney Diseases that has 8 different medical variables and one target variable. The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset(Pima Indians Diabetes Database - UCI MACHINE LEARNING and Kaggle Team).

A supervised learning classification algorithm was chosen to make a prediction because the target was categorical and the target values were known. Decision tree classification is a Random Forest machine learning algorithm that uses multiple decision trees to improve classification and prevent overfitting(Supervised Machine Learning - Geeks for Geeks).

A decision tree is a flowchart-like tree structure where each internal node denotes the feature, branches denote the rules and the leaf nodes denote the result of the algorithm. It is a versatile supervised machine-learning algorithm. It is a Random Forest algorithm used to train different subsets of training data, which makes random forest one of the most powerful algorithms in machine learning(Decision Tree - Geeks for Geeks).

The pandas and numpy libraries were used to prepare the dataset. The sci-kit learn library was used to split the data, train the model using the training data, check the accuracy using the test data, and predict the outcome. The joblib library was used to save and load a persisting model, to save time when making a prediction.

The application will predict if a patient has diabetes using 8 different medical variables. This happens because a machine learning algorithm was implemented. A csv dataset was read into a pandas dataframe, that dataframe was then randomly split into two parts using sci-kit learn’s train_test_split method. Eighty percent of the data frame was used to train the model using sci-kit learn’s fit method, and the remaining twenty percent was used for testing. A prediction is made with the test data using sci-kit learn’s predict method. The accuracy of the training was tested using sci-kit learn’s accuracy_score method. The application gives the user the option to use the original dataset, unmodified, or to use a cleaned version. The dataset has a lot of 0 values, which is okay in the pregnancies and target columns, but in all other columns it means that the value is invalid and lowers the accuracy of training and ultimately the predictions. The cleaned version of the data converts the 0 values in all columns except the pregnancies and target columns to the average value of the column which can then be used for training, which may increase the accuracy of the training model and ultimately the predictions.

Supervised learning was selected because the dataset being used has labeled columns and because it has input and output parameters. Classification is the type of supervised learning that was selected because the outcome or target can be classified or categorized into two different categories. The supervised machine learning algorithm that was selected as the best choice was the Decision Tree Classification algorithm. The decision tree classification algorithm was selected because it is used to model decisions and their possible consequences. Each internal node in the tree represents a decision, while each leaf node represents a possible outcome. Decision trees can be used to model complex relationships between input features and output variables.In the training process, the data is split 80/20. 80% as training data and the rest as testing data. The model learns from training data only. Learning means that the model will build some logic of its own. Once the model is ready it can be tested. At the time of testing, the input is fed from the remaining 20% of data that the model has never seen before, the model will predict some value and will compare it with the actual output and calculate the accuracy. (Supervised Machine Learning - Geeks for Geeks). 

### Validation
The accuracy of the machine learning application was accessed using Sci-Kit Learn’s metric module accuracy_score method. It takes the Y values of the test data and the prediction as inputs and outputs the accuracy score, which is a value between 0 and 1. Multiplying this number by 100 will give the accuracy percent. Classification accuracy can be described as the “percentage of true prediction” or it is a sum of the true positive and true negative divided by the sum of predicted class value, it can be calculated using the following formula:

X = t / n ∗ 100

Here X represents the classification accuracy, t is the number of correct classification and n is a total number of samples. (Deep learning approach for diabetes prediction using PIMA Indian dataset - Huma Naz￼ and Sachin Ahuja)

## User Guide
Instructions for downloading and installing necessary software and libraries.
> [!Note]
> The following instructions are intended for a PC running Windows 10 or higher.

1. If it’s not already installed on the PC, download [Python 3.11](https://www.python.org/downloads/release/python-3119/)(The application may work with Python versions 3.8 through 3.10 or 3.12, but it was built, tested, and only guaranteed to work correctly using Python version 3.11)

2. [Install Python](https://www.geeksforgeeks.org/how-to-install-python-on-windows/), after a successful installation, continue to the next step.
> [!Note]
>  A command prompt window can be opened by pressing the windows key and typing `cmd`.

3. In a command prompt window type: `python –version` or `python3 –version`  to ensure Python version 3.11 is installed and configured.
4. (Optional) If running the application in a virtual environment is desired, configure it and install the following libraries while it is activated.
5. In a command prompt window type: `pip install pandas`
6. In a command prompt window type: `pip install numpy`
7. In a command prompt window type: `pip install matplotlib`
8. In a command prompt window type: `pip install -U scikit-learn` 
9. In a command prompt window type: `pip install PyQt5`

An example of how to use the application: 
1. Clone this project to any directory and make note of the path to it.
2. In a command prompt window, navigate to the directory where the project was cloned and go into that directory.
3. In a command prompt type `dir`, and verify that the “main.py”, “plot_data.py”, “process_and_train_data.py”, and “diabetes.csv” files are there, if any of those files are not present, go back to step 1.
4. If typing `python –version` in the command prompt window displays `Python 3.11.X`, continue to step 4a. If typing `python3 –version` in the command prompt window displays `Python 3.11.X`, continue to step 4b.
    - a. In a command prompt window, type: “python main.py” and ensure the applicationGUI is displayed.
    - b. In a command prompt window, type: “python3 main.py” and ensure the applicationGUI is displayed. 
5. Once the application is running:
    - A label is shown informing the user if the “diabetes.csv” dataset has been found or not.
      - If the “diabetes.csv” file is not found, the user will not be able to proceed and will be informed that the “diabetes.csv” file needs to be in the same directory as the application file.
      - If the “diabetes.csv” file is found, the user will be able to proceed.
    - The “Select dataset to use:” drop down box can be used to either select the original, unmodified, dataset to proceed with, or a cleaned version of the original dataset where all “0” values are replaced with the average value of the column, for all columns except for the pregnancy column.
    - The close button will close any open windows and quit the application.
6. The “Show Graphs” button will open a new window where the data can be graphed in either a bar graph, scatter plot, or a histogram graph.
    - Use the “Select Data to Plot” drop down box to select which column of data to graph.
    - The “Hide data with a value of 0” check box can be used to hide all “0” values for the scatter plot and histogram graph. Note: The “Hide data with a value of 0” check box will be hidden when “Pregnancies” is selected in the “Select Data to Plot” drop down box.
    - Select a graph/plot to display the data by clicking on the corresponding button.
      - The bar graph will display max value for the selected column, the average value of the dataset where all results are positive for diabetes, the average value of the dataset where all results are negative for diabetes, and the min value for the selected column.
      - The scatter plot will display all values in the selected column and will be green for results where the patient was negative for having diabetes and red for results where the patient was positive for having diabetes.
      - The histogram graph will display all values in the selected column.
    - The “Close” button will close the Plot Data window.
7. The “Predict” button will open a new window where the user can enter data and get a prediction of whether diabetes is predicted or not.
    - Either select a predefined set of patient data from the “Predefined Values” drop down box or enter custom values in the input spinboxes, then click on the “Make Prediction” button. The result will be displayed at the top of the window.
    - Click the “Retrain Model” button to retrain the model.
    - The “Training Model Accuracy” label to the right of the “Retrain Model” button will display the accuracy of the tested dataset.
    - The “Close” button will close the Predict window.

## Visualizations
### Main Window

### Bar Graph

### Scatter Plot

### Histogram

### Predict Window (No Prediction)

### Predict Window (Negative Result)

### Predict Window (Positive Result)
