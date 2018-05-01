Categorizamus: image categorization
=======================================
Image categorization project


Requirements
------------

- Python 3.5.x 

Quick start
-----------

git submodule add https://github.com/tensorflow/tensorflow.git tensorflow --init

Execute:
docker-compose up
docker exec -it categorizamus_web_1 bash

### How to train dataset:

python tensorflow/tensorflow/examples/image_retraining/retrain.py  \
--bottleneck_dir=dataset/products/bottlenecks \
--how_many_training_steps 500 \
--model_dir=dataset/products/inception \
--output_graph=dataset/products/retrained_graph.pb \
--output_labels=dataset/products/retrained_labels.txt \
--image_dir dataset/products/products_photos \
--saved_model_dir /tmp/saved_models/2