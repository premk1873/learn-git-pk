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
lin = LinearRegression() 
lin.fit(X, y) 

# Step 4: Visualising the Linear Regression results 
plt.scatter(X, y, color = 'blue') 
plt.plot(X, lin.predict(X), color = 'red') 
plt.title('Linear Regression') 
plt.xlabel('Temperature') 
plt.ylabel('Pressure') 
plt.show()
