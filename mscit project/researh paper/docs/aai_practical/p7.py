#pip install scikit-learn 
# Import scikit-learn dataset library 
from sklearn import datasets 
from sklearn.model_selection import train_test_split 
from sklearn import metrics 
from sklearn.linear_model import LogisticRegression 
# Load dataset 
cancer = datasets.load_breast_cancer() 
# Print the names of the 13 features 
print("Features: ", cancer.feature_names) 
# Print the label type of cancer ('malignant', 'benign') 
print("Labels: ", cancer.target_names) 
# Print data (feature) shape 
print("Data shape: ", cancer.data.shape) 
# Print the cancer data features (top 5 records) 
print("Top 5 records: \n", cancer.data[:5]) 
# Print the target values 
print("Target values: ", cancer.target) 
# Split dataset into training set and test set 
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, 
test_size=0.3, random_state=109) 
print("Training set shape: ", x_train.shape, y_train.shape) 
print("Test set shape: ", x_test.shape, y_test.shape) 
# Train a logistic regression model 
model = LogisticRegression() 
model.fit(x_train, y_train) 
# Make predictions on the test set 
y_pred = model.predict(x_test) 
# Model Accuracy: how often is the classifier correct? 
print("Accuracy:", metrics.accuracy_score(y_test, y_pred)) 
# Model Precision: what percentage of positive tuples are labeled as such? 
print("Precision:", metrics.precision_score(y_test, y_pred)) 
# Model Recall: what percentage of positive tuples are labelled as such? 
print("Recall:", metrics.recall_score(y_test, y_pred))
