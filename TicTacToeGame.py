board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display_board():
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('---+---+---')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('---+---+---')
    print(f' {board[1]} | {board[2]} | {board[3]}')

def handle_turn(player):
    print(f"{player}'s turn.")
    position = input('Choose a position from 1-9: ')

    valid = False
    while not valid:

        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input('Are u mad G? Insert an apropriet answer blud! Choose ur position fam from 1-9: ')
            
        position = int(position)
        if board[position] == ' ':
            valid = True
        else:
            print("U tweaking bruv, come again!")
    board[position] = player
    display_board()

def check_win():
    return ((board[1] == board[2] == board[3] and board[1] != ' ') or 
    (board[4] == board[5] == board[6] and board[4] != ' ') or 
    (board[7] == board[8] == board[9] and board[7] != ' ') or 
    (board[1] == board[4] == board[7] and board[1] != ' ') or 
    (board[2] == board[5] == board[8] and board[2] != ' ') or 
    (board[3] == board[6] == board[9] and board[3] != ' ') or 
    (board[1] == board[5] == board[9] and board[1] != ' ') or 
    (board[3] == board[5] == board[7] and board[3] != ' ')) 

def check_tie():
    if ' ' not in board:
        return True
    else:
        return False

def play_game():
    player1 = input("Wagwarn Bossman, make a choice innit X or O: ")
    while player1 not in ['X','O']:
        player1 = input("U dumb blud or what!? choose X or O: ")
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    display_board()
    while not check_win():
        handle_turn(player1)
        if check_win():
            print(f"{player1} Chefed his op up with a rambo!")
            break
        elif check_tie():
            print("Nobody got chinked, rematch!")
            break
        handle_turn(player2)
        if check_win():
            print(f"{player2} Obliterated his op")
            break
play_game()