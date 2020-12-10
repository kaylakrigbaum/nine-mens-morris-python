import random
import pygame
import sys
import math

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SLATE = (112, 128, 144)
DARKGREY = (169, 169, 169)

# Using the systems font for pygame display
pygame.font.init()
# myfont = pygame.font.SysFont('Comic Sans MS', 30)

activatedMills = []
totalMills = []


# menu
def menu():
    running = True
    while running:
        pygame.init()  # initializing pygame stuff

        # storing the coords of our mouse location as a tuple
        mouse = pygame.mouse.get_pos()

        res = (700, 800)  # setting the resolution of our game screen
        screen = pygame.display.set_mode(res)

        width = screen.get_width()
        height = screen.get_height()

        screen.fill(WHITE)
        # gathering pygame event information
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            # if the user clicks on the quit, pygame exits, else if they click play the game, the board populates
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width / 2 - 50 <= mouse[0] <= width / 2 + 90 and height / 2 + 240 <= mouse[
                    1] <= height / 2 + 280:  # 140 and 40
                    pygame.quit()
                    return 0
                elif width / 2 - 60 <= mouse[0] <= width / 2 + 120 and height / 2 <= mouse[1] <= height / 2 + 50:
                    return 1
                elif width / 2 - 60 <= mouse[0] <= width / 2 + 120 and height / 2 + 120 <= mouse[1] <= height / 2 + 180:
                    return 2

        # picking the font that we want to use for the title of the game
        myfont = pygame.font.SysFont('Comic Sans MS', 84)
        mainTextSurface = myfont.render("Nine Mens Morris", False, BLACK)
        textRect = mainTextSurface.get_rect(center=(width / 2, height / 2 - 140))
        screen.blit(mainTextSurface, textRect)

        # creating the button font for all the smaller buttons
        buttonFont = pygame.font.SysFont('Comic Sans MS', 35)
        quitText = buttonFont.render("Quit", False, BLACK)

        # changing the shading in case user hovers over button..else statement creates the solid color when user isn't hovering over
        if width / 2 - 50 <= mouse[0] <= width / 2 + 90 and height / 2 + 240 <= mouse[1] <= height / 2 + 280:
            pygame.draw.rect(screen, SLATE, [width / 2 - 50, height / 2 + 250, 140, 40])
        else:
            pygame.draw.rect(screen, DARKGREY, [width / 2 - 50, height / 2 + 250, 140, 40])

        screen.blit(quitText, (width / 2 - 25, height / 2 + 245))  # displaying the text


        # rendering text for the "Play Game" button
        playText = buttonFont.render("Play Game", False, BLACK)

        # changing the shading based on mouse movement.
        if width / 2 - 60 <= mouse[0] <= width / 2 + 120 and height / 2 <= mouse[1] <= height / 2 + 50:
            pygame.draw.rect(screen, SLATE, [width / 2 - 60, height / 2, 180, 50])
        else:
            pygame.draw.rect(screen, DARKGREY, [width / 2 - 60, height / 2, 180, 50])

        screen.blit(playText, (width / 2 - 50, height / 2 + 0))  # displaying the text


        PlayAiText = buttonFont.render("Play vs AI", False, BLACK)

        if width / 2 - 60 <= mouse[0] <= width / 2 + 120 and height / 2 + 120  <= mouse[1] <= height / 2 + 180:
            pygame.draw.rect(screen, SLATE, [width / 2 - 60, height / 2 + 120, 180, 50])
        else:
            pygame.draw.rect(screen, DARKGREY, [width / 2 - 60, height / 2 + 120, 180, 50])

        screen.blit(PlayAiText, (width / 2 - 50, height / 2 + 115))

        pygame.display.set_caption("Main Menu")
        pygame.display.update()


# randomly select player turn
def selectPlayerTurn():
    turn = random.randint(1, 2)
    return turn


