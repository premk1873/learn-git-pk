import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
# Step 1 :Import libraries and dataset
datas = pd.read_csv('data.csv') 
print(datas )
#Step 2: Dividing the dataset into 2 components
X = datas.iloc[:, 1:2].values 
y = datas.iloc[:, 2].values 
#Step 3: Fitting Linear Regression to the dataset 
from sklearn.linear_model import LinearRegression 
# Step 4: Fitting Polynomial Regression to the dataset 
from sklearn.preprocessing import PolynomialFeatures  
poly = PolynomialFeatures(degree = 4) 
X_poly = poly.fit_transform(X)  
poly.fit(X_poly, y) 
lin2 = LinearRegression() 
lin2.fit(X_poly, y)
# Step 5: Visualising the Linear Regression results 
# Visualising the Polynomial Regression results 
plt.scatter(X, y, color = 'blue') 
plt.plot(X, lin2.predict(X_poly), color = 'red') 
plt.title('Polynomial Regression') 
plt.xlabel('Temperature') 
plt.ylabel('Pressure')
plt.show()
