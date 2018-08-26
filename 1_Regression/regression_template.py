# Regression Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('/home/n-kimberly/code/Machine-Learning/Part 2 - Regression/Section 6 - Polynomial Regression/Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Fitting Polynomial Regression to the dataset
from sklearn.linear_model import LinearRegression
'''
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 5)
X = poly_reg.fit_transform(X)
poly_reg.fit(X, y)
'''
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X, y)

# Visualising the Polynomial Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(X), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
'''
# Predicting a new result with Polynomial Regression
X_desired = poly_reg.fit_transform(np.array([[6.5]]))
lin_reg_2.predict(X_desired)
'''