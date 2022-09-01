def display_board(board):
    
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.    
    
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0], "  |  " , board[0][1], "  |  " , board[0][2], "  |" )
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0], "  |  " , board[1][1], "  |  " , board[1][2], "  |" )
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0], "  |  " , board[2][1], "  |  " , board[2][2], "  |" )
    print("|       |       |       |")
    print("+-------+-------+-------+")
    

def enter_move(board):

    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    x = True

    count_i = 0
    count_j = 0

    while x:
        
        print("Please, provide your move")
        g = int(input())

        z = False

        # Switch from g to a count_a and count_b to be able to search thrue board 

        if g == 1:
            count_i = 0
            count_j = 0
            z = True
        elif g == 2:
            count_i = 0
            count_j = 1
            z = True
        elif g == 3:
            count_i = 0
            count_j = 2
            z = True
        elif g == 4:
            count_i = 1
            count_j = 0
            z = True
        elif g == 5:
            count_i = 1
            count_j = 1
            z = True
        elif g == 6:
            count_i = 1
            count_j = 2
            z = True
        elif g == 7:
            count_i = 2
            count_j = 0
            z = True
        elif g == 8:
            count_i = 2
            count_j = 1
            z = True
        elif g == 9:
            count_i = 2
            count_j = 2
            z = True
        else:
            print("Provided number is a wrong number. Provide number that is greater or equal to 1 or smaller or equal to 9")
            continue
        
        # Check if position is free or already taken and take it over if that is possible

        if z:
            if board[count_i][count_j] != "X" and board[count_i][count_j] !=  "O":
                board[count_i][count_j] = "O"
                x = False
            elif board[count_i][count_j] ==  "O":
                print("That position has been already taken by you. Choose another one instead")
            else:
                print("That position has been already taken by your oponent. Choose another one instead")
    
    return board


def make_list_of_free_fields(board):
    
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_squares = [['','',''], ['','',''], ['','','']]

    i = 0

    while i < 3:
        if type(board[i][0]) == int:
            free_squares[i][0] = (i, 0)
        if type(board[i][1]) == int:
            free_squares[i][1] = (i, 1)
        if type(board[i][2]) == int:
            free_squares[i][2] = (i, 2)
        
        i += 1
        
    return free_squares


def victory_for(board, sign):
    
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    won = None
    
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        won = sign
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        won = sign
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        won = sign
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        won = sign
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        won = sign
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        won = sign
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        won = sign
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        won = sign

    if won != None:
        print("Player", sign, "won the game!!!")
        won = False
        return won

#def draw_move(board):
    # The function draws the computer's move and updates the board.


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

display_board(board)
board = enter_move(board)
print(board)
display_board(board)
board = enter_move(board)
display_board(board)
board = enter_move(board)
display_board(board)
free_squares = make_list_of_free_fields(board)
print(free_squares)
sign = "O"
won = victory_for(board, sign)