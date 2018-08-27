import numpy as np 
import matplotlib.pyplot as plt

# x = np.array([1, 2, 3, 4, 5])
# y = x[np.newaxis,:1]
# print (x.shape)
# print (y.shape)
# print (x)
# print (y)
x_data = np.linspace(-7,10,500)[:, np.newaxis]
noise = np.random.normal(-25, 0.8, x_data.shape)
y_data = np.square(x_data) - 5 + noise

plt.scatter(x_data, y_data)
plt.show()