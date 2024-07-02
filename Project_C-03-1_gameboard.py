#this code is create by M23W7502_ThetPaingOo
def show_board(board):

    if len(board) != 9:
        raise ValueError("The board must be a list of 9 elements.")

    display_board = []
    for value in board:
        if value == 0:
            display_board.append('-')
        elif value == 1:
            display_board.append('O')
        elif value == 2:
            display_board.append('X')
        else:
            raise ValueError("Board values must be 0, 1, or 2.")
  
    for i in range(0, 9, 3):
        print(" ".join(display_board[i:i+3]))

board = [0, 1, 2, 1, 2, 0, 2, 0, 1]
show_board(board)
