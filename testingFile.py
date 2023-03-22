import numpy as np
import cv2
from pieceClassifier import predict_image_piece
from colourClassifier import predict_image_colour
from PIL import Image
import pprint

# Open the image
img = Image.open("exampleImages/handDrawn.jpg").convert("RGB")

# Get the width and height of the image
width, height = img.size

# Calculate the size of each square
square_size = width // 8

# Create a list to store the resized squares
squares = []

# Loop through each row and column of the image
for i in range(8):
    for j in range(8):
        # Crop the square from the image
        x = j * square_size
        y = i * square_size
        square = img.crop((x, y, x + square_size, y + square_size))
        
        # Resize the square to (85, 85)
        square = square.resize((85, 85))
        
        # Add the square to the list
        squares.append(square)

def get_predicted_squares():
    predicted_squares = [[],[],[],[],[],[],[],[]]

    position_to_square = lambda position: position[0] * 8 + position[1]

    for i in range(8):
        for j in range(8):
            square_number = position_to_square((i, j))
            piece_colour = predict_image_colour(squares[square_number])
            piece_type = predict_image_piece(squares[square_number])
            predicted_squares[i].append(piece_colour + " " + piece_type)

    return predicted_squares








"""
'Chess Puzzle Loader'
Idea: First, get the model to check colour of the piece it predicts.
Then, iterate through each part of the board and see which pieces are present.
Once board state is recorded and recognised, put this into the chess game
and begin playing from whatever image is passed in.
"""