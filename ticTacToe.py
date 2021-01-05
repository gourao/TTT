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

debugBoard = {'7': 'X' , '8': ' ' , '9': ' ' ,
              '4': ' ' , '5': 'O' , '6': ' ' ,
              '1': 'X' , '2': 'X' , '3': 'O' }

# Outcomes of a board
WIN = 0x001
LOSE = 0x010
TIE = 0x100

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
        printBoard(board)
        print("**** " + turn + " will win (7 - 8 - 9). ****")
        value = True
    elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
        printBoard(board)
        print("**** " + turn + " will win (4 - 5 - 6). ****")
        value = True
    elif board['1'] == board['2'] == board['3'] != ' ': # across the bottom
        printBoard(board)
        print("**** " + turn + " will win (1 - 2 - 3). ****")
        value = True
    elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
        printBoard(board)
        print("**** " + turn + " will win (1 - 4 - 7). ****")
        value = True
    elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
        printBoard(board)
        print("**** " + turn + " will win (2 - 5 - 8). ****")
        value = True
    elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
        printBoard(board)
        print("**** " + turn + " will win (3 - 6 - 9). ****")
        value = True
    elif board['7'] == board['5'] == board['3'] != ' ': # diagonal
        printBoard(board)
        print("**** " + turn + " will win (7 - 5 - 3). ****")
        value = True
    elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
        printBoard(board)
        print("**** " + turn + " will win (1 - 5 - 9). ****")
        value = True
    return value

# Returns winner and position that will cause the win
def simulate(board, currentTurn):
    print("Running simulation for ", currentTurn)
    printBoard(board)

    # 1. Breadth first search for a winning spot
    found = false
    boardCopy = dict(board)
    for key in boardCopy:
        if boardCopy[key]  == ' ':
            found = true
            print("Trying breadth search on openspot ", key)
            boardCopy[key] = currentTurn

            if winLogic(boardCopy, currentTurn):
                # Base case, win found.  We win if we take this spot.
                print('Detected win by ', currentTurn, " at ", key)
                return currentTurn, key, WIN

            # Try the next position in the board (Breadth first search).
            boardCopy[key] = ' '

    if found == false:
        # No open spots, tie board
        return '', '', TIE

    # 2. If we get here, then no breadth first win detected, so try Depth first
    # search for a win (or loss to the opponent) This is the recursive case
    boardCopy = dict(board)
    bestResult = LOSE
    bestWinner = ''
    bestPos = ''
    # Note: We are now simulating the opponent
    for key in boardCopy:
        if boardCopy[key]  == ' ':
            print("Trying depth search on openspot ", key)
            boardCopy[key] = currentTurn

            if currentTurn == 'O':
                winner, pos, result = simulate(boardCopy, 'X')

                # Minimize results for the opponent
                if result == WIN:
                    return winner, pos, LOSE
            else:
                winner, pos, result = simulate(boardCopy, 'O')

                # Maximize results for us.  Find best possible outcome.
                # A loss is an immediate no go for this position.
                if result == LOSE:
                    return winner, pos, LOSE
                if result > bestResult:
                    bestWinner = winner
                    bestPos = pos
                    bestResult = result


            # Try the next position in the board (Breadth first search).
            boardCopy[key] = ' '

    print("Simulation results for ", currentTurn,
          " Winner: ", bestWinner,
          " Position: ", bestPos,
          " Result: ", bestResult)
    return bestWinner, bestPos, bestResult

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

            # [W] > [W,T] > [T] > [W,T,L] > [W,L] > [T,L] > [L]
            if bestResult == 0x0:
                bestResult = result
                bestKey = key
                bestResultStr = resultStr
            elif result == WIN:
                bestResult = result
                bestKey = key
                bestResultStr = resultStr
            elif result == WIN | TIE:
                bestResult = result
                bestKey = key
                bestResultStr = resultStr
            elif result == TIE:
                bestResult = result
                bestKey = key
                bestResultStr = resultStr
            elif result == WIN | TIE | LOSS:
                bestResult = result
                bestKey = key
                bestResultStr = resultStr
            elif result == WIN | LOSS:
                bestResult = result
                bestKey = key
                bestResultStr = resultStr
            elif result == TIE | LOSS:
                bestResult = result
                bestKey = key
                bestResultStr = resultStr
            elif result == LOSS:
                bestResult = result
                bestKey = key
                bestResultStr = resultStr

            # Try the next position in the board (Breadth first search).
            boardCopy[key] = ' '

    print("Chosing position ", key, " for a result of ", bestResultStr)

def debug():
    run(debugBoard)

# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    round = 0
    for i in range(10): #iterate 9 times
        print("\n\n\n\n\n\n---------------------------------------------\n\n\n")
        print("Round ", round, "... Board Layout:")
        printBoard(masterBoard)

        if turn == 'O': #if O's turn
            print("It's " + turn + "'s turn!")
            winner, move, result = simulate(masterBoard, turn)
            if winner != '':
                print("Simulate detected that ",
                      winner, " can win by taking position ", move,
                      " with a result of ", result)
            if move == '':
                print("Game Over. It's a Tie!")
                sys.exit()

            # XXX TODO is this needed?
            # Special case tic tac toe logic - if the middle position is still
            # open and we don't have a winner, pick that spot since the
            # computer is going second.  This is purely a non algorithmic
            # optimization for Tic Tac Toe.
            if round > 0 and masterBoard["5"] == ' ':
                print("*** BOOK MOVE: Computer taking open mid position")
                move = "5"
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

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

if __name__ == "__main__":
    debug()
    # game()
