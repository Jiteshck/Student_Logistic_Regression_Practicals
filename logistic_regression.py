import numpy as np
from sklearn.linear_model import LogisticRegression
# Study hours
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
# Result: 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])
# Create model
model = LogisticRegression()
# Train model
model.fit(X, y)
# Predict for a student who studied for 6 hours
prediction = model.predict([[6]])
print("Prediction:", prediction)
# Probability
probability = model.predict_proba([[6]])
print("Probability:", probability)