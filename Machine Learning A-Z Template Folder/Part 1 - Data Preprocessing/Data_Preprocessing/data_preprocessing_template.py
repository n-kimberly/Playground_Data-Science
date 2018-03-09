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

# Take care of missing data
## sudo apt-get install python-sklearn
from sklearn.preprocessing import Imputer 
## instantiate imputer from Imputer class with mean strategy imputing via col
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
## fit to x
imputer_fit = imputer.fit(x[:,1:3])
## assign transformed matrix to corresponding X columns
X[:,1:3] = imputer_fit.transform(x[:,1:3])

# Encode independent categorical data
## Import LabelEncoder and OneHotEncoder
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
## instantiate labelencoder_X from LabelEncoder class
labelencoder_X = LabelEncoder()
## fit to x
labelencoder_X_fit = labelencoder_X.fit_transform(x[:,0])
## assign transformed matrix to X
X[:,0] = labelencoder_X_fit
## instantiate onehoteencoder_X from OneHotEncoder class with col 0 as category
onehotencoder_X = OneHotEncoder(categorical_features=[0])
## fit transform to X and convert to array
onehotencoder_X_fit = onehotencoder_X.fit_transform(X).toarray()
## assign transformed matrix to X
X = onehotencoder_X_fit

# Encode dependent categorical data
## instantiate labelencoder_y from LabelEncoder class
labelencoder_Y = LabelEncoder()
## fit to x
labelencoder_Y_fit = labelencoder_Y.fit_transform(y)
## assign transformed matrix to X
Y = labelencoder_Y_fit
## dependent variables do not need to be dummy encoded

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
# split 20% for testing  using random number generator & assign train, test X, Y arrays
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""