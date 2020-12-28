#Implementation of Two Player Tic-Tac-Toe game in Python.
#Sources: https://dev.to/jamesshah/the-classic-tictactoe-game-in-python-cpi
#         https://www.amazon.in/Automate-Boring-Stuff-Python-Programming-ebook/dp/B00WJ049VU/ref=as_li_ss_tl?crid=36GA0S183R1H9&keywords=automate+the+boring+stuff+with+python&qid=1573710172&sprefix=Automate+t,aps,372&sr=8-1&linkCode=sl1&tag=bytetales-21&linkId=365febe171431796e07d4419d0a621ca&language=en_IN
import random

#PROBLEM: PROGRAM DOESN'T TERMINATE

def repo2():
  return max(3,2)
  
''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' } #board is a dictionary. the initial keys to the dictionary are empty strings

board_keys = []

for key in theBoard:
    board_keys.append(key) #generates this list: ['7', '8', '9', '4', '5', '6', '1', '2', '3'] BUT WHY?

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

    
def winLogic(turn):
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top # TURN WINNING LOGIC INTO A SEPARATE FUNCTION
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")                
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " + turn + " won. ****")

def rank(boardState, currentTurn):
    #create a copy of the board - how to create a copy of a variable in python?
    return

# Now we'll write the main function which has all the gameplay functionality.
def game():
    
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)

        if turn == 'O':
            print("It's " + turn + "'s turn!")
            move = rank(theBoard, turn)
            #str(random.randint(1, 9))
            
        else:
            print("It's your turn," + turn + ".Move to which place?")
            move = input() #asks for numerical input from turn, so the random must be before this
        
        if theBoard[move] == ' ': #if key = empty, put x in place
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            winLogic(turn)

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " " #erases everything

        game()

if __name__ == "__main__":
    game()