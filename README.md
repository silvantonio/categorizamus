# categorizamus
Image categorization project

Train flower

python tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=dataset/flowers/bottlenecks \
--how_many_training_steps 500 \
--model_dir=dataset/flowers/inception \
--output_graph=dataset/flowers/retrained_graph.pb \
--output_labels=dataset/flowers/retrained_labels.txt \
--image_dir dataset/flowers/flower_photos \
--saved_model_dir /tmp/saved_models/1

train products

python tensorflow/tensorflow/examples/image_retraining/retrain.py  \
--bottleneck_dir=dataset/products/bottlenecks \
--how_many_training_steps 500 \
--model_dir=dataset/products/inception \
--output_graph=dataset/products/retrained_graph.pb \
--output_labels=dataset/products/retrained_labels.txt \
--image_dir dataset/products/products_photos \
--saved_model_dir /tmp/saved_models/2