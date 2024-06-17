## Sudoko Solver

board = [
    [0,0,0,5,0,0,2,0,9],
    [0,4,2,0,1,0,0,0,0],
    [6,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,5,0,2,0],
    [0,3,0,0,0,7,0,0,0],
    [0,6,9,2,0,0,0,0,0],
    [0,0,0,0,6,0,0,0,0],
    [0,0,0,0,0,8,0,0,4],
    [3,9,0,0,0,0,7,0,6]
]


## Function to print sukodo board
def print_board(board):
    for i in range(len(board)):
        if i in [3,6]:
            print('------' + '|' + '-------' + '|' + '-------' + '\n')
        for j in range(len(board[0])):
            if j in [3,6] and board[i][j]!= 0 :
                print('|' + ' ' +str(board[i][j]),end = ' ')
            elif j in [3,6] and board[i][j]== 0:
                print('|' + ' ' +'_',end = ' ')
            elif board[i][j] == 0:
                print('_',end=' ')
            else:
                print(str(board[i][j]),end=' ')
        print('\n')


## Function to find first empty cell
def first_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return [i,j]
    return False


## Function to check in matrix
def matrix_check(num,x,y,board):
    dist1 = {0:[0,1,2],
             1:[0,1,2],
             2:[0,1,2],
             3:[3,4,5],
             4:[3,4,5],
             5:[3,4,5],
             6:[6,7,8],
             7:[6,7,8],
             8:[6,7,8]}
    
    for i in dist1[x]:
        for j in dist1[y]:
            if board[i][j] == num:
                return False
    
    return True



## Function to check the placement
def placement(num,board):
    cell = first_empty(board)
    if cell:
        if num not in board[cell[0]] and num not in [board[x][cell[1]] for x in range(len(board))] and matrix_check(num,cell[0],cell[1],board):
            return True
    
    return False

## Function to solve Sudoko
def solve(board):
    cell = first_empty(board)
    for i in range(1,10):
        if placement(i,board):
            board[cell[0]][cell[1]] = i
            if not first_empty(board):
                return board
            sol = solve(board)
            if not sol:
                board[cell[0]][cell[1]] = 0
                continue
            else:
                return board
    return False


print_board(solve(board))