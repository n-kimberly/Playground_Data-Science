# Set proper working directory

# - Data Preprocessing

# Import {library_name} as {shortcut_name}
## Numpy contains mathematical tools
import numpy as np 
## Matplotlib contains plotting tools
import matplotlib.pyplot as plt
## Pandas contains dataset import and management tools
import pandas as pd

# Import the dataset
## Use panda to bring in 'Social_Network_Ads.csv'
dataset = pd.read_csv('Social_Network_Ads.csv')
## Assign relevant independent and dependent matrices
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set
# Import train_test_split
from sklearn.cross_validation import train_test_split
## There are 400 observations. Perhaps we will train with 300 and test with the last 100 (25%)
## Split 25% for testing  using random number generator & assign train, test X, Y arrays
X_train_unscaled, X_test_unscaled, y_train_unscaled, y_test_unscaled = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling so that age and salary are weighed the same
## Import StandardScaler ((x_stand = (x - mean(x)) / (standard deviation(x))))
from sklearn.preprocessing import StandardScaler
## instantiate StandardScaler
sc_X = StandardScaler()
## Transform train and test X arrays
## Fit sc_X to X_test_unscaled matrix, then transformed it
X_train = sc_X.fit_transform(X_train_unscaled)
## Use same fitted sc_X object to transform X_test matrix
X_test = sc_X.transform(X_test_unscaled)
## No need to transform categorical data y
y_train = y_train_unscaled
y_test = y_test_unscaled

# - Fitting Logistic Regression to the Training Set
# Import sklearn library from LogistcRegression class
from sklearn.linear_model import LogisticRegression
# Create logistic regression object to act as classifier to fit our object
## Use random state classifier to get same result every time
classifier = LogisticRegression(random_state=0)
# Fiting classifier logistic regression object to our training set so that the classifier can learn the correlation
classifier.fit(X_train, y_train)

# - Predict test set result
y_pred = classifier.predict(X_test)

# - Making the Confusion Matrix
## import function (not class) from metrics library
## class contains capitals; functions are lower case
from sklearn.metrics import confusion_matrix
# create confusion matrix instance
cm = confusion_matrix(y_true=y_test, y_pred=y_pred)
## result is 65 true negatives, 3 false positives, 8 false negatives, and 24 true positives

# - Visualize predictions
from matplotlib.colors import ListedColormap
## Declare X_set and y_set to make code more portable
## Assign X_set and y_set to desired set of values
X_set, y_set = X_train, y_train
## Create coordinate matrix from coordinate vectors
## Here vectors are size max - min of X_set age and salary with resolution 0.01
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop=X_set[:,0].max()+1, step = 0.01),
            np.arange(start = X_set[:, 1].min() - 1, 
                      stop=X_set[:,1].max()+1, 
                      step = 0.01))
## Now apply classifier on all the points
## Use contour function to create prediction boundary
## ravel is a function that flattens an array
plt.contourf(X1,
             X2,
             classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75,
             cmap=ListedColormap(('red','green')))
## For i,j = 0,0 and i,j = 1,1, plot observations for X when y = j
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], 
                X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
## Add plot titles and info
plt.title('Logistic Regression (Training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()