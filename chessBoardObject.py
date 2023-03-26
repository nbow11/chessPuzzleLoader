from typing import *

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

PIECE_WEIGHTS = {
    "pawn": 10, "bishop": 30, "knight": 30, "rook": 50, "queen": 90, "king": 100
}

get_piece_coordinates = lambda piece: piece[1]

class ChessBoard:
    def __init__(self, board):
        self.board = board
        self.white_pieces, self.black_pieces = [], []
        self.set_pieces()

    def set_pieces(self):
        self.white_pieces, self.black_pieces = [], []
        for i in range(8):
            for j in range(8):
                if self.get_current_board()[i][j] != "blank":
                    if self.board[i][j].split()[0] == "white":
                        self.get_white_pieces().append([self.get_current_board()[i][j], (i, j)])
                    else:
                        self.get_black_pieces().append([self.get_current_board()[i][j], (i, j)])

    def get_current_board(self):
        return self.board

        return self.new_board

    def get_white_pieces(self):
        return self.white_pieces
    
    def get_black_pieces(self):
        return self.black_pieces

    def get_black_pawn_moves(self, piece):
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
        if j > 0 and self.get_current_board()[i+1][j-1].startswith('white') and self.get_current_board()[i+1][j-1] != "white king":
            possible_moves.append((position, (i+1, j-1)))
        if j < 7 and self.get_current_board()[i+1][j+1].startswith('white') and self.get_current_board()[i+1][j-1] != "white king":
            possible_moves.append((position, (i+1, j+1)))

        return possible_moves

    def get_white_pawn_moves(self, piece):
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
        if j > 0 and self.get_current_board()[i-1][j-1].startswith('black') and self.get_current_board()[i-1][j-1] != "black king":
            possible_moves.append((position, (i-1, j-1)))
        if j < 7 and self.get_current_board()[i-1][j+1].startswith('black') and self.get_current_board()[i-1][j+1] != "black king":
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
            elif self.get_current_board()[r][j].startswith(opposite_colour) and self.get_current_board()[r][j] != f"{opposite_colour} king":
                possible_moves.append((position, (r, j)))
                break
            else:
                break
        # Check possible moves in downward direction
        for r in range(i+1, 8):
            if self.get_current_board()[r][j] == 'blank':
                possible_moves.append((position, (r, j)))
            elif self.get_current_board()[r][j].startswith(opposite_colour) and self.get_current_board()[r][j] != f"{opposite_colour} king":
                possible_moves.append((position, (r, j)))
                break
            else:
                break
        # Check possible moves in left direction
        for c in range(j-1, -1, -1):
            if self.get_current_board()[i][c] == 'blank':
                possible_moves.append((position, (i, c)))
            elif self.get_current_board()[i][c].startswith(opposite_colour) and self.get_current_board()[r][j] != f"{opposite_colour} king":
                possible_moves.append((position, (i, c)))
                break
            else:
                break
        # Check possible moves in right direction
        for c in range(j+1, 8):
            if self.get_current_board()[i][c] == 'blank':
                possible_moves.append((position, (i, c)))
            elif self.get_current_board()[i][c].startswith(opposite_colour) and self.get_current_board()[r][j] != f"{opposite_colour} king":
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
            elif self.get_current_board()[r][c].startswith(opposite_colour) and self.get_current_board()[r][j] != f"{opposite_colour} king":
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
            elif self.get_current_board()[r][c].startswith(opposite_colour) and self.get_current_board()[r][j] != f"{opposite_colour} king":
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
            elif self.get_current_board()[r][c].startswith(opposite_colour) and self.get_current_board()[r][j] != f"{opposite_colour} king":
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
            elif self.get_current_board()[r][c].startswith(opposite_colour) and self.get_current_board()[r][j] != f"{opposite_colour} king":
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
                    if self.get_current_board()[r][j] != f"{opposite_colour} king":
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
        for move in self.get_rook_moves(piece, colour):
            possible_moves.append(move)
        for move in self.get_bishop_moves(piece, colour):
            possible_moves.append(move)

        return possible_moves

    def get_piece_moves(self, piece, colour: str):
        match piece[0].split()[1]:
            case "pawn":
                if colour == "white":
                    return self.get_white_pawn_moves(piece)
                else:
                    return self.get_black_pawn_moves(piece)
            case "bishop":
                return self.get_bishop_moves(piece, colour)
            case "knight":
                return self.get_knight_moves(piece, colour)
            case "rook":
                return self.get_rook_moves(piece, colour)
            case "queen":
                return self.get_queen_moves(piece, colour)
            case "king":
                return self.get_king_moves(piece, colour)

    def get_capturable_pieces(self, moves):

        capturable_pieces = []
        for move in moves:
            initial, end = move
            i, j = end

            if self.get_current_board()[i][j] != "blank":
                capturable_pieces.append((self.get_current_board()[i][j], (i, j)))

        return capturable_pieces
    
    def assess_double_pawns(self, colour: str) -> int:
        DOUBLE_PENALTY = -2
        double_score = 0
        double_count = {}
        
        for row in range(8):
            for col in range(8):
                piece = self.get_current_board()[row][col]
                if piece != "blank":
                    piece_colour, piece_name = piece.split()
                    if piece is not None and piece_colour == colour and piece_name == "pawn":
                        if col in double_count:
                            double_count[col] += 1
                        else:
                            double_count[col] = 0
        
        for value in double_count.values():
            if value >= 1:
                double_score += value * DOUBLE_PENALTY
        
        return double_score

    def evaluate_pawn_structure(self, colour: str):
        pawn_structure_value = 0
        opposite_colour = "white" if colour == "black" else "white"

        for row in range(8):
            for col in range(8):
                piece = self.get_current_board()[row][col]
                if piece != "blank":
                    piece_colour, piece_name = piece.split()
                    if piece is not None and piece_colour == colour and piece_name == "pawn":
                        if (colour == "black" and row == 6) or (colour == "white" and row == 1):
                            pawn_structure_value += 5
                        elif row == 2 or row == 5:
                            pawn_structure_value += 3
                        elif row == 3 or row == 4:
                            if opposite_colour == "white":
                                if len(self.get_white_pieces()) < 7:
                                    pawn_structure_value += 3
                            else:
                                if len(self.get_black_pieces()) < 7:
                                    pawn_structure_value += 3
                        else:
                            pawn_structure_value += 1

        return pawn_structure_value + self.assess_double_pawns(colour)

    def evaluate_board_material(self, colour: str) -> int:
        TOTAL_PIECES_VALUE = 39
        pieces_present = {}
        pieces_present_value = 0
        opponent_pieces = self.get_white_pieces() if colour == "black" else self.get_black_pieces()
        
        for piece in opponent_pieces:
            c, name = piece[0].split()
            if name != "king":
                if name not in pieces_present:
                    pieces_present[name] = 1
                else:
                    pieces_present[name] = pieces_present[name] + 1

        for piece, value in pieces_present.items():
            pieces_present_value += PIECE_WEIGHTS[piece] * value
        
        return TOTAL_PIECES_VALUE - pieces_present_value

    def evaluate_board(self, colour) -> int:
        total_score = self.evaluate_board_material(colour) + self.evaluate_pawn_structure(colour)

        return total_score

    def apply_move(self, move: List[Tuple[int, int]]):
        start_i, start_j = move[0]
        end_i, end_j = move[1]

        piece_name = self.get_current_board()[start_i][start_j]

        if piece_name != "blank":
            self.get_current_board()[start_i][start_j] = "blank"
            colour = piece_name.split()[0]
            if end_i == 0 and piece_name == "white pawn" or end_i == 7 and piece_name == "black pawn":
                self.get_current_board()[end_i][end_j] = f"{colour} queen"
            else:
                self.get_current_board()[end_i][end_j] = piece_name
            self.set_pieces()


# chessboard = ChessBoard(example_squares)

# chessboard.apply_move([(7, 3), (1, 3)]) 
# chessboard.apply_move([(0, 6), (6, 6)]) 
# print(chessboard.get_capturable_pieces())
# chessboard.apply_move([(4, 4), (2, 3)])
# chessboard.apply_move([(7, 3), (1, 3)])
# print(chessboard.evaluate_board_material("white"))

# FIX EVALUATE BOARD -> NEEDS TO SEE THAT A MOVE MAXIMISES ITS SCORE
# ATM, IT ONLY IS SEEING A CONSTANT SCORE


# print(example_squares[5][6])
# for piece in chessboard.get_white_pieces():
#     if piece[0].startswith("white rook"):
#         print(chessboard.get_rook_moves(piece, "white"))

# print(chessboard.evaluate_board("white"))

# for piece in chessboard.get_white_pieces():
#     if piece[0].split()[1] == "pawn":
#         moves = chessboard.get_white_pawn_moves(piece)
#         print(chessboard.get_capturable_pieces(moves))