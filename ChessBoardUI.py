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
                # resize and place the piece images onto the squares
                if row == 0 or row == 7:
                    if col == 0 or col == 7:
                        piece_image_file = 'blackRook.png' if row == 0 else 'whiteRook.png'
                    elif col == 1 or col == 6:
                        piece_image_file = 'blackKnight.png' if row == 0 else 'whiteKnight.png'
                    elif col == 2 or col == 5:
                        piece_image_file = 'blackBishop.png' if row == 0 else 'whiteBishop.png'
                    elif col == 3:
                        piece_image_file = 'blackQueen.png' if row == 0 else 'whiteQueen.png'
                    else:
                        piece_image_file = 'blackKing.png' if row == 0 else 'whiteKing.png'
                elif row == 1 or row == 6:
                    piece_image_file = 'blackPawn.png' if row == 1 else 'whitePawn.png'
                else:
                    continue  # no piece image to place on this square
                
                piece_image_path = os.path.join('pieceImagesGUI', piece_image_file)
                piece_image = Image.open(piece_image_path)
                piece_image = piece_image.resize((50, 50), Image.ANTIALIAS)
                piece_image_tk = ImageTk.PhotoImage(piece_image)
                
                square.create_image(0, 0, image=piece_image_tk, anchor=tk.NW)
                square.piece_image_tk = piece_image_tk  # save a reference to the image to prevent garbage collection

    def _draw_pieces(self):
        pass
