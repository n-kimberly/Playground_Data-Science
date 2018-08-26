# Backward Elimination with p-values only
import statsmodels.formula.api as sm

## Write program
def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x
 
 ## Add column of 1's to account for b0 the intercept
X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis=1)

## Initialize optimized matrix of features
X_opt = X[:, [0, 1, 2, 3, 4, 5]]

## Define significance level
SL = 0.05

## Run program
X_Modeled = backwardElimination(X_opt, SL)

# Backward Elimination with p-values and Adjusted R Squared
import statsmodels.formula.api as sm

## Write Program
def backwardElimination(x, SL):
    numVars = len(x[0])
    temp = np.zeros((50,6)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:,j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()
    return x
 
 ## Add column of 1's to account for b0 the intercept
X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis=1)

## Initialize optimized matrix of features
X_opt = X[:, [0, 1, 2, 3, 4, 5]]

## Define significance level
SL = 0.05

## Run program
X_Modeled = backwardElimination(X_opt, SL)

# Visualize final model
X_eng = X_Modeled[:,2:3]
X_mark = X_Modeled[:,3:4]
from sklearn.linear_model import LinearRegression

regressor_eng = LinearRegression()
regressor_eng.fit(X_eng, y)
plt.scatter(X_eng, y, color = 'red')
plt.plot(X_eng, regressor_eng.predict(X_eng), color = 'blue')
plt.title('Profit vs. Engineering Spend')
plt.xlabel('Engineering Spend')
plt.ylabel('Profit')
plt.show()

regressor_mark = LinearRegression()
regressor_mark.fit(X_mark, y)
plt.scatter(X_mark, y, color = 'green')
plt.plot(X_mark, regressor_mark.predict(X_mark), color = 'blue')
plt.title('Profit vs. Engineering Spend')
plt.xlabel('Engineering Spend')
plt.ylabel('Profit')
plt.show()

X_comb = np.append(arr=X_eng, values=X_mark, axis=0)
y_comb = np.append(y, y)
regressor_comb = LinearRegression()
regressor_comb.fit(X_comb, y_comb)
plt.scatter(X_eng, y, color = 'red')
plt.scatter(X_mark, y, color = 'green')
plt.plot(X_comb, regressor_comb.predict(X_comb), color = 'blue')
plt.title('Profit vs. Engineering Spend')
plt.xlabel('Engineering Spend')
plt.ylabel('Profit')
plt.show()


