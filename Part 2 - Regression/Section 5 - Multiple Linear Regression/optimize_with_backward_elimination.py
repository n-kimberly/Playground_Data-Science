# Building optimal model using Backward Elimination

## Import csv library for outputting summary tables
import csv
## Statsmodel library, does not automatically integrate b0
import statsmodels.formula.api as sm
## Add column of 1's to account for b0 the intercept
X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis=1)

## Initialize optimized matrix of features
X_opt = X[:, [0, 1, 2, 3, 4, 5]]

# Step 1: Identify significance level
alpha = 0.05

# Step 2: Fit full model with all possible predictors
## Instantiate regressor as fit of X and y
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
## Print summary
elim_1 = regressor_OLS.summary(alpha = alpha).as_csv
res = [elim_1]
csvfile = 'Elim_1.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(res)
elim_1

# Step 3: Eliminate predictor with highest P value > 0.05
X_opt = X[:, [0, 1, 3, 4, 5]]

# Step 2: Refit model with elimination 
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
## Print summary
elim_2 = regressor_OLS.summary(alpha = alpha).as_csv
res = [elim_2]
csvfile = 'Elim_2.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(res)
elim_2    

# Step 3: Eliminate the predictor of highest P value > 0.05
## Here that would be x1: column 1
X_opt = X[:, [0, 3, 4, 5]]

# Step 2: Refit model with elimination 
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
## Print summary
elim_3 = regressor_OLS.summary(alpha = alpha).as_csv
res = [elim_3]
csvfile = 'Elim_3.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(res)    
elim_3
    
# Step 4: Remove the predictor of highest P value > 0.05
## Here that would be x2: column 2
X_opt = X[:, [0, 3, 5]]

# Step 2: Refit model with elimination 
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
## Print summary
elim_4 = regressor_OLS.summary(alpha = alpha).as_csv
res = [elim_4]
csvfile = 'Elim_4.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(res)  
elim_4

# Step 3: Remove the predictor of highest P value > 0.05
## Here that would be x2: column 2
X_opt = X[:, [0, 3]]

# Step 2: Refit model with elimination 
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
# Print summary
elim_5 = regressor_OLS.summary(alpha = alpha).as_csv
res = [elim_5]
csvfile = 'Elim_5.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(res)  
elim_5

# Step 3: Remove the predictor of highest P value > 0.05
## There are no more eliminations to be made

# Compile summaries used in eliminations
res = [elim_1, elim_2, elim_3]
csvfile = 'Eliminations.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in res:
        writer.writerow([val])       

#======================================================#

# Fitting Simple Linear Regression to the optimized set
X_vis = X_opt[:,1:2]
## Import LinearRegression
from sklearn.linear_model import LinearRegression
## Instantiate LinearRegression()
regressor = LinearRegression()
## Call fit method on training set
regressor.fit(X_vis, y)

# Visualize final model
plt.scatter(X_vis, y, color = 'red')
plt.plot(X_vis, regressor.predict(X_vis), color = 'blue')
plt.title('Profit vs. Engineering Spend')
plt.xlabel('Engineering Spend')
plt.ylabel('Profit')
plt.show()


