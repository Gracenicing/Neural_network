import tensorflow as tf 
import matplotlib.pyplot as plt

W1 = tf.Variable(tf.random_normal([2, 3], mean = 0, stddev = 1))

with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	
	output = sess.run(W1)
	print (output)
	x,y = output
	print(x)
	print(y)

	plt.scatter(x,y)
	plt.show()
	sess.close()
