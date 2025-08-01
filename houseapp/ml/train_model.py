import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("data.csv")

X = df[['area', 'bedrooms', 'age']]
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the trained model to disk
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
