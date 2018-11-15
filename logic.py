import random

GRID_LEN = 4
DEFAULT = 2
EMPTY = 0
NEW = [2,4]
WIN = 2048

def init_matrix():
    idxs = random.sample(range(GRID_LEN*GRID_LEN), 2)
    idx = 0
    matrix = []
    for i in range(GRID_LEN):
        row = []
        for j in range(GRID_LEN):
            if idx in idxs:
                row.append(DEFAULT)
            else:
                row.append(EMPTY)
            idx += 1
        matrix.append(row)

    #matrix[0][0] = 16
    #matrix[0][1] = 8
    #matrix[0][2] = 4
    #matrix[0][3] = 2
    return matrix

def equal(a, b):
    return a!=EMPTY and b!=EMPTY and a==b

def up(matrix):
    done = False
    for col in range(GRID_LEN):
        for row in range(1, GRID_LEN): # merge
            if equal(matrix[row-1][col], matrix[row][col]):
                matrix[row-1][col] *= 2
                matrix[row][col] = EMPTY
                done = True
        for row in range(1, GRID_LEN): # move to empty pos if matrix[row][col]!=EMPTY:
                if matrix[row][col]!=EMPTY:
                    tmp_row = row
                    while tmp_row-1>=0 and matrix[tmp_row-1][col]==EMPTY:
                        tmp_row -= 1
                    if matrix[tmp_row][col]==EMPTY:
                        matrix[tmp_row][col] = matrix[row][col]
                        matrix[row][col] = EMPTY
                        done = True
    return done

def down(matrix):
    done = False
    for col in range(GRID_LEN):
        for i in range(1, GRID_LEN): # merge
            row = GRID_LEN-1-i
            if equal(matrix[row][col], matrix[row+1][col]):
                matrix[row+1][col] *= 2
                matrix[row][col] = EMPTY
                done = True
        for i in range(1, GRID_LEN): # move to empty pos
            row = GRID_LEN-1-i
            if matrix[row][col]!=EMPTY:
                tmp_row = row
                while tmp_row+1<GRID_LEN and matrix[tmp_row+1][col]==EMPTY:
                    tmp_row += 1
                if matrix[tmp_row][col]==EMPTY:
                    matrix[tmp_row][col] = matrix[row][col]
                    matrix[row][col] = EMPTY
                    done = True
    return done

def left(matrix):
    done = False
    for row in range(GRID_LEN):
        for col in range(1, GRID_LEN): # merge
            if equal(matrix[row][col], matrix[row][col-1]):
                matrix[row][col-1] *= 2
                matrix[row][col] = EMPTY
                done = True
        for col in range(1, GRID_LEN): # move to empty pos
            if matrix[row][col]!=EMPTY:
                tmp_col = col
                while tmp_col-1>=0 and matrix[row][tmp_col-1]==EMPTY:
                    tmp_col -= 1
                if matrix[row][tmp_col]==EMPTY:
                    matrix[row][tmp_col] = matrix[row][col]
                    matrix[row][col] = EMPTY
                    done = True
    return done

def right(matrix):
    done = False
    for row in range(GRID_LEN):
        for i in range(1, GRID_LEN): # merge
            col = GRID_LEN-1-i
            if equal(matrix[row][col], matrix[row][col+1]):
                matrix[row][col+1] *= 2
                matrix[row][col] = EMPTY
                done = True
        for i in range(1, GRID_LEN): # move to empty pos
            col = GRID_LEN-1-i
            if matrix[row][col]!=EMPTY:
                tmp_col = col
                while tmp_col+1<GRID_LEN and matrix[row][tmp_col+1]==EMPTY:
                    tmp_col += 1
                if matrix[row][tmp_col]==EMPTY:
                    matrix[row][tmp_col] = matrix[row][col]
                    matrix[row][col] = EMPTY
                    done = True
    return done

def move(matrix, direction):
    switch = {
            "up":up,
            "down":down,
            "left":left,
            "right":right,
        }
    case = switch[direction]
    return case(matrix)

def add_new(matrix):
    tmp = []
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            if matrix[i][j]==EMPTY:
                tmp.append([i,j])
    if len(tmp)>0:
        rand = random.choice(tmp)
        matrix[rand[0]][rand[1]] = random.choice(NEW)

def is_win(matrix):
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            if matrix[i][j]==WIN:
                return True
    return False

def get_neighbour(i,j):
    offsets = [[-1,0],[1,0],[0,-1],[0,1]]
    ret = []
    for o in offsets:
        tmp_i, tmp_j = i+o[0], j+o[1]
        if tmp_i>=0 and tmp_i<GRID_LEN and tmp_j>=0 and tmp_j<GRID_LEN :
            ret.append([tmp_i,tmp_j])
    return ret

def game_over(matrix):
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            if matrix[i][j]==EMPTY:
                return False
            neighbours = get_neighbour(i,j)
            for t in neighbours:
                if equal(matrix[t[0]][t[1]], matrix[i][j]):
                    return False
    return True





