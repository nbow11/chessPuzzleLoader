from PIL import Image
import os
import cv2
import uuid

# define input and output directories
image_path = "newBoards/board7.png"

def split_chessboard(image_path):
    # Load the image
    img = Image.open(image_path).convert("RGB")
    
    # Split the image into 64 squares
    squares = []
    width, height = img.size
    square_size = min(width, height) // 8
    for i in range(8):
        for j in range(8):
            x, y = j * square_size, i * square_size
            square = img.crop((x, y, x + square_size, y + square_size))
            square = square.resize((85, 85))
            squares.append(square)
    
    return squares

squares = split_chessboard(image_path)

# Define a list of piece names without color
piece_names = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']

# Loop through the images in squares and add them to the corresponding folder
for i, img in enumerate(squares):
    piece_uuid = uuid.uuid4()
    # Check if the index is in the range of pieces with index 0-15 and 48-63
    if i in range(8):
        # Get the folder name for the piece
        piece_name = piece_names[i]

        # Create the folder if it does not exist
        folder_path = f"chessImageData/{piece_name}"
        os.makedirs(folder_path, exist_ok=True)

        # Save the image to the folder
        img.save(os.path.join(folder_path, f"{piece_uuid}.png"))
    elif i in range(8, 16) or i in range(48, 56):
        # Get the folder name for the piece
        piece_name = "pawn"

        # Create the folder if it does not exist
        folder_path = f"chessImageData/{piece_name}"
        os.makedirs(folder_path, exist_ok=True)

        # Save the image to the folder
        img.save(os.path.join(folder_path, f"{piece_uuid}.png"))
    
    elif i in range(56, 64):
        # Get the folder name for the piece
        index = lambda n: n - 56
        piece_name = piece_names[index(i)]

        # Create the folder if it does not exist
        folder_path = f"chessImageData/{piece_name}"
        os.makedirs(folder_path, exist_ok=True)

        # Save the image to the folder
        img.save(os.path.join(folder_path, f"{piece_uuid}.png"))