from possibleMoves import ChessBoard
# from testingFile import get_predicted_squares

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

def get_piece_moves(piece, colour: str):
    match piece[0].split()[1]:
        case "pawn":
            if colour == "white":
                return chessboard.get_white_pawn_moves(piece)
            else:
                return chessboard.get_black_pawn_moves(piece)
        case "bishop":
            return chessboard.get_bishop_moves(piece, colour)
        case "knight":
            return chessboard.get_knight_moves(piece, colour)
        case "rook":
            return chessboard.get_rook_moves(piece, colour)
        case "queen":
            return chessboard.get_queen_moves(piece, colour)
        case "king":
            return chessboard.get_king_moves(piece, colour)

def get_legal_moves(board: ChessBoard, current_player: str):
    pieces = board.get_white_pieces() if current_player == "white" else board.get_black_pieces()
    legal_moves = []

    for piece in pieces:
        legal_moves.append(get_piece_moves(piece, current_player))

    return legal_moves

def minimax_alpha_beta(board: ChessBoard, depth: int, current_player: str, alpha, beta):
    if depth == 0: return board.evaluate_board(current_player)
    opposite_colour = "white" if current_player == "black" else "black"

    legal_moves = get_legal_moves(board, current_player)

    best_score = float('-inf') if current_player == "white" else float('inf')
    best_move = None
    for list_moves in legal_moves:
        for move in list_moves:
            start, end = move
            piece_name = board.get_current_board()[start[0]][start[1]]
            new_board = board.apply_move(piece_name, move=move)
            score = -minimax_alpha_beta(new_board, depth - 1, opposite_colour, -beta, -alpha)
            if current_player == "white":
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            else:
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, score)
                if beta <= alpha:
                    break
    print(best_move)

    return best_score

    # if best_move is None:
    #     return best_score
    # else:
    #     return best_score, best_move

# chessboard.apply_move("white knight", [(4, 4), (5, 6)])
# print(minimax_alpha_beta(chessboard, 2, "white", float('-inf'), float('inf')))
print(get_legal_moves(chessboard, "white"))

# NEED TO FIX TO DISALLOW KING CAPTURE