from typing import *

example_squares = [
    ['blank', 'blank', 'blank', 'blank', 'black queen', 'blank', 'blank', 'blank'], 
    ['white pawn', 'white king', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank'], 
    ['blank', 'blank', 'white rook', 'blank', 'blank', 'blank', 'blank', 'white pawn'], 
    ['blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'white pawn', 'blank'], 
    ['blank', 'white rook', 'blank', 'blank', 'blank', 'blank', 'black pawn', 'black pawn'], 
    ['blank', 'blank', 'blank', 'black knight', 'blank', 'blank', 'blank', 'blank'], 
    ['black king', 'black pawn', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank'], 
    ['blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank', 'blank']
]

get_piece_coordinates = lambda piece: piece[1]

class ChessBoard:
    def __init__(self, board):
        self.board = board
        self.white_pieces, self.black_pieces = [], []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != "blank":
                    if self.board[i][j].split()[0] == "white":
                        self.white_pieces.append([example_squares[i][j], (i, j)])
                    else:
                        self.black_pieces.append([example_squares[i][j], (i, j)])

    def get_current_board(self):
        return self.board
    
    def get_white_pieces(self):
        return self.white_pieces
    
    def get_black_pieces(self):
        return self.black_pieces

    def get_white_pawn_moves(self, piece):
        possible_moves = []
        position = get_piece_coordinates(piece)
        i, j = position
        # Check if pawn can move one or two steps forward
        if i == 1 and self.get_current_board()[i+1][j] == 'blank' and self.get_current_board()[i+2][j] == 'blank':
            if self.get_current_board()[i+1][j] == 'blank':  # check if square in front of pawn is empty
                possible_moves.append((position, (i+1, j)))
            possible_moves.append((position, (i+2, j)))
        elif self.get_current_board()[i+1][j] == 'blank':
            possible_moves.append((position, (i+1, j)))
        # Check if pawn can capture diagonally
        if j > 0 and self.get_current_board()[i+1][j-1].startswith('black') and self.get_current_board()[i+1][j-1] != "black king":
            possible_moves.append((position, (i+1, j-1)))
        if j < 7 and self.get_current_board()[i+1][j+1].startswith('black') and self.get_current_board()[i+1][j-1] != "black king":
            possible_moves.append((position, (i+1, j+1)))

        return possible_moves

    def get_black_pawn_moves(self, piece):
        possible_moves = []
        position = get_piece_coordinates(piece)
        i, j = position
        # Check if pawn can move one or two steps forward
        if i == 6 and self.get_current_board()[i-1][j] == 'blank' and self.get_current_board()[i-2][j] == 'blank':
            if self.get_current_board()[i-1][j] == 'blank':  # check if square in front of pawn is empty
                possible_moves.append((position, (i-1, j)))
            possible_moves.append((position, (i-2, j)))
        elif self.get_current_board()[i-1][j] == 'blank':
            possible_moves.append((position, (i-1, j)))
        # Check if pawn can capture diagonally
        if j > 0 and self.get_current_board()[i-1][j-1].startswith('white') and self.get_current_board()[i-1][j-1] != "white king":
            possible_moves.append((position, (i-1, j-1)))
        if j < 7 and self.get_current_board()[i-1][j+1].startswith('white') and self.get_current_board()[i-1][j+1] != "white king":
            possible_moves.append((position, (i-1, j+1)))

        return possible_moves

    def get_rook_moves(self, piece, colour):

        opposite_colour = "black" if colour == "white" else "white"

        possible_moves = []
        position = get_piece_coordinates(piece)
        i, j = position
        # Check possible moves in upward direction
        for r in range(i-1, -1, -1):
            if self.get_current_board()[r][j] == 'blank':
                possible_moves.append((position, (r, j)))
            elif self.get_current_board()[r][j].startswith(opposite_colour):
                possible_moves.append((position, (r, j)))
                break
            else:
                break
        # Check possible moves in downward direction
        for r in range(i+1, 8):
            if self.get_current_board()[r][j] == 'blank':
                possible_moves.append((position, (r, j)))
            elif self.get_current_board()[r][j].startswith(opposite_colour):
                possible_moves.append((position, (r, j)))
                break
            else:
                break
        # Check possible moves in left direction
        for c in range(j-1, -1, -1):
            if self.get_current_board()[i][c] == 'blank':
                possible_moves.append((position, (i, c)))
            elif self.get_current_board()[i][c].startswith(opposite_colour):
                possible_moves.append((position, (i, c)))
                break
            else:
                break
        # Check possible moves in right direction
        for c in range(j+1, 8):
            if self.get_current_board()[i][c] == 'blank':
                possible_moves.append((position, (i, c)))
            elif self.get_current_board()[i][c].startswith(opposite_colour):
                possible_moves.append((position, (i, c)))
                break
            else:
                break

        return possible_moves

    def get_bishop_moves(self, piece, colour):
        opposite_colour = "black" if colour == "white" else "white"
        possible_moves = []
        position = get_piece_coordinates(piece)
        i, j = position
        # Check possible moves in upper left direction
        r, c = i-1, j-1
        while r >= 0 and c >= 0:
            if self.get_current_board()[r][c] == 'blank':
                possible_moves.append((position, (r, c)))
            elif self.get_current_board()[r][c].startswith(opposite_colour):
                possible_moves.append((position, (r, c)))
                break
            else:
                break
            r, c = r-1, c-1
        # Check possible moves in upper right direction
        r, c = i-1, j+1
        while r >= 0 and c < 8:
            if self.get_current_board()[r][c] == 'blank':
                possible_moves.append((position, (r, c)))
            elif self.get_current_board()[r][c].startswith(opposite_colour):
                possible_moves.append((position, (r, c)))
                break
            else:
                break
            r, c = r-1, c+1
        # Check possible moves in lower left direction
        r, c = i+1, j-1
        while r < 8 and c >= 0:
            if self.get_current_board()[r][c] == 'blank':
                possible_moves.append((position, (r, c)))
            elif self.get_current_board()[r][c].startswith(opposite_colour):
                possible_moves.append((position, (r, c)))
                break
            else:
                break
            r, c = r+1, c-1
        # Check possible moves in lower right direction
        r, c = i+1, j+1
        while r < 8 and c < 8:
            if self.get_current_board()[r][c] == 'blank':
                possible_moves.append((position, (r, c)))
            elif self.get_current_board()[r][c].startswith(opposite_colour):
                possible_moves.append((position, (r, c)))
                break
            else:
                break
            r, c = r+1, c+1

        return possible_moves

    def get_knight_moves(self, piece, colour):
        opposite_colour = "black" if colour == "white" else "white"
        possible_moves = []
        position = get_piece_coordinates(piece)
        i, j = position
        # Check all possible knight moves from current position
        knight_moves = [(i+1,j+2), (i+1,j-2), (i+2,j+1), (i+2,j-1), 
                        (i-1,j+2), (i-1,j-2), (i-2,j+1), (i-2,j-1)]
        for move in knight_moves:
            r, c = move
            if r >= 0 and r < 8 and c >= 0 and c < 8:
                if self.get_current_board()[r][c] == 'blank' or self.get_current_board()[r][c].startswith(opposite_colour):
                    possible_moves.append((position, (r, c)))

        return possible_moves

    def get_king_moves(self, piece, colour):
        opposite_colour = "black" if colour == "white" else "white"
        possible_moves = []
        position = get_piece_coordinates(piece)
        i, j = position
        # Check all possible king moves from current position
        king_moves = [(i+1,j), (i-1,j), (i,j+1), (i,j-1), 
                    (i+1,j+1), (i+1,j-1), (i-1,j+1), (i-1,j-1)]
        for move in king_moves:
            r, c = move
            if r >= 0 and r < 8 and c >= 0 and c < 8:
                if self.get_current_board()[r][c] == 'blank' or self.get_current_board()[r][c].startswith(opposite_colour):
                    # Check if move puts king in check
                    possible_moves.append((position, (r, c)))

        return possible_moves

    def get_queen_moves(self, piece, colour):
        possible_moves = []
        position = get_piece_coordinates(piece)
        i, j = position
        # Check all possible king moves from current position
        for move in self.get_rook_moves(self.get_current_board(), piece, colour):
            possible_moves.append(move)
        for move in self.get_bishop_moves(self.get_current_board(), piece, colour):
            possible_moves.append(move)

        return possible_moves

    def get_capturable_pieces(self, moves):
        capturable_pieces = []
        for move in moves:
            initial, end = move
            i, j = end

            if self.get_current_board()[i][j] != "blank":
                capturable_pieces.append((self.get_current_board()[i][j], (i, j)))

        return capturable_pieces

chessboard = ChessBoard(example_squares)

for piece in chessboard.get_white_pieces():
    if piece[0].startswith("white pawn"):
        print(chessboard.get_white_pawn_moves(piece))



# print(get_possible_moves(example_squares, white_pieces))