# First, set proper working directory

## Then import {library_name} as {shortcut_name}
import numpy as np # contains mathematical tools
import matplotlib.pyplot as plt #
import pandas as pd

# Importing the dataset, 'Data.csv'
dataset = pd.read_csv('Data.csv')
# Assign independent and dependent matrices
x = dataset.iloc[:, :-1].values
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Take care of missing data
## sudo apt-get install python-sklearn
from sklearn.preprocessing import Imputer 
## assign imputer the mean strategy
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
## assign imputer to fit X columns with missing data
imputer_fit = imputer.fit(x[:,1:3])
## assign x columns missing data to transformed imputer matrix
X[:,1:3] = imputer_fit.transform(x[:,1:3])

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""