def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ", tablica_z_liczbami[1], "  |  " , tablica_z_liczbami[2], "  |  " , tablica_z_liczbami[3] , "  |" )
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ", tablica_z_liczbami[4], "  |  " , tablica_z_liczbami[5], "  |  " , tablica_z_liczbami[6] , "  |" )
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ", tablica_z_liczbami[7], "  |  " , tablica_z_liczbami[8], "  |  " , tablica_z_liczbami[9] , "  |" )
    print("|       |       |       |")
    print("+-------+-------+-------+")
    
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

test:
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    # The function draws the computer's move and updates the board.
