import tensorflow as tf
from tensorflow.python.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2

PIECE_NAMES = ["bishop", "blank", "king", "knight", "pawn", "queen", "rook"]

def load_images():
    piece_images = {}
    file_path = "chessImageData/"

    for piece in PIECE_NAMES:
        images = []
        for filename in os.listdir(file_path + piece):
            if not filename.startswith('.'):  # Exclude hidden files
                img = Image.open(os.path.join(file_path + piece, filename))
                img_array = np.array(img)
                images.append(img_array)
        
        piece_images[piece] = images
    
    return piece_images

piece_images = load_images()

# Convert the image data to a numpy array
X = np.concatenate([piece_images[piece] for piece in PIECE_NAMES])

# label images 
y = np.concatenate([[i]*len(piece_images[piece]) for i, piece in enumerate(PIECE_NAMES)])

# randomly shuffle data before splitting
X, y = shuffle(X, y, random_state=50)

# normalise the pixel values to be between 0 and 1
X = X.astype('float32') / 255

# split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=50)

file_name = "pieceClassifierModel.h5"

if not os.path.isfile(f"CNN_models/{file_name}"):
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3,3), activation="relu",input_shape=(85, 85, 3)),
        tf.keras.layers.MaxPooling2D((2, 2), strides=2),

        tf.keras.layers.Conv2D(64, (3,3), padding='same', activation="relu"),
        tf.keras.layers.MaxPooling2D((2, 2), strides=2),

        tf.keras.layers.Flatten(),

        tf.keras.layers.Dense(100, activation="relu"),

        # dropout regularisation to lower variance
        # tf.keras.layers.Dropout(0.1),
        tf.keras.layers.Dense(7, activation="softmax")
    ])

    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

    # train the model
    trained_model = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

    model.save("CNN_models/pieceClassifierModel.h5")

# saved trained model
loaded_model = tf.keras.models.load_model("CNN_models/pieceClassifierModel.h5")

# evaluate the model on test data
# test_loss, test_acc = model.evaluate(X_val, y_val)

# print the test accuracy
# print('Test accuracy:', test_acc)

def predict_image_with_path(image_path: str):
    img = cv2.imread(image_path)
    image = cv2.resize(img, (85, 85))
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # normalize the pixel values

    # classify the image
    predictions = loaded_model.predict(image)
    predicted_label = np.argmax(predictions)

    which_img = {0: "bishop", 1: "blank", 2: "king", 3: "knight", 
                 4: "pawn", 5: "queen", 6: "rook"}

    return f"Predicted piece: {which_img[predicted_label]}"

def predict_image_piece(image):
   # Convert the PIL image to a numpy array
    img = np.array(image)

    # Resize the image to (85, 85) and normalize the pixel values
    image = cv2.resize(img, (85, 85))
    image = np.expand_dims(image, axis=0)
    image = image / 255.0

    # Classify the image
    predictions = loaded_model.predict(image)
    predicted_label = np.argmax(predictions)

    which_img = {0: "bishop", 1: "blank", 2: "king", 3: "knight", 
                 4: "pawn", 5: "queen", 6: "rook"}

    return f"{which_img[predicted_label]}"