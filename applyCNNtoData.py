import numpy as np
import cv2
from pieceClassifier import predict_image_piece
from colourClassifier import predict_image_colour
from PIL import Image
import pprint

RANK_LENGTH, FILE_LENGTH = 8, 8

# image_path = "exampleImages/liPuzzle3.png"

def split_image(board_image: Image = None, img_path: str = None):
    # Open the image
    if img_path is not None:
        img = Image.open(img_path).convert("RGB")
    else:
        img = board_image

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
    
    return squares

def get_predicted_squares(squares):

    predicted_squares = [[],[],[],[],[],[],[],[]]

    position_to_square = lambda position: position[0] * 8 + position[1]

    for i in range(RANK_LENGTH):
        for j in range(FILE_LENGTH):
            square_number = position_to_square((i, j))
            piece_colour = predict_image_colour(squares[square_number])
            piece_type = predict_image_piece(squares[square_number])
            if piece_type != "blank":
                predicted_squares[i].append(piece_colour + " " + piece_type)
            else:
                predicted_squares[i].append(piece_type)

    return predicted_squares


# print(get_predicted_squares())
# squares[38].show()
# squares[39].show()
# print(predict_image_piece(squares[38]))
# print(predict_image_piece(squares[39]))

"""
'Chess Puzzle Loader'
Idea: First, get the model to check colour of the piece it predicts.
Then, iterate through each part of the board and see which pieces are present.
Once board state is recorded and recognised, put this into the chess game
and begin playing from whatever image is passed in.
"""