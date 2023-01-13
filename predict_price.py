import pandas
from sklearn.linear_model import LinearRegression

data = pandas.read_csv("phonedata.csv")
model = LinearRegression()
model.fit(data[['product']], data[['price']])
predicted_price = model.predict([[15]])
print(f"price of this model of Iphone is: {predicted_price[0][0]:.2f} $")