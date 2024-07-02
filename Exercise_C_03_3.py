#Group5

#M23W7502_ThetPaingOo
#M23W7314_Gurung_Bishwas
#M24W0387_TAMANG_ARBIN
#M24WO246 alish_maharjan
#M23W7640 Krishna Rohan
#M24W0197 _pramod rakendu parvathy

def show_board(board):
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

def is_win(board, player):
    for row in range(0, 9, 3):
        if board[row] == board[row + 1] == board[row + 2] == player:
            return True
    for col in range(3):
        if board[col] == board[col + 3] == board[col + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    
    return False

def show_placeable_locations(board):
    placeable_locations = [i for i, value in enumerate(board) if value == 0]
    print("Remaining placeable locations:", placeable_locations)

def play_game():
    board = [0] * 9
    current_player = 1 
    
    for turn in range(9):
        show_board(board)
        show_placeable_locations(board)
        print(f"Player {current_player}'s turn.")
        while True:
            try:
                move = int(input("Enter your move (0-8): "))
                if board[move] == 0:
                    board[move] = current_player
                    break
                else:
                    print("Invalid move. The cell is already occupied.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 0 and 8.")
        
        if is_win(board, current_player):
            show_board(board)
            print(f"Player {current_player} wins!")
            return
        
        current_player = 2 if current_player == 1 else 1 
    
    show_board(board)
    print("It's a draw!")

play_game()
