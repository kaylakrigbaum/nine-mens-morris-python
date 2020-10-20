import random

#menu
def menu():
    print('Would you like to begin the game?')
    while True:
        try:
            choice = str(raw_input('Enter Y or N ==> ')).lower()
            if (choice != 'y') and (choice != 'n'):
                raise ValueError
            break
        except ValueError:
            print('Please enter a single Y or N character')

    if choice == 'y':
        return True
    return False

#randomly select player turn
def selectPlayerTurn():
    turn = 0
    turn = random.randint(1, 2)
    return turn

#check for any mills
def checkForMill(board, check, currentPlayer):
    #top horizontal
    if (board[0][0] == board[0][3] and board[0][0] == board[0][6] and board[0][0] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    #left vertical
    elif (board[1][1] == board[1][3] and board[1][1] == board[1][5] and board[1][1] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    #bottom horizontal
    elif (board[2][2] == board[2][3] and board[2][2] == board[2][4] and board[2][2] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    #bottom horizontal
    elif (board[2][2] == board[2][3] and board[2][2] == board[2][4] and board[2][2] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[3][0] == board[3][1] and board[3][0] == board[3][2] and board[3][0] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[3][4] == board[3][5] and board[3][4] == board[3][6] and board[3][4] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[4][2] == board[4][3] and board[4][2] == board[4][4] and board[4][2] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[5][1] == board[5][3] and board[5][1] == board[5][5] and board[5][1] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[6][0] == board[6][3] and board[6][0] == board[6][6] and board[6][0] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[0][0] == board[3][0] and board[0][0] == board[6][0] and board[0][0] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[1][1] == board[3][1] and board[1][1] == board[5][1] and board[1][1] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[2][2] == board[3][2] and board[2][2] == board[4][2] and board[2][2] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[0][3] == board[1][3] and board[0][3] == board[2][3] and board[0][3] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[4][3] == board[5][3] and board[4][3] == board[6][3] and board[4][3] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[2][4] == board[3][4] and board[2][4] == board[4][4] and board[2][4] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[1][5] == board[3][5] and board[1][5] == board[5][5] and board[1][5] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif (board[0][6] == board[3][6] and board[0][6] == board[6][6] and board[0][6] != 0):
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    else:
        return False

#output the current board
def displayBoard(board, rows, cols):
    for rows in board:
        for cols in rows:
            print '{:4}'.format(cols),
        print
    return

#test board creation
def testBoardCreation(board, size):
    return board.size() == size

#test mills
def testMills(board):
    return

#phase 1: players place their pieces on the board
def placementStage():
    return

#player class
class player:
    def __init__(self):
        self.player = 0
        self.pieceCount = 0
        self.placePieces = 0
        self.phase = 0

#main game logic area
def main():
    playing = menu()
    if playing:
        #initialize valid board
        validBoard = [[1, 0, 0, 1, 0, 0, 1],
                      [0, 1, 0, 1, 0, 1, 0],
                      [0, 0, 1, 1, 1, 0, 0],
                      [1, 1, 1, 0, 1, 1, 1],
                      [0, 0, 1, 1, 1, 0, 0],
                      [0, 1, 0, 1, 0, 1, 0],
                      [1, 0, 0, 1, 0, 0, 1]]

        #initialize blank board
        rows, cols = 7, 7
        board = [[0 for x in range(rows)] for y in range(cols)]

        #display board
        displayBoard(board, rows, cols)

        #declare player objects
        p1 = player()
        p2 = player()


        #randomize turn
        playerTurn = selectPlayerTurn()

        #begin the game turns in a loop
        while playing:
            if testBoardCreation(board, 7):
                displayBoard(board, rows, cols)


if __name__=="__main__":
    main()