import tensorflow as tf
sess = tf.Session()

filename_queue = tf.train.string_input_producer(["iris.csv"])

reader = tf.TextLineReader(skip_header_lines=0)
key, value = reader.read(filename_queue)
record_defaults = [[0.],[0.],[0.],[0.],[""]]
col1, col2, col3, col4, col5 = tf.decode_csv(value,record_defaults=record_defaults)
tarray = tf.TensorArray(dtype=tf.float32, size=149)
features = tf.stack([col1,col2,col3,col4])
with tf.Session() as sess:

  # Start populating the filename queue.
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    for i in range(120):
    # Retrieve a single instance:
      example, label = sess.run([features, col4])
      print(label)

    coord.request_stop()
    coord.join(threads)