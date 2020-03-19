board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def printBoard(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if j%3==0:
                print("|",end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ",end="")

def isPossible(x,y,num):
    global board
    #check row:
    for i in range(0,9):
        if (board[x][i] == num):
            return False
    #check column:
    for i in range(0,9):
        if(board[i][y]== num):
            return False
    # ckeck sub Matrix:
    box_x = (y//3)
    box_y = (x//3)
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if board[i][j] == num:
                return False
    return True
print(isPossible(0,2,3))

def solve():
    global board
    for i in range(9):
        for j in range(9):
            if(board[i][j]==0):
                for n in range(1,10):
                    if isPossible(i,j,n):
                        board[i][j] = n
                        solve()
                        board[i][j]=0
                return
    printBoard(board) 

solve()



