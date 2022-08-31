def display_board(board):
    
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.    
    
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0], "  |  " , board[1], "  |  " , board[2] , "  |" )
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[3], "  |  " , board[4], "  |  " , board[5] , "  |" )
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[6], "  |  " , board[7], "  |  " , board[8] , "  |" )
    print("|       |       |       |")
    print("+-------+-------+-------+")
    

def enter_move(board):

    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    while True:
        
        print("Please, provide your move")
        i = int(input())

        if i > 0 and i < 10:
            if board[i - 1] != "X" and board[i - 1] !=  "O":
                board[i - 1] = "O"
                break
            elif board[i - 1] ==  "O":
                print("That position has been already taken by you. Choose another one instead")
                continue
            else:
                print("That position has been already taken by your oponent. Choose another one instead")
                continue
        else:
            print("Provided number is a wrong number. Provide number that is greater or equal to 1 or smaller or equal to 9")
            continue


#def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


#def draw_move(board):
    # The function draws the computer's move and updates the board.


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

display_board(board)
enter_move(board)
display_board(board)
enter_move(board)
display_board(board)