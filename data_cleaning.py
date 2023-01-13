import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv("phonedata.csv")
plt.scatter(data['product'], data['price'])
plt.show()
