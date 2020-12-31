# Implementation of Two Player Tic-Tac-Toe game in Python.
# Sources: https://dev.to/jamesshah/the-classic-tictactoe-game-in-python-cpi
import random
import sys

# KEY:
# variable 'turn' holds string value X or O

'''We will make the board using dictionary
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move
    we will change the value according to player's choice of move.'''

# board is a dictionary. the initial keys to the dictionary are empty strings
masterBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

boardKeys = []

for key in masterBoard:
    # generates this list: ['7', '8', '9', '4', '5', '6', '1', '2', '3'] BUT WHY?
    boardKeys.append(key)

print(boardKeys)
'''We will have to print the updated board after every move in the game and
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function.'''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def winLogic(board, turn):
    value = False
    if board['7'] == board['8'] == board['9'] != ' ': # across the top # TURN WINNING LOGIC INTO A SEPARATE FUNCTION
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
        printBoard(board)
        print("**** " + turn + " will win. ****")
        value = True
    return value

# Returns winner and position that will cause the win
def simulate(board, currentTurn):
    print("Running simulation for ", currentTurn)
    printBoard(board)

    # 1. Breadth first search for a winning spot
    boardCopy = dict(board)
    for key in boardCopy:
        if boardCopy[key]  == ' ':
            print("Trying breadth search on openspot ", key)
            boardCopy[key] = currentTurn

            if winLogic(boardCopy, currentTurn):
                # Base case, win found.  We win if we take this spot.
                print('Detected win by ', currentTurn, " at ", key)
                return currentTurn, key

            # Try the next position in the board (Breadth first search).
            boardCopy[key] = ' '

    # 2. If we get here, then no breadth first win detected, so try Depth first
    # search for a win (or loss to the opponent) This is the recursive case
    boardCopy = dict(board)
    openSpot = ''
    for key in boardCopy:
        if boardCopy[key]  == ' ':
            print("Trying depth search on openspot ", key)
            boardCopy[key] = currentTurn

            # This is just for detecting if we had any move open at all.
            if openSpot == '':
                openSpot = key

            if currentTurn == 'O':
                winner, pos  = simulate(boardCopy, 'X')
            else:
                winner, pos = simulate(boardCopy, 'O')

            # This is the minimax part...
            if winner == currentTurn:
                # We (currentTurn) wins if we take this spot we ocupied.
                return winner, key
            elif winner != '':
                # Opponent wins, we need to block that spot.
                return winner, pos

            # Try the next position in the board (Breadth first search).
            boardCopy[key] = ' '

    # If we get here, there was no winner
    if openSpot == '':
        print("Board full... Tie")
    else:
        print("No win for ", currentTurn, "... Returning any open spot ", openSpot)
    return '', openSpot

# Bugs
# 1. Moves 4, 1, 7 by user is not being detected

# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0
    for i in range(10): #iterate 9 times
        printBoard(masterBoard)

        if turn == 'O': #if O's turn
            print("It's " + turn + "'s turn!")
            winner, move = simulate(masterBoard, turn)
            if winner != '':
                print("Simulate detected that ", winner, " can win by taking position ", move)
            if move == '':
                print("Game Over. It's a Tie!")
                sys.exit()

            # Special case tic tac toe logic - if the middle position is still
            # open and we don't have a winner, pick that spot since the
            # computer is going second.  This is purely a non algorithmic
            # optimization for Tic Tac Toe.
            if count > 0 and masterBoard["5"] == ' ':
                print("Computer taking open mid position")
                move = "5"
        else:
            print("It's your turn, " + turn + ". Move to which place?")
            move = input()

        if masterBoard[move] == ' ': #if dict[key] = empty, put x in place
            masterBoard[move] = turn
            count += 1
        else:
            print("That place is already filled. Move to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        # Because the min # after which someone can win is in 5 counted moves from both.
        if count >= 5:
            if winLogic(masterBoard, turn):
                print("Game Over. ", turn, " Won!")
                sys.exit()

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

if __name__ == "__main__":
    game()
