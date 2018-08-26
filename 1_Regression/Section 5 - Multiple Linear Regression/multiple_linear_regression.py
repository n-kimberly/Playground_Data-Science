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
dataset = pd.read_csv('50_Startups.csv')
## Assign independent and dependent matrices
### Original data
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
### My data
X = dataset.iloc[:, :-1].values

# Encode independent categorical data
## Import LabelEncoder and OneHotEncoder
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
## instantiate labelencoder_X from LabelEncoder class
labelencoder_X = LabelEncoder()
## fit to x
labelencoder_X_fit = labelencoder_X.fit_transform(x[:,3])
## assign transformed matrix to X
X[:,3] = labelencoder_X_fit
## instantiate onehoteencoder_X from OneHotEncoder class with col 0 as category
onehotencoder_X = OneHotEncoder(categorical_features=[3])
## fit transform to X and convert to array
onehotencoder_X_fit = onehotencoder_X.fit_transform(X).toarray()
## assign transformed matrix to X
X = onehotencoder_X_fit

# Avoiding the Dummy Variable Trap
## Remove first column, one of the dummy variable columns
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
# Import train_test_split
from sklearn.cross_validation import train_test_split
## split 20% for testing  using random number generator & assign train, test X, Y arrays
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training Set
## Import LinearRegression
from sklearn.linear_model import LinearRegression
## Instantiate LinearRegression()
regressor = LinearRegression()
## Call fit method on training set
regressor.fit(X_train, y_train)

# Predicting the Test set results
## Call predict method on test array
y_pred = regressor.predict(X_test)

# Visualising the Training set data
## Split up X
X_train_4 = X_train[:,4]
X_train_3 = X_train[:,3]
X_train_2 = X_train[:,2]

plt.scatter(X_train_4, y_train, color = 'red')
plt.title('Profit vs. Marketing Spend')
plt.xlabel('Marketing Spend')
plt.ylabel('Profit')
plt.show()

plt.scatter(X_train_3, y_train, color = 'red')
plt.title('Profit vs. Admin Spend')
plt.xlabel('Admiin Spend')
plt.ylabel('Profit')
plt.show()

plt.scatter(X_train_2, y_train, color = 'red')
plt.title('Profit vs. Engineering Spend')
plt.xlabel('Engineering Spend')
plt.ylabel('Profit')
plt.show()

# Visualising the Test set data
## Split up X
X_test_4 = X_test[:,4]
X_test_3 = X_test[:,3]
X_test_2 = X_test[:,2]

plt.scatter(X_test_4, y_pred, color = 'red')
plt.scatter(X_test_4, y_test, color = 'blue')
plt.title('Profit vs. Marketing Spend')
plt.xlabel('Marketing Spend')
plt.ylabel('Profit')
plt.show()

plt.scatter(X_test_3, y_pred, color = 'red')
plt.scatter(X_test_3, y_test, color = 'blue')
plt.title('Profit vs. Admin Spend')
plt.xlabel('Admiin Spend')
plt.ylabel('Profit')
plt.show()

plt.scatter(X_test_2, y_pred, color = 'red')
plt.scatter(X_test_2, y_test, color = 'blue')
plt.title('Profit vs. Engineering Spend')
plt.xlabel('Engineering Spend')
plt.ylabel('Profit')
plt.show()