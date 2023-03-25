import tkinter as tk
from ChessBoardUI import ChessBoardUI
from possibleMoves import ChessBoard
from chessBot import get_legal_moves
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

# Create the top panel for the chess board
board_panel = ChessBoardUI(root)

print(get_legal_moves(chessboard, "white"))

# print(moves)
# chessboard.apply_move()
# chessboard.apply_move([(0, 4), (1, 4)])
# chessboard.apply_move([(4, 4), (5, 2)])
board_panel.draw_pieces(chessboard.get_current_board())
board_panel.pack(side=tk.TOP)

# Create the bottom panel for the chess moves
moves_panel = tk.Frame(root, width=400, height=150, bg='light gray')
moves_panel.pack(side=tk.BOTTOM)

# Add widgets to the panels (e.g., chess board and moves)

# Start the GUI event loop
root.mainloop()