# check for any mills
def checkForMill(board, currentPlayer):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    # creating a text surface that will display in pygame who has created a mill.
    screen.fill((255, 0, 0))
    textsurface = myfont.render(currentPlayer.upper() + " HAS CREATED A MILL", False, (0, 0, 0))

    # top horizontal
    if board[0][0] == board[0][3] and board[0][0] == board[0][6] and board[0][0] != 0:
        if ([(0, 0), (0, 3), (0, 6)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(0, 0), (0, 3), (0, 6)]))
            return True
    else:
        if ([(0, 0), (0, 3), (0, 6)]) in activatedMills:
            activatedMills.remove(([(0, 0), (0, 3), (0, 6)]))

    # left vertical
    if board[1][1] == board[1][3] and board[1][1] == board[1][5] and board[1][1] != 0:
        if ([(1, 1), (1, 3), (1, 5)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(1, 1), (1, 3), (1, 5)]))
            return True
    else:
        if ([(1, 1), (1, 3), (1, 5)]) in activatedMills:
            activatedMills.remove(([(1, 1), (1, 3), (1, 5)]))
    # bottom horizontal
    if board[2][2] == board[2][3] and board[2][2] == board[2][4] and board[2][2] != 0:
        if ([(2, 2), (2, 3), (2, 4)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(2, 2), (2, 3), (2, 4)]))
            return True
    else:
        if ([(2, 2), (2, 3), (2, 4)]) in activatedMills:
            activatedMills.remove(([(2, 2), (2, 3), (2, 4)]))

    if board[3][0] == board[3][1] and board[3][0] == board[3][2] and board[3][0] != 0:
        if ([(3, 0), (3, 1), (3, 2)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(3, 0), (3, 1), (3, 2)]))
            return True
    else:
        if ([(3, 0), (3, 1), (3, 2)]) in activatedMills:
            activatedMills.remove(([(3, 0), (3, 1), (3, 2)]))

    if board[3][4] == board[3][5] and board[3][4] == board[3][6] and board[3][4] != 0:
        if ([(3, 4), (3, 5), (3, 6)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(3, 4), (3, 5), (3, 6)]))
            return True
    else:
        if ([(3, 4), (3, 5), (3, 6)]) in activatedMills:
            activatedMills.remove(([(3, 4), (3, 5), (3, 6)]))

    if board[4][2] == board[4][3] and board[4][2] == board[4][4] and board[4][2] != 0:
            if ([(4, 2), (4, 3), (4, 4)]) not in activatedMills:
                screen.blit(textsurface, (0, 0))  # display who created the mill.
                activatedMills.insert(0, ([(4, 2), (4, 3), (4, 4)]))
                return True
    else:
        if ([(4, 2), (4, 3), (4, 4)]) in activatedMills:
            activatedMills.remove(([(4, 2), (4, 3), (4, 4)]))

    if board[5][1] == board[5][3] and board[5][1] == board[5][5] and board[5][1] != 0:
        if ([(5, 1), (5, 3), (5, 5)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(5, 1), (5, 3), (5, 5)]))
            return True
    else:
        if ([(5, 1), (5, 3), (5, 5)]) in activatedMills:
            activatedMills.remove(([(5, 1), (5, 3), (5, 5)]))

    if board[6][0] == board[6][3] and board[6][0] == board[6][6] and board[6][0] != 0:
        if ([(6, 0), (6, 3), (6, 6)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(6, 0), (6, 3), (6, 6)]))
            return True
    else:
        if ([(6, 0), (6, 3), (6, 6)]) in activatedMills:
            activatedMills.remove(([(6, 0), (6, 3), (6, 6)]))

    if board[0][0] == board[3][0] and board[0][0] == board[6][0] and board[0][0] != 0:
        if ([(0, 0), (3, 0), (6, 0)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(0, 0), (3, 0), (6, 0)]))
            return True
    else:
        if ([(0, 0), (3, 0), (6, 0)]) in activatedMills:
            activatedMills.remove(([(0, 0), (3, 0), (6, 0)]))

    if board[1][1] == board[3][1] and board[1][1] == board[5][1] and board[1][1] != 0:
        if ([(1, 1), (3, 1), (5, 1)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(1, 1), (3, 1), (5, 1)]))
            return True
    else:
        if ([(1, 1), (3, 1), (5, 1)]) in activatedMills:
            activatedMills.remove(([(1, 1), (3, 1), (5, 1)]))

    if board[2][2] == board[3][2] and board[2][2] == board[4][2] and board[2][2] != 0:
        if ([(2, 2), (3, 2), (4, 2)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(2, 2), (3, 2), (4, 2)]))
            return True
    else:
        if ([(2, 2), (3, 2), (4, 2)]) in activatedMills:
            activatedMills.remove(([(2, 2), (3, 2), (4, 2)]))

    if board[0][3] == board[1][3] and board[0][3] == board[2][3] and board[0][3] != 0:
        if ([(0, 3), (1, 3), (2, 3)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(0, 3), (1, 3), (2, 3)]))
            return True
    else:
        if ([(0, 3), (1, 3), (2, 3)]) in activatedMills:
            activatedMills.remove(([(0, 3), (1, 3), (2, 3)]))

    if board[4][3] == board[5][3] and board[4][3] == board[6][3] and board[4][3] != 0:
        if ([(4, 3), (5, 3), (6, 3)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(4, 3), (5, 3), (6, 3)]))
            return True
    else:
        if ([(4, 3), (5, 3), (6, 3)]) in activatedMills:
            activatedMills.remove(([(4, 3), (5, 3), (6, 3)]))

    if board[2][4] == board[3][4] and board[2][4] == board[4][4] and board[2][4] != 0:
        if ([(2, 4), (3, 4), (4, 4)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(2, 4), (3, 4), (4, 4)]))
            return True
    else:
        if ([(2, 4), (3, 4), (4, 4)]) in activatedMills:
            activatedMills.remove(([(2, 4), (3, 4), (4, 4)]))

    if board[1][5] == board[3][5] and board[1][5] == board[5][5] and board[1][5] != 0:
        if ([(1, 5), (3, 5), (5, 5)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(1, 5), (3, 5), (5, 5)]))
            return True
    else:
        if ([(1, 5), (3, 5), (5, 5)]) in activatedMills:
            activatedMills.remove(([(1, 5), (3, 5), (5, 5)]))

    if board[0][6] == board[3][6] and board[0][6] == board[6][6] and board[0][6] != 0:
        if ([(0, 6), (3, 6), (6, 6)]) not in activatedMills:
            screen.blit(textsurface, (0, 0))  # display who created the mill.
            activatedMills.insert(0, ([(0, 6), (3, 6), (6, 6)]))
            return True
    else:
        if ([(0, 6), (3, 6), (6, 6)]) in activatedMills:
            activatedMills.remove(([(0, 6), (3, 6), (6, 6)]))

    return False


