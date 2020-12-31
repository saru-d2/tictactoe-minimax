from board import *
import os
print("Welcome to your doom")

def clear():
    os.system('clear')

inputFine = False
while not inputFine:
    hCh = input("Choose your poison (X/O)")
    if hCh in ['x', 'X', 'o', 'O']:
        inputFine = True
    else:
        print("abbey 2 year old READ")
board_obj = Board(hCh)

inputFine = False

while not inputFine:
    stFirst = input("Would you like to start first?")
    if stFirst in ['y', 'Y', 'n', 'N']:
        inputFine = True
    else:
        print("abbey 2 year old READ")
aiGo = False
if stFirst in ['n', 'N']:
    aiGo = True

gameOver = False
totMoves = 0
chkRet = 0
while not gameOver and totMoves < 10:
    if aiGo:
        board_obj.aiTurn()
        totMoves += 1 
        aiGo = False
    clear()
    board_obj.show()
    humanDumb = True

    while humanDumb:
        try:
            inp = int(input("please give input: "))
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')
            continue
        ret = board_obj.humanInput(inp)
        
        if ret == 1:
            humanDumb = False
            totMoves += 1 
        else: 
            print("you absolute numbskull!, try again")
    print("hihi")

    chkRet = board_obj.checkWin()
    if chkRet > 0:
        break
    board_obj.aiTurn()        
    totMoves += 1 

    chkRet = board_obj.checkWin()
    if chkRet > 0:
        break
clear()
board_obj.show()
if chkRet == 0:
    print("tie")
elif chkRet == AI:
    print("AI")
else:
    print("HUMAN")
