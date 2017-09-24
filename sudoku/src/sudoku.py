import random

import numpy as np

#ematrix = np.zeros( (9,9) )
#print matrix

def check_row(sudoku_maxtrix, index):
    count = 0
    for i in range(9):
        #print sudoku_maxtrix[index]
        if sudoku_maxtrix[index][i] == i+1:
            count = count + 1
        else:
            count = count + 2
        #print "sudoku_maxtrix[index][i]={0},count={1}".format(sudoku_maxtrix[index][i], count)
        if count != i+1:
            return False
    return True

def check_column(sudoku_maxtrix, index):
    pass

def check_cell(sudoku_maxtrix, index_x, index_y):
    pass

def get_cell_index(x, y):
    cell_x = x/3
    cell_y = y/3
    index = cell_x * 3 + cell_y
    return index

def get_empty_index(sudoku_maxtrix, row_record, column_record, cell_record):
    for i in range(9):
        for j in range(9):
            if row_record[i] == 0 and column_record[j] == 0 and sudoku_maxtrix[i][j] == 0:
                cell_index = get_cell_index(i, j)
                if cell_record[cell_index] == 0:
                    return i, j
    print sudoku_maxtrix
    return -1, -1


def set_sudoku_number_with_random(sudoku_maxtrix, value):
    random.seed()
    row_record = [0 for x in range(9)]
    column_record = [0 for x in range(9)]
    cell_record = [0 for x in range(9)]
    #print row_record
    count = 0
    while(count < 9):
        x = random.randint(0,8)
        y = random.randint(0,8)
        #print "set_sudoku_number: ({0},{1})".format(x, y)
        cell_index = get_cell_index(x, y)
        if sudoku_maxtrix[x][y] != 0 :
            x, y = get_empty_index(sudoku_maxtrix, row_record, column_record, cell_record)
            cell_index = get_cell_index(x, y)
            #print "get_empty_index: ({0},{1})".format(x, y)
            if x == -1: 
                print "get_empty_index failed: ({0},{1})".format(x, y)
                return False
        
        if 0 == row_record[x] and 0 == column_record[y] and 0 == cell_record[cell_index]:
            row_record[x] = value
            column_record[y] = value
            cell_record[cell_index] = value
            sudoku_maxtrix[x][y] = value
            count = count + 1
    
    return True
    # print row_record
    # print column_record
    # print cell_record

def set_sudoku_case(sudoku_maxtrix):
    for i in range(9):
        print("set sudoku with value: {0}".format(i+1))
        result = set_sudoku_number_with_random(sudoku_maxtrix, i + 1)   
        print  sudoku_maxtrix
        if result is False:
            return False
    return True