# test board creation
def testBoardCreation(board, size):
    return len(board) == size


# test mills
def testMills(board):
    return


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def check_piece_in_mill(piece):
    for mill in activatedMills:
        if piece in mill:
            return True
    return False


def remove_piece(board, row, col, turnToggle):
    # figure out if the piece being removed is part of a mill
    piece = (row, col)
    no_other_pieces = False
    if check_piece_in_mill(piece):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == turnToggle:
                    if not check_piece_in_mill((i, j)):
                        return False
        no_other_pieces = True
    if no_other_pieces:
        for mill in activatedMills:
            if piece in mill:
                activatedMills.remove(mill)
    board[row][col] = 0
    return True

    board[row][col] = 0


# this function checks the following:
# 1. Identify adjacent nodes

# 0: [1, 0, 0, 1, 0, 0, 1],
# 1: [0, 1, 0, 1, 0, 1, 0],
# 2: [0, 0, 1, 1, 1, 0, 0],
# 3: [1, 1, 1, 0, 1, 1, 1],
# 4: [0, 0, 1, 1, 1, 0, 0],
# 5: [0, 1, 0, 1, 0, 1, 0],
# 6: [1, 0, 0, 1, 0, 0, 1]
#    0  1  2  3  4  5  6
def check_adjacent(curr_row, curr_col):
    adjacencies = {}
    adjacencies[(0, 0)] = [(3, 0), (0, 3)]
    adjacencies[(3, 0)] = [(0, 0), (6, 0), (3, 1)]
    adjacencies[(6, 0)] = [(3, 0), (6, 3)]

    adjacencies[(1, 1)] = [(3, 1), (1, 3)]
    adjacencies[(3, 1)] = [(3, 0), (3, 2), (1, 1), (5, 1)]
    adjacencies[(5, 1)] = [(3, 1), (5, 3)]

    adjacencies[(2, 2)] = [(2, 3), (3, 2)]
    adjacencies[(3, 2)] = [(2, 2), (4, 2), (3, 1)]
    adjacencies[(0, 3)] = [(0, 0), (0, 6), (1, 3)]

    adjacencies[(1, 3)] = [(0, 3), (2, 3), (1, 1), (1, 5)]
    adjacencies[(2, 3)] = [(2, 2), (2, 4), (1, 3)]
    adjacencies[(4, 3)] = [(4, 2), (4, 4), (5, 3)]

    adjacencies[(5, 3)] = [(4, 3), (6, 3), (5, 1), (5, 5)]
    adjacencies[(6, 3)] = [(5, 3), (6, 0), (6, 6)]
    adjacencies[(2, 4)] = [(2, 3), (3, 4)]

    adjacencies[(3, 4)] = [(2, 4), (4, 4), (3, 5)]
    adjacencies[(4, 4)] = [(3, 4), (4, 3)]
    adjacencies[(1, 5)] = [(3, 5), (1, 3)]

    adjacencies[(3, 5)] = [(1, 5), (5, 5), (3, 4), (3, 6)]
    adjacencies[(5, 5)] = [(3, 5), (5, 3)]
    adjacencies[(0, 6)] = [(0, 3), (3, 6)]

    adjacencies[(3, 6)] = [(0, 6), (3, 5), (6, 6)]
    adjacencies[(6, 6)] = [(3, 6), (6, 3)]
    adjacencies[(4, 2)] = [(3, 2), (4, 3)]

    return adjacencies[(curr_row, curr_col)]


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

