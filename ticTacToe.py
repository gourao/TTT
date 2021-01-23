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

debugBoard1 = {'7': 'X' , '8': ' ' , '9': ' ' ,
               '4': ' ' , '5': 'O' , '6': ' ' ,
               '1': 'X' , '2': 'X' , '3': 'O' }

debugBoard2 = {'7': ' ' , '8': ' ' , '9': ' ' ,
               '4': ' ' , '5': 'O' , '6': 'X' ,
               '1': 'X' , '2': ' ' , '3': ' ' }

debugBoard3 = {'7': ' ' , '8': ' ' , '9': 'X' ,
               '4': ' ' , '5': 'O' , '6': ' ' ,
               '1': 'X' , '2': ' ' , '3': ' ' }

debugBoard4 = {'7': ' ' , '8': ' ' , '9': 'X' ,
               '4': ' ' , '5': 'O' , '6': ' ' ,
               '1': 'X' , '2': ' ' , '3': 'O' }

debugBoard5 = {'7': ' ' , '8': 'O' , '9': 'X' ,
               '4': ' ' , '5': 'O' , '6': ' ' ,
               '1': 'X' , '2': 'X' , '3': ' ' }

# Basic outcomes of a board
WIN = 0x001
TIE = 0x010
LOSE = 0x100

'''We will have to print the updated board after every move in the game and
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function.'''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'] + "      7|8|9")
    print('-+-+-      -+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'] + "      4|5|6")
    print('-+-+-      -+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'] + "      1|2|3")

def winLogic(board, turn):
    value = False
    if board['7'] == board['8'] == board['9'] != ' ': # across the top # TURN WINNING LOGIC INTO A SEPARATE FUNCTION
        print("**** " + turn + " will win (7 - 8 - 9). ****")
        value = True
    elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
        print("**** " + turn + " will win (4 - 5 - 6). ****")
        value = True
    elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
        print("**** " + turn + " will win (1 - 2 - 3). ****")
        value = True
    elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
        print("**** " + turn + " will win (1 - 4 - 7). ****")
        value = True
    elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
        print("**** " + turn + " will win (2 - 5 - 8). ****")
        value = True
    elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
        print("**** " + turn + " will win (3 - 6 - 9). ****")
        value = True
    elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
        print("**** " + turn + " will win (7 - 5 - 3). ****")
        value = True
    elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
        print("**** " + turn + " will win (1 - 5 - 9). ****")
        value = True
    return value

def opposite(turn):
    if turn == 'O':
        return 'X'
    else:
        return 'O'

# Rank a board in it's current layout
def rank(board, currentTurn):
    print("Ranking board for ", currentTurn)
    printBoard(board)

    boardCopy = dict(board)
    result = 0x0
    for key in boardCopy:
        if boardCopy[key]  == ' ':
            boardCopy[key] = currentTurn

            if winLogic(boardCopy, currentTurn):
                # Base case, win found.  We win if we take this spot.
                if currentTurn == 'O':
                    result = result | WIN
                else:
                    result = result | LOSE
            else:
                # Recurse on the next turn
                result = result | rank(boardCopy, opposite(currentTurn))

            # Try the next position in the board (Breadth first search).
            boardCopy[key] = ' '

    if result == 0x0:
        result = TIE

    return result


# scoreMap scores various board combinations in this order:
# [W] > [W,T] > [T] > [W,T,L] > [W,L] > [T,L] > [L]
scoreMap = {WIN: 7,
    WIN | TIE: 6,
    TIE: 5,
    WIN | TIE | LOSE: 4,
    WIN | LOSE: 3,
    TIE | LOSE: 2,
    LOSE: 1}


# Chose a suitable move by ranking every open spot
def run(board):
    bestKey = ''
    bestResult = 0x0
    bestResultStr = ""

    boardCopy = dict(board)
    for key in boardCopy:
        if boardCopy[key]  == ' ':
            print("Trying openspot ", key)
            boardCopy[key] = 'O'

            result = rank(boardCopy, 'X')

            # For debugging only
            resultStr = ''
            if result & WIN:
                resultStr += ' W '
            if result & LOSE:
                resultStr += ' L '
            if result & TIE:
                resultStr += ' T '
            print("Result at ", key, " is ", resultStr)

            if bestResult == 0x0:
                bestResult = result
                bestKey = key
                bestResultStr = resultStr
            elif scoreMap[result] > scoreMap[bestResult]:
                bestResult = result
                bestKey = key
                bestResultStr = resultStr

            # Try the next position in the board (Breadth first search).
            boardCopy[key] = ' '

    print("Chosing position ", bestKey, " for a result of ", bestResultStr)

    return bestKey

def debug():
    run(debugBoard5)

# XXX FIXME hack moves
def isCornered(board):
    if board["1"] == board["9"] == 'X':
        return True
    elif board["7"] == board["3"] == 'X':
        return True
    return False

def openMid(board):
    if board["8"] == ' ':
        return "8"
    elif board["6"] == ' ':
        return "6"
    elif board["2"] == ' ':
        return "2"
    else:
        return "4"

# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    round = 0
    for i in range(10): #iterate 9 times
        print("\n\n\n\n\n\n---------------------------------------------\n\n\n")
        print("Round ", round, "... Board Layout:")
        printBoard(masterBoard)
        print("It's " + turn + "'s turn!")

        if turn == 'O': # Computer's turn
            # XXX TODO Why can't the algorithm figure this out?
            # Special case tic tac toe logic - if the middle position is still
            # open and we don't have a winner, pick that spot since the
            # computer is going second.  This is purely a non algorithmic
            # optimization for Tic Tac Toe.
            if round > 0 and masterBoard["5"] == ' ':
                print("*** BOOK MOVE: Computer taking open mid position")
                move = "5"
            elif round > 0 and isCornered(masterBoard):
                move = openMid(masterBoard)
            else:
                move = run(masterBoard)
        else:
            print("It's your turn, " + turn + ". Move to which place?")
            move = input()

        if masterBoard[move] == ' ': #if dict[key] = empty, put x in place
            masterBoard[move] = turn
            round += 1
        else:
            print("That place is already filled. Move to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        # Because the min # after which someone can win is in 5 rounded moves from both.
        if round >= 5:
            if winLogic(masterBoard, turn):
                print("Game Over. ", turn, " Won!")
                sys.exit()
        elif round >= 8:
                print("Game Over. Tie Game!")
                sys.exit()

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

if __name__ == "__main__":
	debug()
# game()
