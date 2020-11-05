import random
import pygame
import sys
import math

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Using the systems font for pygame display
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

activatedMills = []


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
    turn = random.randint(1, 2)
    return turn

# check for any mills
def checkForMill(board, currentPlayer):
    #creating a text surface that will display in pygame who has created a mill.
    textsurface = myfont.render(currentPlayer.upper() + " HAS CREATED A MILL", False, (0, 0, 0))

    # top horizontal
    if board[0][0] == board[0][3] and board[0][0] == board[0][6] and board[0][0] != 0 and ([(0, 0), (0, 3), (0, 6)]) not in activatedMills:
        screen.blit(textsurface, (0,0)) # display who created the mill.
        activatedMills.insert(0,([(0, 0), (0, 3), (0, 6)]))
        return True
    # left vertical
    if board[1][1] == board[1][3] and board[1][1] == board[1][5] and board[1][1] != 0 and ([(1, 1), (1, 3), (1, 5)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(1, 1), (1, 3), (1, 5)]))
        return True
    # bottom horizontal
    if board[2][2] == board[2][3] and board[2][2] == board[2][4] and board[2][2] != 0 and ([(2, 2), (2, 3), (2, 4)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(2, 2), (2, 3), (2, 4)]))
        return True

    if board[3][0] == board[3][1] and board[3][0] == board[3][2] and board[3][0] != 0 and ([(3, 0), (3, 1), (3, 2)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(3, 0), (3, 1), (3, 2)]))
        return True

    if board[3][4] == board[3][5] and board[3][4] == board[3][6] and board[3][4] != 0 and ([(3, 4), (3, 5), (3, 6)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(3, 4), (3, 5), (3, 6)]))
        return True

    if board[4][2] == board[4][3] and board[4][2] == board[4][4] and board[4][2] != 0 and ([(4, 2), (4, 3), (4, 4)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(4, 2), (4, 3), (4, 4)]))
        return True

    if board[5][1] == board[5][3] and board[5][1] == board[5][5] and board[5][1] != 0 and ([(5, 1), (5, 3), (5, 5)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(5, 1), (5, 3), (5, 5)]))
        return True

    if board[6][0] == board[6][3] and board[6][0] == board[6][6] and board[6][0] != 0 and ([(6, 0), (6, 3), (6, 6)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(6, 0), (6, 3), (6, 6)]))
        return True

    if board[0][0] == board[3][0] and board[0][0] == board[6][0] and board[0][0] != 0 and ([(0, 0), (3, 0), (6, 0)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(0, 0), (3, 0), (6, 0)]))
        return True

    if board[1][1] == board[3][1] and board[1][1] == board[5][1] and board[1][1] != 0 and ([(1, 1), (3, 1), (5, 1)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(1, 1), (3, 1), (5, 1)]))
        return True

    if board[2][2] == board[3][2] and board[2][2] == board[4][2] and board[2][2] != 0 and ([(2, 2), (3, 2), (4, 2)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(2, 2), (3, 2), (4, 2)]))
        return True

    if board[0][3] == board[1][3] and board[0][3] == board[2][3] and board[0][3] != 0 and ([(0, 3), (1, 3), (2, 3)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(0, 3), (1, 3), (2, 3)]))
        return True

    if board[4][3] == board[5][3] and board[4][3] == board[6][3] and board[4][3] != 0 and ([(4, 3), (5, 3), (6, 3)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(4, 3), (5, 3), (6, 3)]))
        return True

    if board[2][4] == board[3][4] and board[2][4] == board[4][4] and board[2][4] != 0 and ([(2, 4), (3, 4), (4, 4)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(2, 4), (3, 4), (4, 4)]))
        return True

    if board[1][5] == board[3][5] and board[1][5] == board[5][5] and board[1][5] != 0 and ([(1, 5), (3, 5), (5, 5)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(1, 5), (3, 5), (5, 5)]))
        return True

    if board[0][6] == board[3][6] and board[0][6] == board[6][6] and board[0][6] != 0 and ([(0, 6), (3, 6), (6, 6)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(0, 6), (3, 6), (6, 6)]))
        return True

    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != 0 and ([(0, 0), (1, 1), (2, 2)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(0, 0), (1, 1), (2, 2)]))
        return True

    if board[6][0] == board[5][1] and board[6][0] == board[4][2] and board[6][0] != 0 and ([(6, 0), (5, 1), (4, 2)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(6, 0), (5, 1), (4, 2)]))
        return True

    if board[0][6] == board[1][5] and board[0][6] == board[2][4] and board[0][6] != 0 and ([(0, 6), (1, 5), (2, 4)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(0, 6), (1, 5), (2, 4)]))
        return True

    if board[6][6] == board[5][5] and board[6][6] == board[4][4] and board[6][6] != 0 and ([(6, 6), (5, 5), (4, 4)]) not in activatedMills:
        screen.blit(textsurface, (0, 0))  # display who created the mill.
        activatedMills.insert(0,([(6, 6), (5, 5), (4, 4)]))
        return True

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


