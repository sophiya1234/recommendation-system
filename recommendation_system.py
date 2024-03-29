# -*- coding: utf-8 -*-
"""recommendation_system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1In9sWOAAZHr0BAGVWndPudK8WQAx3-vu
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
data = pd.read_csv("tour_package.csv")

# Explore the dataset
print(data.head())
print(data.info())
print(data.describe())



# Handle missing values
data.dropna(inplace=True)

# Encode categorical variables
data_encoded = pd.get_dummies(data, columns=['TypeofContact', 'Occupation', 'Gender', 'MaritalStatus', 'Designation'])

# Split the data into features (X) and target variable (y)
X = data_encoded.drop(['ProdTaken', 'CustomerID'], axis=1)
y = data_encoded['ProdTaken']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Split categorical and numerical features
categorical_features = X.select_dtypes(include=['object']).columns
numerical_features = X.select_dtypes(exclude=['object']).columns

# Encode categorical variables
ct = ColumnTransformer(
    transformers=[
        ('one_hot_encoder', OneHotEncoder(), categorical_features)
    ],
    remainder='passthrough'
)
X_encoded = ct.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Visualize the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d")
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Classification report
print(classification_report(y_test, y_pred))

# Example new customer data
new_data = pd.DataFrame({
    'Age': [30],
    'TypeofContact': ['Company Invited'],
    'CityTier': [1],
    'Occupation': ['Salaried'],
    'Gender': ['Male'],
    'NumberOfPersonVisiting': [2],
    'PreferredPropertyStar': [4],
    'MaritalStatus': ['Single'],
    'NumberOfTrips': [3],
    'Passport': [1],
    'OwnCar': [1],
    'NumberOfChildrenVisiting': [0],
    'Designation': ['Executive'],
    'MonthlyIncome': [50000],
    'PitchSatisfactionScore': [4],
    'ProductPitched': ['Deluxe'],
    'NumberOfFollowups': [2],
    'DurationOfPitch': [20]
})