import gameboard
import player

print("Welcome to Alex's game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2
# I expanded the board game and changed the coordinates of player

board = gameboard.GameBoard()
# player = player.Player(3,2 )
player = player.Player(3,4)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
    if selection == "w":
        if board.checkMove(player.rowPosition-1, player.columnPosition):
            player.moveUp()
    elif selection == "s":
        if board.checkMove(player.rowPosition +1, player.columnPosition):
            player.moveDown()
    elif selection == "a":
        if board.checkMove(player.rowPosition, player.columnPosition-1):
            player.moveLeft()
    elif selection == "d":
        if board.checkMove(player.rowPosition, player.columnPosition+1):
            player.moveRight()
    if board.checkWin(player.rowPosition, player.columnPosition):
        print("Congratulations! You Won the game.. thanks to Alex :) ")
        break
    
        
        


   




        