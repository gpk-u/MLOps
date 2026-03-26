import numpy as np
from sklearn.linear_model import LinearRegression
import pickle


# fake dataset
X = np.array([[500], [1000], [1500], [2000], [2500]])
y = np.array([100000, 200000, 300000, 400000, 500000])

# train model
model = LinearRegression()
model.fit(X,y)

# save model
with open("model.pkl", "wb") as f:
    pickle.dump(model,f)


print("Model Trained and saved")