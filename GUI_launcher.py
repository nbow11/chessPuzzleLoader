import tkinter as tk
from ChessBoardUI import ChessBoardUI
from chessBoardObject import ChessBoard
from tkinter import filedialog
from PIL import ImageTk, Image
# from testingFile import split_image, get_predicted_squares
from chessBot import minimax_alpha_beta, get_legal_moves, is_check_mate
import random
import itertools
# from testingFile import get_predicted_squares

# Create the main window
root = tk.Tk()

# puzzle_squares = get_predicted_squares()

example_squares = [
    ['blank', 'blank', 'blank', 'blank', 'black king', 'black bishop', 'black rook', 'blank'], 
    ['blank', 'black rook', 'blank', 'black knight', 'blank', 'blank', 'blank', 'blank'], 
    ['black pawn', 'blank', 'blank', 'blank', 'black pawn', 'black pawn', 'blank', 'blank'], 
    ['blank', 'black pawn', 'black pawn', 'blank', 'black pawn', 'blank', 'blank', 'black pawn'], 
    ['blank', 'blank', 'blank', 'blank', 'white knight', 'blank', 'blank', 'blank'], 
    ['blank', 'blank', 'blank', 'blank', 'blank', 'white knight', 'blank', 'blank'], 
    ['white pawn', 'white pawn', 'white pawn', 'blank', 'blank', 'white pawn', 'white pawn', 'white pawn'], 
    ['blank', 'blank', 'blank', 'white rook', 'white rook', 'blank', 'white king', 'blank']
]

CURRENT_PLAYER = True

chessboard = None

board_image = None

# def open_image():
#     global board_image
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         img = Image.open(file_path).convert("RGB")
#         img = img.resize((250, 250), Image.ANTIALIAS)
#         board_image = img
#         photo = ImageTk.PhotoImage(img)
#         image_label.config(image=photo)
#         image_label.image = photo  # Keep a reference to the image to prevent garbage collection
#         save_button.config(state=tk.NORMAL)

predicted_squares = None

# def save_image():
#     global predicted_squares
#     squares = split_image(board_image=board_image)
#     predicted_squares = get_predicted_squares(squares)
#     for widget in root.winfo_children():
#         widget.destroy()
#     launch_GUI(predicted_squares)

# open_button = tk.Button(root, text="Open image", command=open_image)
# open_button.pack()

# image_label = tk.Label(root)
# image_label.pack()

# save_button = tk.Button(root, text="Confirm", command=save_image, state=tk.DISABLED)
# save_button.pack()

def launch_GUI(pieces):
    # Create the top panel for the chess board
    global chessboard
    chessboard = ChessBoard(pieces)
    board_panel = ChessBoardUI(root)

    board_panel.draw_pieces(pieces)
    board_panel.pack(side=tk.TOP)

    # Create the bottom panel for the chess moves
    moves_panel = tk.Frame(root, width=400, height=150, bg='light gray')
    button = tk.Button(moves_panel, text="Next move", command=lambda: button_click())

    button.pack()
    moves_panel.pack(side=tk.BOTTOM)

def redraw():
    global CURRENT_PLAYER
    
    which_player = "white" if CURRENT_PLAYER == True else "black"

    recommended_move, _ = minimax_alpha_beta(chessboard, 2, True, which_player)
    # print(recommended_move)
    recommended_start, recommended_end = recommended_move
    chessboard.apply_move([recommended_start, recommended_end])

    CURRENT_PLAYER = not CURRENT_PLAYER

    for widget in root.winfo_children():
        if isinstance(widget, ChessBoardUI):
            widget.destroy()

    # create a new ChessBoardUI instance with the given pieces
    board = ChessBoardUI(root)
    board.draw_pieces(chessboard.get_current_board())
    board.pack()

def button_click():
    redraw()
    root.after(2000, button_click)

launch_GUI(example_squares)

root.mainloop()
# chessboard.apply_move([(0, 6), (3, 6)])

# chessboard.apply_move([(0, 4), (1, 3)])

# chessboard.apply_move([(4, 4), (2, 5)])
# print(chessboard.evaluate_board("white"))
# print(minimax_alpha_beta(chessboard, 2, "white"))
# chessboard.apply_move([(7, 3), (1, 3)])
# print(minimax_alpha_beta(chessboard, 2, "black"))
# chessboard.apply_move([(0, 4), (1, 4)])

# chessboard.apply_move([(1, 3), (1, 1)])
# print(minimax_alpha_beta(chessboard, 2, "white"))
# chessboard.apply_move([(7, 4), (6, 4)])
# for piece in chessboard.get_black_pieces():
#     if piece[0] == "black king":
#         print(chessboard.get_piece_moves(piece, "black"))
# print(get_legal_moves(chessboard, "black"))
# print(chessboard.get_current_board()[1][3])
# launch_GUI(chessboard.get_current_board())

# FIX ROOK NOT BEING TAKEN BY ANY PIECES IN THE LEGAL MOVES GENERATOR


# pieces_present = {}
# opponent_pieces = chessboard.get_black_pieces()

# for piece in opponent_pieces:
#     c, name = piece[0].split()
#     if name != "king":
#         if name not in pieces_present:
#             pieces_present[name] = 1
#         else:
#             pieces_present[name] = pieces_present[name] + 1

# print(f"black: {pieces_present}")

# pieces_present1 = {}
# opponent_pieces1 = chessboard.get_white_pieces()

# for piece in opponent_pieces1:
#     c, name = piece[0].split()
#     if name != "king":
#         if name not in pieces_present1:
#             pieces_present1[name] = 1
#         else:
#             pieces_present1[name] = pieces_present1[name] + 1
# print(f"white: {pieces_present1}")