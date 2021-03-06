#https://thenewstack.io/machine-learning-10-lines-code/
import tensorflow as tf
#import systems as sys
from urllib import request

#image_path = sys.argv[1]
image_path = "products_photos/shoe/61cbAQatNlL._UL1500_.jpg"

# Read in the image_data
# image_data = tf.gfile.FastGFile(image_path, 'rb').read()

image_url = "https://media.gq.com/photos/558359513655c24c6c963e8d/master/w_640/style-blogs-the-gq-eye-Sperry%20Top%20Sider-635.jpeg"
req = request.Request(image_url)
response = request.urlopen(req)
image_data = response.read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
in tf.gfile.GFile("retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

# Feed the image_data as input to the graph and get first prediction
with tf.Session() as sess:

    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

    predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})

    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    print(top_k)

    response = []
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))
        response.append([human_string, score])

    print(response)