if playing == 1 or playing == 2:
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
    shiftingBool = False  # bool used to determine whether user is shifting a piece
    turnToggle = 1  # this is used to toggle between white and black
    if playerTurn == 1:
        p1.color = "white"
        p2.color = "black"
    else:
        p2.color = "white"
        p1.color = "black"

    while playing:
        myfont = pygame.font.SysFont('Comic Sans MS', 30)

        # creating a text surface that will display in pygame who has created a mill.
        if testBoardCreation(board, 7):
            draw_board(board, validBoard)
            pygame.display.update()  # updates the screen
            for event in pygame.event.get():
                if placingBool is True and shiftingBool is not True:
                    screen.fill((255, 0, 0))
                    if turnToggle == 1:
                        textsurface = myfont.render("WHITE'S TURN! PLACE A PIECE", False, (0, 0, 0))
                    else:
                        textsurface = myfont.render("BLACK'S TURN! PLACE A PIECE", False, (0, 0, 0))
                    screen.blit(textsurface, (0, 0))

                if event.type == pygame.QUIT:
                    sys.exit()  # ends program when you close game

                if event.type == pygame.MOUSEBUTTONDOWN and placingBool is True and shiftingBool is not True:
                    posx = event.pos[0]  # x position of mouse click
                    posy = event.pos[1]  # y position of mouse click

                    col = int(math.floor(posx / square_size))
                    row = int(math.floor(posy / square_size))



                    # makes sure that you clicked on a circle
                    if row < 1 or validBoard[row - 1][col] != 1:
                        print("Illegal move")

                    else:
                        # placement stage
                        if p1.placedPieces < 9 or p2.placedPieces < 9:
                            if turnToggle == 1:
                                if board[row - 1][col] == 0:
                                    drop_piece(board, row - 1, col, 1)
                                    turnToggle = 2
                                    if p1.color == "white":
                                        p1.placedPieces += 1
                                        p1.pieceCount += 1
                                    else:
                                        p2.placedPieces += 1
                                        p2.pieceCount += 1
                                    if checkForMill(board, "white"):  # if there is a mill allow for removal of piece
                                        placingBool = False  # setting this to allow for removal instead of placing
                                else:
                                    print("Choose an empty space")

                            else:
                                screen.fill((255, 0, 0))
                                textsurface = myfont.render("BLACK'S TURN! PLACE A PIECE", False, (0, 0, 0))
                                screen.blit(textsurface, (0, 0))
                                if board[row - 1][col] == 0:
                                    drop_piece(board, row - 1, col, 2)
                                    turnToggle = 1
                                    if p1.color == "black":
                                        p1.placedPieces += 1
                                        p1.pieceCount += 1
                                    else:
                                        p2.placedPieces += 1
                                        p2.pieceCount += 1
                                    if checkForMill(board, "black"):
                                        placingBool = False
                                else:
                                    print("Choose an empty space")

                        # stage 2
                        elif p1.pieceCount > 2 and p2.pieceCount > 2:
                            screen.fill((255, 0, 0))
                            myfont = pygame.font.SysFont('Comic Sans MS', 30)
                            textsurfaceStage2 = myfont.render("Stage two has begun move pieces to adjacent spot  ",
                                                              False, (0, 0, 0))
                            screen.blit(textsurfaceStage2, (0, 5))
                            adjacent_nodes = check_adjacent(row - 1, col)
                            shiftingBool = True

                        else:
                            screen.fill((255, 0, 0))
                            myfont = pygame.font.SysFont('Comic Sans MS', 30)
                            textsurfaceEndGame = myfont.render("Game over!",
                                                              False, (0, 0, 0))
                            screen.blit(textsurfaceEndGame, (0, 5))
                            print("Game over")

                elif event.type == pygame.MOUSEBUTTONDOWN and placingBool is not True:
                    posx = event.pos[0]  # x position of mouse click
                    posy = event.pos[1]  # y position of mouse click

                    col = int(math.floor(posx / square_size))
                    row = int(math.floor(posy / square_size))

                    # makes sure that you clicked on a circle
                    if row < 1 or validBoard[row - 1][col] != 1:
                        print("Illegal move in stage 2")
                    else:
                        if board[row - 1][col] == turnToggle:  # check if it is the opposing piece
                            if remove_piece(board, row - 1, col, turnToggle):
                                p1.pieceCount -= 1
                                placingBool = True

                elif event.type == pygame.MOUSEBUTTONDOWN and placingBool is True and shiftingBool is True:
                    posx = event.pos[0]  # x position of mouse click
                    posy = event.pos[1]  # y position of mouse click

                    newCol = int(math.floor(posx / square_size))
                    newRow = int(math.floor(posy / square_size))

                    # makes sure that you clicked on a circle
                    if row < 1 or validBoard[newRow - 1][newCol] != 1 or board[row - 1][col] != turnToggle:
                        print("Illegal move in stage 2")

                    elif p1.pieceCount == 3 or p2.pieceCount == 3:
                        current_node = (row - 1, col)
                        next_node = (newRow - 1, newCol)
                        if board[newRow - 1][newCol] == 0:
                            board[newRow - 1][newCol] = turnToggle
                            board[row - 1][col] = 0
                        if turnToggle == 1:
                            if checkForMill(board, "white"):
                                placingBool = False
                            turnToggle = 2
                        else:
                            if checkForMill(board, "black"):
                                placingBool = False
                            turnToggle = 1
                    else:
                        current_node = (row - 1, col)
                        next_node = (newRow - 1, newCol)
                        if board[newRow - 1][
                            newCol] == 0 and next_node in adjacent_nodes and current_node != next_node:
                            board[newRow - 1][newCol] = turnToggle
                            board[row - 1][col] = 0
                            if turnToggle == 1:
                                if checkForMill(board, "white"):
                                    placingBool = False
                                turnToggle = 2
                            else:
                                if checkForMill(board, "black"):
                                    placingBool = False
                                turnToggle = 1
                    shiftingBool = False

                draw_board(board, validBoard)
                pygame.display.update()

                # begin the game turns in a loop
