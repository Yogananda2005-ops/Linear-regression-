import numpy as np
from sklearn.linear_model import LinearRegression


model = LinearRegression()
model.fit(x,y)

prediction = model.predict([[6]])
print("Prediction:", prediction)