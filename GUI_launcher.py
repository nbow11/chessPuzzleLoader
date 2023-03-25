import tkinter as tk
from ChessBoardUI import ChessBoardUI
from possibleMoves import ChessBoard
from chessBot import minimax_alpha_beta, get_legal_moves
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

chessboard = ChessBoard(example_squares)

def launch_GUI(pieces):
    # Create the top panel for the chess board
    board_panel = ChessBoardUI(root)

    # print(get_legal_moves(chessboard, "white"))

    # print(moves)
    # chessboard.apply_move()
    # chessboard.apply_move([(0, 4), (1, 4)])
    # chessboard.apply_move([(4, 4), (5, 2)])
    board_panel.draw_pieces(pieces)
    board_panel.pack(side=tk.TOP)

    # Create the bottom panel for the chess moves
    moves_panel = tk.Frame(root, width=400, height=150, bg='light gray')
    moves_panel.pack(side=tk.BOTTOM)

    # Add widgets to the panels (e.g., chess board and moves)

    # Start the GUI event loop
    root.mainloop()

chessboard.apply_move([(7, 3), (1, 3)])

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
print(get_legal_moves(chessboard, "black"))
print(chessboard.get_current_board()[1][3])
launch_GUI(chessboard.get_current_board())

# FIX ROOK NOT BEING TAKEN BY ANY PIECES IN THE LEGAL MOVES GENERATOR


pieces_present = {}
opponent_pieces = chessboard.get_black_pieces()

for piece in opponent_pieces:
    c, name = piece[0].split()
    if name != "king":
        if name not in pieces_present:
            pieces_present[name] = 1
        else:
            pieces_present[name] = pieces_present[name] + 1

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