import tensorflow as tf
from tensorflow.python.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2

COLOURS = ["white", "black"]

def load_images():
    piece_images = {}
    file_path = "colourImageData/"

    for colour in COLOURS:
        images = []
        for filename in os.listdir(file_path + colour):
            img = Image.open(os.path.join(file_path + colour, filename))
            img_array = np.array(img)
            images.append(img_array)
        
        piece_images[colour] = images
    
    return piece_images

piece_images = load_images()

# Convert the image data to a numpy array
X = np.concatenate([piece_images[piece] for piece in COLOURS])

# label images 
y = np.concatenate([[i]*len(piece_images[piece]) for i, piece in enumerate(COLOURS)])

# randomly shuffle data before splitting
X, y = shuffle(X, y, random_state=50)

# normalise the pixel values to be between 0 and 1
X = X.astype('float32') / 255

# split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=50)

file_name = "colourClassifierModel.h5"

if not os.path.isfile(f"CNN_models/{file_name}"):
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3,3), activation="relu",input_shape=(85, 85, 3)),
        tf.keras.layers.MaxPooling2D((2, 2), strides=2),

        tf.keras.layers.Conv2D(64, (3,3), padding='same', activation="relu"),
        tf.keras.layers.MaxPooling2D((2, 2), strides=2),

        tf.keras.layers.Flatten(),

        tf.keras.layers.Dense(100, activation="relu"),

        # dropout regularisation to lower variance
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(2, activation="softmax")
    ])

    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

    # train the model
    trained_model = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

    model.save("colourClassifierModel.h5")

# saved trained model
loaded_model = tf.keras.models.load_model("CNN_models/colourClassifierModel.h5")

def predict_image_colour(image):
   # Convert the PIL image to a numpy array
    img = np.array(image)

    # Resize the image to (85, 85) and normalize the pixel values
    image = cv2.resize(img, (85, 85))
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

    # Classify the image
    predictions = loaded_model.predict(image)
    predicted_label = np.argmax(predictions)

    which_img = {0: "white", 1: "black"}

    return f"{which_img[predicted_label]}"