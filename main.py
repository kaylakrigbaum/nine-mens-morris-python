import random
import pygame
import sys
import math

BLUE = (0, 0, 255)



# menu
def menu():
    print('Would you like to begin the game?')
    while True:
        try:
            choice = str(input('Enter Y or N ==> ')).lower()
            if (choice != 'y') and (choice != 'n'):
                raise ValueError
            break
        except ValueError:
            print('Please enter a single Y or N character')

    if choice == 'y':
        return True
    return False


# randomly select player turn
def selectPlayerTurn():
    turn = 0
    turn = random.randint(1, 2)
    return turn


# check for any mills
def checkForMill(board, check, currentPlayer):
    # top horizontal
    if board[0][0] == board[0][3] and board[0][0] == board[0][6] and board[0][0] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    # left vertical
    elif board[1][1] == board[1][3] and board[1][1] == board[1][5] and board[1][1] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    # bottom horizontal
    elif board[2][2] == board[2][3] and board[2][2] == board[2][4] and board[2][2] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    # bottom horizontal
    elif board[2][2] == board[2][3] and board[2][2] == board[2][4] and board[2][2] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[3][0] == board[3][1] and board[3][0] == board[3][2] and board[3][0] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[3][4] == board[3][5] and board[3][4] == board[3][6] and board[3][4] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[4][2] == board[4][3] and board[4][2] == board[4][4] and board[4][2] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[5][1] == board[5][3] and board[5][1] == board[5][5] and board[5][1] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[6][0] == board[6][3] and board[6][0] == board[6][6] and board[6][0] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[0][0] == board[3][0] and board[0][0] == board[6][0] and board[0][0] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[1][1] == board[3][1] and board[1][1] == board[5][1] and board[1][1] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[2][2] == board[3][2] and board[2][2] == board[4][2] and board[2][2] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[0][3] == board[1][3] and board[0][3] == board[2][3] and board[0][3] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[4][3] == board[5][3] and board[4][3] == board[6][3] and board[4][3] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[2][4] == board[3][4] and board[2][4] == board[4][4] and board[2][4] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[1][5] == board[3][5] and board[1][5] == board[5][5] and board[1][5] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    elif board[0][6] == board[3][6] and board[0][6] == board[6][6] and board[0][6] != 0:
        print(currentPlayer, " HAS CREATED A MILL")
        return True

    else:
        return False


# output the current board
def displayBoard(board, validBoard, rows, cols):
    for i in range(rows):
        print(i, end="")
        print("  ", end="")
        for j in range(cols):
            if validBoard[i][j] == 1:
                print(board[i][j], end="")
            print("   ", end="")
        print("\n")

    print("  a  b  c  d  e  f  g\n\n", end="")
    return


# test board creation
def testBoardCreation(board, size):
    return len(board) == size


# test mills
def testMills(board):
    return


# phase 1: players place their pieces on the board
def placementStage(white, black, board, validBoard):
    currentPlayer = 'white'
    currentTurnNum = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        while white.placedPieces < 9 or black.placedPieces < 9:
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]

                col = int(math.floor(posx/square_size))
                row = int(math.floor(posy/square_size))

                if validBoard[col][row] == 1:
                    print("You clicked legally")
                else:
                    print("Illegal")
                # # convert col letter to index
                # colChar = move[0]
                # colNum = ord(colChar) - 97
                # rowNum = int(move[1])
                #
                # # check if move is legal
                # if colNum < len(validBoard) and rowNum < len(validBoard) and validBoard[rowNum][colNum] == 1 and \
                #         board[rowNum][colNum] == 0:
                #     # place piece
                #     board[rowNum][colNum] = currentTurnNum
                #
                #     # check for mill
                #     if white.placedPieces >= 2 or black.placedPieces >= 2:
                #         checkForMill(board, True, currentPlayer)
                #
                #     displayBoard(board, validBoard, 7, 7)
                #     if currentTurnNum == 1:
                #         white.placedPieces += 1
                #         currentPlayer = "black"
                #         currentTurnNum = 2
                #
                #     else:
                #         black.placedPieces += 1
                #         currentPlayer = "white"
                #         currentTurnNum = 1
                #
                # else:
                #     print("Invalid location.")
                #     continue
    return

def draw_board(board, validBoard):
    for c in range(7):
        for r in range(7):
            if validBoard[c][r] == 1:
                pygame.draw.circle(screen, BLUE, (c * square_size + 50, r*square_size + square_size + 50), 20)


# player class
class player:
    def __init__(self):
        self.player = 0
        self.pieceCount = 0
        self.placedPieces = 0
        self.phase = 0

# main game logic area
playing = menu()

if playing:
    pygame.init()
    # screen variables
    square_size = 100

    width = 7 * square_size
    height = 8 * square_size

    size = (width, height)

    screen = pygame.display.set_mode(size)
    # initialize valid board
    validBoard = [[1, 0, 0, 1, 0, 0, 1],
                  [0, 1, 0, 1, 0, 1, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [1, 1, 1, 0, 1, 1, 1],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 1, 0, 1, 0, 1, 0],
                  [1, 0, 0, 1, 0, 0, 1]]

    # initialize blank board
    rows, cols = 7, 7
    board = [[0 for x in range(rows)] for y in range(cols)]

    # display board


    # declare player objects
    p1 = player()
    p2 = player()

    # randomize turn
    while playing:
        playerTurn = selectPlayerTurn()
        if testBoardCreation(board, 7):
            draw_board(board, validBoard)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    posy = event.pos[1]

                    col = int(math.floor(posx/square_size))
                    row = int(math.floor(posy/square_size))

                    if row < 1:
                        print("Illegal")

                    else:
                        if validBoard[col][row - 1] == 1:
                            print("You clicked legally")
                        else:
                            print("Illegal")



                # begin the game turns in a loop
