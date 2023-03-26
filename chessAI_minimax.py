from chessBoardEntity import ChessBoard
from copy import deepcopy
import math
# from GUI_launcher import launch_GUI

# from testingFile import get_predicted_squares

example_squares = [
    ['blank', 'blank', 'blank', 'blank', 'black king', 'black bishop', 'black rook', 'blank'], 
    ['blank', 'black rook', 'blank', 'black knight', 'blank', 'blank', 'black queen', 'blank'], 
    ['black pawn', 'blank', 'blank', 'blank', 'black pawn', 'black pawn', 'blank', 'blank'], 
    ['blank', 'black pawn', 'black pawn', 'blank', 'black pawn', 'blank', 'blank', 'black pawn'], 
    ['blank', 'blank', 'blank', 'blank', 'white knight', 'blank', 'blank', 'blank'], 
    ['blank', 'blank', 'blank', 'blank', 'blank', 'white knight', 'blank', 'blank'], 
    ['white pawn', 'white pawn', 'white pawn', 'blank', 'blank', 'white pawn', 'white pawn', 'white pawn'], 
    ['blank', 'blank', 'blank', 'white rook', 'white rook', 'blank', 'white king', 'blank']
]

PIECE_WEIGHTS = {
    "pawn": 1, "bishop": 3, "knight": 3, 
    "rook": 5, "queen": 9, "king": 100
}

# puzzle_squares = get_predicted_squares()
chessboard = ChessBoard(example_squares)

def get_best_capture():
    maximum = 0
    capturable_piece = ""

    for piece in chessboard.get_white_pieces():
        moves = []
        match piece[0].split()[1]:
            case "pawn":
                moves = chessboard.get_white_pawn_moves(piece)
            case "bishop":
                moves = chessboard.get_bishop_moves(piece, "white")
            case "knight":
                moves = chessboard.get_knight_moves(piece, "white")
            case "rook":
                moves = chessboard.get_rook_moves(piece, "white")
            case "queen":
                moves = chessboard.get_queen_moves(piece, "white")
            case "king":
                moves = chessboard.get_king_moves(piece, "white")

        for capturable in chessboard.get_capturable_pieces(moves):
            piece_type = capturable[0].split()[1]
            if PIECE_WEIGHTS[piece_type] > maximum:
                maximum = PIECE_WEIGHTS[piece_type]
                capturable_piece = f"{piece_type} at {capturable[1]} by {piece}"

    return (capturable_piece, maximum)

def get_legal_moves(board: ChessBoard, requested_colour: str, current_player: str):
    pieces = board.get_white_pieces() if requested_colour == "white" else board.get_black_pieces()
    legal_moves = []

    for piece in pieces:
        legal_moves.append(board.get_piece_moves(piece, requested_colour, current_player))

    return legal_moves

def is_check_mate(legal_moves):
    checkmate = True

    for moves in legal_moves:
        if moves != []:
            checkmate = False
    
    return checkmate

def minimax_alpha_beta(board: ChessBoard, depth: int, maximising_player: bool, 
                       requested_colour: str, alpha=-math.inf, beta=math.inf):
    
    if depth == 0 or board.is_checkmate():
        return None, board.evaluate_board(requested_colour)
    
    opposing_colour = "white" if requested_colour == "black" else "white"

    if maximising_player:
        legal_moves = get_legal_moves(board, requested_colour, requested_colour)
        if legal_moves == None: return
        best_move = None
        max_eval = -math.inf
        for list_moves in legal_moves:
            for move in list_moves:
                # Create a copy of the board
                board_copy = deepcopy(board)
                # Apply the move to the copy
                board_copy.apply_move(move=move)
                # Recursively call the function with the board copy
                _, eval = minimax_alpha_beta(board_copy, depth - 1, False, requested_colour, alpha, beta)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if alpha >= beta:
                    break
        return best_move, max_eval
    else:
        legal_moves = get_legal_moves(board, opposing_colour, opposing_colour)
        if legal_moves == None: return
        best_move = None
        min_eval = math.inf
        for list_moves in legal_moves:
            for move in list_moves:
                # Create a copy of the board
                board_copy = deepcopy(board)
                # Apply the move to the copy
                board_copy.apply_move(move=move)
                # Recursively call the function with the board copy
                _, eval = minimax_alpha_beta(board_copy, depth - 1, True, requested_colour, alpha, beta)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return best_move, min_eval
    

# for piece in chessboard.get_white_pieces():
#     if piece[0] == "white king":
#         print(chessboard.is_king_in_check(piece[1], piece))
# print(get_legal_moves(chessboard, "white", "white"))
# chessboard.apply_move([(7, 3), (1, 3)])
# print(chessboard.evaluate_player_checkmate("white"))
# for list_moves in get_legal_moves(chessboard, "black"):
#     print(chessboard.get_capturable_pieces(list_moves))
# chessboard.apply_move([(0, 4), (1, 3)])
# print(chessboard.evaluate_board("black"))
# print(get_legal_moves(chessboard, "black"))
print(minimax_alpha_beta(chessboard, 2, True, "white"))
# chessboard.apply_move([(4, 4), (5, 6)])
# chessboard.apply_move([(1, 6), (6, 6)])
# print(minimax_alpha_beta(chessboard, 2, True, "white"))
# print(chessboard.does_player_have_checkmate("black"))
# print(chessboard.evaluate_opponent_checkmate("white"))
# chessboard.apply_move([(7, 3), (1, 3)]) 
# chessboard.apply_move([(0, 6), (6, 6)]) 
# chessboard.apply_move([(4, 4), (3, 2)]) 
# print(chessboard.evaluate_board_material("black"))
# print(minimax_alpha_beta(chessboard, 2, True, "white"))
# print(minimax_alpha_beta(chessboard, 1, "white"))

# for list_move in get_legal_moves(chessboard, "white"):
#     for move in list_move:
#         print(move)
# chessboard.apply_move([(4, 4), (5, 6)])
# print(chessboard.evaluate_board("white"))
# for list_moves in get_legal_moves(chessboard, "white"):
#     for move in list_moves:
#         print(move)
# print(minimax_alpha_beta(chessboard, 3, "white"))

# print(get_legal_moves(chessboard, "white"))
# legal_moves = get_legal_moves(chessboard, "white")
# for list_moves in legal_moves:
#         for move in list_moves:
#             print(move)

# NEED TO FIX TO DISALLOW KING CAPTURE