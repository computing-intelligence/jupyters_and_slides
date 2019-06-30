import tensorflow as tf
import numpy as np
import random


def func(x):
    if x <= 0: return -x ** 2
    else:
        return x**(3/4)


training_data = [random.randrange(-100, 100) for _ in range(100000)]
training_Y = [func(x) for x in training_data]
training_data = [x for x in training_data]

print(training_data[:10])
print(training_Y[:10])


x = tf.placeholder(dtype=tf.float32, shape=[None, 1], name='x')
y = tf.placeholder(dtype=tf.float32, shape=[None, 1], name='y')
a = tf.Variable(dtype=tf.float32, initial_value=tf.random_normal(stddev=0.05, shape=[1, 10]), name='a1')
a2 = tf.Variable(dtype=tf.float32, initial_value=tf.random_normal(stddev=0.5, shape=[10, 15]), name='a2')
a3 = tf.Variable(dtype=tf.float32, initial_value=tf.random_normal(stddev=0.5, shape=[15, 1]), name='a3')


b = tf.Variable(dtype=tf.float32, initial_value=tf.constant(0.0), name='b1')
b2 = tf.Variable(dtype=tf.float32, initial_value=tf.constant(0.0), name='b2')
b3 = tf.Variable(dtype=tf.float32, initial_value=tf.constant(0.0), name='b3')

output1 = tf.matmul(x, a) + b
output1 = tf.nn.relu(output1)
output2 = tf.matmul(output1, a2) + b2
output2 = tf.nn.relu(output2)

output3 = tf.matmul(output2, a3) + b3

y_hat = output3
loss = tf.losses.mean_squared_error(y_hat, y)
op = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss)


def change_to_vector(L):
    return [[e] for e in L]


def train_one_batch(sess, train_x, train_y, verbose=False):
    batch_x = np.array(change_to_vector(train_x))
    batch_y = np.array(change_to_vector(train_y))
    l, _ = sess.run([loss, op], feed_dict={x: batch_x, y: batch_y})
    if verbose: print(l)


def train_one_epoch(sess, batch_size, X, Y):
    batch_num = len(X) // batch_size

    np.random.shuffle(X)
    np.random.shuffle(Y)

    for i in range(batch_num):
        batch_x = X[i * batch_size: (i + 1) * batch_size]
        batch_y = Y[i * batch_size: (i + 1) * batch_size]
        if i % 100 == 0: verbose = True
        else:
            verbose = False
        train_one_batch(sess, batch_x, batch_y, verbose)


with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    epoch = 500
    for i in range(epoch):
        train_one_epoch(sess, 128, training_data, training_Y)


