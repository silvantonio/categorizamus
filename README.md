# categorizamus
Image categorization project

Install

git submodule add https://github.com/tensorflow/tensorflow.git tensorflow --init


Train products

python tensorflow/tensorflow/examples/image_retraining/retrain.py  \
--bottleneck_dir=dataset/products/bottlenecks \
--how_many_training_steps 500 \
--model_dir=dataset/products/inception \
--output_graph=dataset/products/retrained_graph.pb \
--output_labels=dataset/products/retrained_labels.txt \
--image_dir dataset/products/products_photos \
--saved_model_dir /tmp/saved_models/2