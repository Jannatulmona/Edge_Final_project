import pandas as pd

data = {
    'area': [2600, 3000, 1800, 2200],
    'bedrooms': [3, 4, 2, 3],
    'age': [20, 15, 30, 25],
    'price': [550000, 565000, 350000, 450000]
}

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
