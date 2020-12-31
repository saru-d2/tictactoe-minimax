HUMAN = 1
AI = 2
from math import inf


class Board:
    def __init__(self, h_choice):
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # fyi this is 3x3 grid
        if (h_choice == 'x' or h_choice == 'X'):
            self.aiSym = 'O'
            self.hSym = 'X'
        else:
            self.aiSym = 'X'
            self.hSym = 'O'
        self.key = {HUMAN: self.hSym, AI: self.aiSym, 0: ' '}

    def show(self):
        print()
        for i in range(0, 3):
            for j in range(0, 3):
                print(self.key[int(self.grid[i][j])], end='')
                if (j < 2):
                    print('|', end='')
                else:
                    print('')
            if (i < 2):
                print('-+-+-')

    def humanInput(self, inp):
        if inp not in range(0, 9):
            return -1
        i = int(inp / 3)
        j = inp % 3
        if self.grid[i][j] == 0:
            self.grid[i][j] = HUMAN
            return 1
        else:
            return -1

   

    def aiTurn(self):
        emptyCells = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[i][j] == 0:
                    emptyCells.append([i, j])
        depth = len(emptyCells)
        # print(depth)

        if depth == 9:
            #first move, its best to play center obv
            self.aiPlay(1, 1)
            # print("4, 4")
            return 1
        else:
            move = self.getBestMove(emptyCells)
            self.aiPlay(move[0], move[1])
            # print(move)    
            return 1
    
    def aiPlay(self, i, j):
        self.grid[int(i)][int(j)] = AI

    def getBestMove(self, emptyCells):
        #this is the minimax part, bestest
        #calls a recursive function

        best = minimax(self.grid, len(emptyCells), AI)
        # print(best)
        return [best[1], best[2]]



    def checkWin(self):
        b = self.grid

        winCases = [
            [b[0][0], b[0][1], b[0][2]],
            [b[1][0], b[1][1], b[1][2]],
            [b[2][0], b[2][1], b[2][2]],
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]],
        ]

        if [HUMAN, HUMAN, HUMAN] in winCases:
            return HUMAN
        elif [AI, AI, AI] in winCases:
            return AI
        else:
            return 0
    

def minimax(grid, depth, cur):
    if cur == AI:
        next = HUMAN
        #cur = ai
        best = [-inf, -1, -1]
    else:
        next = AI
        #cur = human
        best = [inf, -1, -1]

    winRet = checkWin(grid)
    if depth == 0 or (winRet != 0):
        if (winRet == AI):
            return [1, -1, -1]
        elif (winRet == HUMAN):
            return[-1, -1, -1]
        else:
            return [0, -1, -1]
    emptyCells = getEmptyCells(grid)
    for cell in emptyCells:
        x = cell[0]
        y = cell[1]
        grid[x][y] = cur
        score = minimax(grid, depth - 1, next)
        score[1] = x
        score[2] = y
        grid[x][y] = 0
        if cur == AI:
            if score[0] > best[0]:
                best = score
        else:
            if score[0] < best[0]:
                best = score
    # print(depth, best)
    return best
        
def checkWin(grid):
    b = grid

    winCases = [
        [b[0][0], b[0][1], b[0][2]],
        [b[1][0], b[1][1], b[1][2]],
        [b[2][0], b[2][1], b[2][2]],
        [b[0][0], b[1][0], b[2][0]],
        [b[0][1], b[1][1], b[2][1]],
        [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]],
        [b[0][2], b[1][1], b[2][0]],
    ]

    if [HUMAN, HUMAN, HUMAN] in winCases:
        return HUMAN
    elif [AI, AI, AI] in winCases:
        return AI
    else:
        return 0

def getEmptyCells(grid):
    ret = []
    for i in range(0, 3):
        for j in range (0, 3):
            if grid[i][j] == 0:
                ret.append([i, j])
    return ret