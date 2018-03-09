# Set proper working directory

# Import {library_name} as {shortcut_name}
## Numpy contains mathematical tools
import numpy as np 
## Matplotlib contains plotting tools
import matplotlib.pyplot as plt
## Pandas contains dataset import and management tools
import pandas as pd

# Import the dataset
## Use panda to bring in 'Data.csv'
dataset = pd.read_csv('Data.csv')
## Assign independent and dependent matrices
### Original data
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
### My data
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

# Splitting the dataset into the Training set and Test set
# Import train_test_split
from sklearn.cross_validation import train_test_split
## split 20% for testing  using random number generator & assign train, test X, Y arrays
X_train_unscaled, X_test_unscaled, Y_train_unscaled, Y_test_unscaled = train_test_split(X, Y, test_size = 0.2, random_state = 0)

"""
# Feature Scaling so that age and salary are weighed the same
## Import StandardScaler ((x_stand = (x - mean(x)) / (standard deviation(x))))
from sklearn.preprocessing import StandardScaler
## instantiate StandardScaler
sc_X = StandardScaler()
## Transform train and test X arrays
X_train = sc_X.fit_transform(X_train_unscaled)
X_test = sc_X.transform(X_test_unscaled)
sc_y = StandardScaler()
## Transform train train Y array (test Y array will be predicted)
Y_train = sc_y.fit_transform(Y_train_unscaled)
"""
