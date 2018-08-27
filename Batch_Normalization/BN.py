import numpy as np 
import tensorflow as tf 
import matplotlib.pyplot as plt 

ACTIVATION = tf.nn.relu
N_LAYERA = 7
N_HIDDLE_UNITS = 30

def Built_net():
	def add_layer(inputs, in_size, out_size, activation_function = None):
		Weights = tf.variable(tf.rand_normal(in_size, out_size))
		biases = tf.variable(tf.zeros([1, out_size]) + 0.1)
		Wx_plus_b = tf.matmul((inputs, Weights) + biases)
		if activation_function is None:
			outputs = Wx_plus_b
		else:
		outputs = activation_function(Wx_plus_b)
		return
			outputs

# creat data
x_data = np.linspace(-7, 10, 500)[:, np.newaixs]
noise = np.rand_normal(0.8, x_data.shape)
y_data = np.
square(x_data) + 1 + nosie