import tensorflow as tf  # now import the tensorflow module
print(tf.version)  # make sure the version is 2.x

string = tf.Variable("this is a string", tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.567, tf.float64)

rank1_tensor = tf.Variable(["Test"], tf.string)
rank2_tensor = tf.Variable([["test", "ok"], ["test", "yes"]], tf.string)

print(tf.rank(rank2_tensor))