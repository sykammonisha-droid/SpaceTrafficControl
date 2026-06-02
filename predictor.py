import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

days = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)

satellites = np.array([100, 120, 150, 180, 220, 260, 300])

model = LinearRegression()

model.fit(days, satellites)

next_week = np.array([[14]])

prediction = model.predict(next_week)

print("Predicted Satellites After One Week:")

print(int(prediction[0]))