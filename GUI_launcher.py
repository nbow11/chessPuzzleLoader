import tkinter as tk
from ChessBoardUI import ChessBoardUI

# Create the main window
root = tk.Tk()

# Create the top panel for the chess board
board_panel = ChessBoardUI(root)
board_panel.pack(side=tk.TOP)

# Create the bottom panel for the chess moves
moves_panel = tk.Frame(root, width=400, height=150, bg='light gray')
moves_panel.pack(side=tk.BOTTOM)

# Add widgets to the panels (e.g., chess board and moves)

# Start the GUI event loop
root.mainloop()