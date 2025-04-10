import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from tabulate import tabulate

X = filtered_df[['pm2.5 aqi value']].values
y = filtered_df['ozone aqi value'].values

model = LinearRegression()
model.fit(X, y)

slope = model.coef_[0]
intercept = model.intercept_
mse = mean_squared_error(y, model.predict(X))
r2 = r2_score(y, model.predict(X))

data = [
    ["Slope (m)", slope],
    ["Intercept (c)", intercept],
    ["Mean Squared Error", mse],
    ["R^2 Score", r2]
]

print(tabulate(data, headers=["Metric", "Value"], tablefmt="grid", stralign="center", numalign="center"))