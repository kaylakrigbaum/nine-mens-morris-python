import random

#menu
def menu():
    print("Would you like to begin the game?")
    #come back and regulate input types
    menuInput = input("Enter Y or N")
    if (menuInput == "Y"):
        return True
    return False

#randomly select player turn
def selectPlayerTurn():
    turn = 0
    turn = random.randint(1, 2)
    return turn

#check for any mills
def checkForMill():
    return

#output the current board
def displayBoard(board, rows, cols):
    for rows in board:
        for cols in rows:
            print '{:4}'.format(cols),
        print
    return

#test board creation
def testBoardCreation():
    return

#test mills
def testMills():
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
        p1, p2 = player()

        #randomize turn
        playerTurn = selectPlayerTurn()

        #begin the game turns in a loop
        while playing:
            if testBoardCreation(board, 7):
                displayBoard(board, rows, cols)


if __name__=="__main__":
    main()