import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(x, y)

prediction = model.predict(x)
print("Prediction: ", prediction)
print("kmec deploying the project")