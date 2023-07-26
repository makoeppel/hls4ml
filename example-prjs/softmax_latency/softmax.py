import tensorflow as tf
import numpy as np

# Sources:
# https://www.tensorflow.org/api_docs/python/tf/keras/layers/Softmax
# https://developers.google.com/machine-learning/crash-course/multi-class-neural-networks/softmax

# Create a softmax 1layer that takes in a 25 element array
def create_model():
	# Create a model
	model = tf.keras.Sequential()
	model.add(tf.keras.layers.InputLayer(input_shape=(25,)))
	model.add(tf.keras.layers.Softmax())
				
	return model

# Save model to forms for hls4ml
def save_model(model, name=None):
	# Save as model.h5, model_weights.h5, and model.json
	if name is None:
		name = model.name
	model.save(name + '.h5')
	model.save_weights(name + '_weights.h5')
	with open(name + '.json', 'w') as outfile:
		outfile.write(model.to_json())
	return

if __name__ == '__main__':
    model = create_model()
    save_model(model, name='softmax')

# Image Matrix
    image_mat = np.array([
	[ 8.123456789, 7.123456789, 8.123456789, 7.123456789, 8.123456789, 7.123456789, 8.123456789, 7.123456789, 8.123456789, 7.123456789, 8.123456789, 7.123456789, 8.123456789, 7.123456789, 8.123456789, 7.123456789, 8.123456789, 7.123456789, 8.123456789, 7.123456789, 8.123456789, 7.123456789, 8.123456789, 7.123456789, 8.123456789 ]
    ])

    # Get prediction
    prediction = model.predict(image_mat)
    print("Image Matrix\n")
    print(image_mat)
    print("Prediction\n")
    print(prediction)

    image_mat3 = np.array([
	[  -8.123456789, -7.123456789, -8.123456789, -7.123456789, -8.123456789, -7.123456789, -8.123456789, -7.123456789, -8.123456789, -7.123456789, -8.123456789, -7.123456789, -8.123456789, -7.123456789, -8.123456789, -7.123456789, -8.123456789, -7.123456789, -8.123456789, -7.123456789, -8.123456789, -7.123456789, -8.123456789, -7.123456789, -8.123456789 ]
    ])

    # Get prediction
    prediction = model.predict(image_mat3)
    print("Image Matrix\n")
    print(image_mat3)
    print("Prediction\n")
    print(prediction) 