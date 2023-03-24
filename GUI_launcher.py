import tkinter as tk
from ChessBoardUI import ChessBoardUI
from testingFile import get_predicted_squares

# Create the main window
root = tk.Tk()

puzzle_squares = get_predicted_squares()

# Create the top panel for the chess board
board_panel = ChessBoardUI(root)
board_panel.draw_pieces(puzzle_squares)
board_panel.pack(side=tk.TOP)

# Create the bottom panel for the chess moves
moves_panel = tk.Frame(root, width=400, height=150, bg='light gray')
moves_panel.pack(side=tk.BOTTOM)

# Add widgets to the panels (e.g., chess board and moves)

# Start the GUI event loop
root.mainloop()