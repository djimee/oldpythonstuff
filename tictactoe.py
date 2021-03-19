import random

# displays the current tic-tac-toe board
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])

# takes a player input, assigning their marker as 'X' or 'O'
def player_input():
    marker = ''

    while marker not in ['X', 'O']:
        marker = input('Player 1, choose X or O: ')
        if marker not in ['X', 'O']:
            print('Invalid input, enter \'X\' or \'O\'')

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

# assigns marker to board given the position
def place_marker(board, marker, position):
    board[position] = marker

# takes in a board and mark and checks to see if it has won
# VERY BAD I KNOW
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# randomly decides which player goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# checks if there is a free space on a certain board position, prints true if there is space
def space_check(board, position):
    return board[position] == ' '

# checks if board has any empty spaces
def full_board_check(board):
    return ' ' not in board

# takes user input for players next position, N.B. 1-9 correspond to keypad numbers/positions
def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position, 1-9: '))
        if not space_check(board, position):
            print('This space is already taken, choose another one!')

    return position

# asks the player if they want to play again, returns True if they do
def replay():
    choice = 'random'
    while choice not in ['Y', 'N']:
        choice = input('Do you want to play again? ')
        if choice == 'Y':
            return True
        else:
            return False

# main method
def __main__(): 
    print('Tic-Tac-Toe!')

    while True:
        game_playing = True
        game_board = [' '] * 10
        p1_marker, p2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first')

        while game_playing:
            # player 1's go
            if turn == 'Player 1':
                display_board(game_board)
                position = player_choice(game_board)
                place_marker(game_board, p1_marker, position)

                if win_check(game_board, p1_marker):
                    display_board(game_board)
                    print('You win!')
                    game_playing = False
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print('It\'\s a draw!')
                        break
                    else:
                        turn = 'Player 2'
            
            # player 2's go
            else:
                display_board(game_board)
                position = player_choice(game_board)
                place_marker(game_board, p2_marker, position)

                if win_check(game_board, p2_marker):
                    display_board(game_board)
                    print('You win!')
                    game_playing = False
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print('It\'\s a draw!')
                        break
                    else:
                        turn = 'Player 1'
        
        if not replay():
            break

__main__()
