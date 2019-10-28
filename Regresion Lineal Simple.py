import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import linear_model 

df = pd.read_csv('countries.csv') 
df_mex = df[df.country == "Mexico"] 
df_mex.plot.scatter(x='year', y='lifeExp')

x = np.asanyarray(df_mex[['year']]) 
y = np.asanyarray(df_mex[['lifeExp']]) 

model = linear_model.LinearRegression() 
model.fit(x, y) 

Years = np.array([2005, 2019, 3019, 542]) 

Years = Years.reshape(-1, 1) 

print(model.predict(Years))