def drop_piece(board, row, col, piece):
    board[row][col] = piece

def remove_piece(board, row, col):
    board[row][col] = 0


# phase 1: players place their pieces on the board
# def placementStage(white, black, board, validBoard):
#     currentPlayer = 'white'
#     currentTurnNum = 1
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         while white.placedPieces < 9 or black.placedPieces < 9:
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 posx = event.pos[0]
#                 posy = event.pos[1]
#
#                 col = int(math.floor(posx / square_size))
#                 row = int(math.floor(posy / square_size))
#
#                 if validBoard[col][row] == 1:
#                     print("You clicked legally")
#                 else:
#                     print("Illegal")
#                 # convert col letter to index
#                 colChar = move[0]
#                 colNum = ord(colChar) - 97
#                 rowNum = int(move[1])
#
#                 # check if move is legal
#                 if colNum < len(validBoard) and rowNum < len(validBoard) and validBoard[rowNum][colNum] == 1 and \
#                         board[rowNum][colNum] == 0:
#                     # place piece
#                     board[rowNum][colNum] = currentTurnNum
#
#                     # check for mill
#                     if white.placedPieces >= 2 or black.placedPieces >= 2:
#                         checkForMill(board, True, currentPlayer)
#
#                     displayBoard(board, validBoard, 7, 7)
#                     if currentTurnNum == 1:
#                         white.placedPieces += 1
#                         currentPlayer = "black"
#                         currentTurnNum = 2
#
#                     else:
#                         black.placedPieces += 1
#                         currentPlayer = "white"
#                         currentTurnNum = 1
#
#                 else:
#                     print("Invalid location.")
#                     continue
#     return


def draw_board(board, validBoard):
    for r in range(7):
        for c in range(7):
            if validBoard[r][c] == 1:
                if board[r][c] == 0:
                    pygame.draw.circle(screen, BLUE, (c * square_size + 50, r * square_size + square_size + 50), 20)
                elif board[r][c] == 1:
                    pygame.draw.circle(screen, WHITE, (c * square_size + 50, r * square_size + square_size + 50), 20)
                else:
                    pygame.draw.circle(screen, BLACK, (c * square_size + 50, r * square_size + square_size + 50), 20)


# player class
class player:
    def __init__(self):
        self.player = 0
        self.pieceCount = 0
        self.placedPieces = 0
        self.phase = 0
        self.color = ""


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
    screen.fill((255, 0, 0))
    pygame.display.update()
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
    playerTurn = selectPlayerTurn()
    placingBool = True  # bool used to determine whether a click is to place a piece or remove a piece
    turnToggle = 1  # this is used to toggle between white and black
    if playerTurn == 1:
        p1.color = "white"
        p2.color = "black"
    else:
        p2.color = "white"
        p1.color = "black"

    while playing:
        if testBoardCreation(board, 7):
            draw_board(board, validBoard)
            pygame.display.update()  # updates the screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # ends program when you close game

                if event.type == pygame.MOUSEBUTTONDOWN and placingBool is True:
                    posx = event.pos[0]  # x position of mouse click
                    posy = event.pos[1]  # y position of mouse click

                    col = int(math.floor(posx / square_size))
                    row = int(math.floor(posy / square_size))

                    # makes sure that you clicked on a circle
                    if row < 1 or validBoard[col][row - 1] != 1:
                        print("Illegal move")

                    else:

                        # placement stage
                        if p1.placedPieces < 9 or p2.placedPieces < 9:
                            if turnToggle == 1:
                                drop_piece(board, row - 1, col, 1)
                                turnToggle = 2
                                if p1.color == "white":
                                    p1.placedPieces += 1
                                else:
                                    p2.placedPieces += 1
                                if checkForMill(board, "white"): #if there is a mill allow for removal of piece
                                    placingBool = False #setting this to allow for removal instead of placing

                            else:
                                drop_piece(board, row - 1, col, 2)
                                turnToggle = 1
                                if p1.color == "black":
                                    p1.placedPieces += 1
                                else:
                                    p2.placedPieces += 1
                                if checkForMill(board, "black"):
                                    placingBool = False


                elif event.type == pygame.MOUSEBUTTONDOWN and placingBool is not True:
                    posx = event.pos[0]  # x position of mouse click
                    posy = event.pos[1]  # y position of mouse click

                    col = int(math.floor(posx / square_size))
                    row = int(math.floor(posy / square_size))

                    # makes sure that you clicked on a circle
                    if row < 1 or validBoard[col][row - 1] != 1:
                        print("Illegal move in stage 2")
                    else:
                        if turnToggle == 1:
                            if board[row - 1][col] == 1:  # check if it is the opposing piece
                                remove_piece(board, row - 1, col)
                                placingBool = True
                        else:
                            if board[row - 1][col] == 2:  # check if it is the opposing piece
                                remove_piece(board, row - 1, col)
                                placingBool = True

                draw_board(board, validBoard)
                pygame.display.update()

                # begin the game turns in a loop
