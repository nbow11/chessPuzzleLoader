import tkinter as tk
from PIL import Image, ImageTk
import os

class ChessBoardUI(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.brown = '#B58863'
        self.light_brown = '#F0D9B5'
        self._draw_squares()

    def _draw_squares(self):
        # create 64 squares with alternating colors
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = self.light_brown
                else:
                    color = self.brown
                
                square = tk.Canvas(self, width=50, height=50, bg=color, highlightthickness=0)
                square.grid(row=row, column=col)

    def _create_piece_image(self, piece_name):
        """
        Create and return a resized PhotoImage object of the piece image with the given name.
        """
        color, piece = piece_name.split()
        piece_image_file = f'{color.lower()}{piece.title()}.png'
        piece_image_path = os.path.join('pieceImagesGUI', piece_image_file)
        piece_image = Image.open(piece_image_path)
        piece_image = piece_image.resize((50, 50), Image.ANTIALIAS)
        piece_image_tk = ImageTk.PhotoImage(piece_image)
        return piece_image_tk

    def draw_pieces(self, pieces):
        """
        Draw the given pieces onto the board.
        pieces: a list of 8 lists, each containing the names of the pieces to be placed in that row.
        """
        for row, piece_row in enumerate(pieces):
            for col, piece_name in enumerate(piece_row):
                if not piece_name:
                    continue
                
                if piece_name != "blank":
                    piece_image_tk = self._create_piece_image(piece_name)
                    square = self.grid_slaves(row=row, column=col)[0]  # get the canvas square at the given row and col
                    square.create_image(0, 0, image=piece_image_tk, anchor=tk.NW)
                    square.piece_image_tk = piece_image_tk  # save a reference to the image to prevent garbage collection

        self.pieces = pieces  # save a reference to the pieces so we can update them later if needed
