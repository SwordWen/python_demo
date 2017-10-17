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
        if count != 9:
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

def reset_sudoku_number(sudoku_maxtrix, value):
    for i in range(9):
        for j in range(9):
            if sudoku_maxtrix[i][j] == value:
                sudoku_maxtrix[i][j] = 0



def set_sudoku_number(sudoku_maxtrix, value):
    random.seed()
    row_record = [0 for x in range(9)]
    column_record = [0 for x in range(9)]
    cell_record = [0 for x in range(9)]
    #print row_record
    count = 0
    while(count < 9):

        x, y = get_empty_index(sudoku_maxtrix, row_record, column_record, cell_record)
        cell_index = get_cell_index(x, y)
        #print "get_empty_index: ({0},{1})".format(x, y)
        if x == -1: 
            print "get_empty_index for value {0} failed: ({1},{2})".format(value, x, y)
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
                print "get_empty_index for value {0} failed: ({1},{2})".format(value, x, y)
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
            reset_sudoku_number(sudoku_maxtrix, i + 1)
            for j in range(10):
                result = set_sudoku_number_with_random(sudoku_maxtrix, i + 1) 
                if result == True:
                    break
                else:
                    reset_sudoku_number(sudoku_maxtrix, i + 1)
                
            if result == False:
                return False
    return True

def set_sudoku_number_dynamic(sudoku_maxtrix, value, stack=[]):
    row_record = [0 for x in range(9)]
    column_record = [0 for x in range(9)]
    cell_record = [0 for x in range(9)]
    #stack = []
    x = 0
    y = 0

    if len(stack) > 0:
        (i , j) = stack.pop()
        sudoku_maxtrix[i][j] = 0
        x = i
        y = j + 1
        for i, j in stack:
            cell_index = get_cell_index(i, j)
            row_record[i] = value
            column_record[j] = value
            cell_record[cell_index] = value


    print "set_sudoku_number_dynamic: i={0}, j={1}, value={2}".format(x, y, value)
    while len(stack) < 9:
        #for x in range(0, 9):
        while x < 9:
            #for y in range(0, 9):
            while y < 9:
                cell_index = get_cell_index(x, y)
                # if value == 2:
                #     print "get_cell_index: x={0}, y={1}".format(x, y)
                if 0 == row_record[x] and 0 == column_record[y] and 0 == cell_record[cell_index] and sudoku_maxtrix[x][y]==0:
                    row_record[x] = value
                    column_record[y] = value
                    cell_record[cell_index] = value
                    sudoku_maxtrix[x][y] = value
                    print "find locaton({0}, {1}) for value {2}".format(x, y, value)
                    stack.append((x,y))
                y = y + 1
            x = x + 1
            y = 0

        if len(stack) == 0:
            print "Can't set_sudoku_number_dynamic with value " + str(value)
            break
        elif len(stack) < 9:            
            (i, j) = stack.pop()
            #print "Can't set_sudoku_number_dynamic, and re-try from " + str((i,j))
            #print sudoku_maxtrix
            cell_index = get_cell_index(i, j)
            row_record[i] = 0
            column_record[j] = 0
            cell_record[cell_index] = 0
            sudoku_maxtrix[i][j] = 0
            x = i
            y = j + 1


 
    print "stack for value({0}): ({1})".format(str(value), str(stack))
    print sudoku_maxtrix
    if len(stack) == 9:
        return True
    else:
        return False

def set_sudoku_case_dynamic(sudoku_maxtrix):
    stack_list = []
    index = 0
    stack = []
    while len(stack_list) < 9:
        # for i in range(index, 9):
        #     index = i
          
        result = set_sudoku_number_dynamic(sudoku_maxtrix, index+1, stack)
        if result == True:
            stack_list.append(stack)
            stack = []
            index = index + 1
        else:
            # print "Can't set sudoku number value = {0}".format(index+1)
            # reset_sudoku_number(sudoku_maxtrix, index + 1)

            if len(stack_list) == 0:
                print "Can't set_sudoku_case_dynamic with value " + str(index + 1)
                return False
            elif len(stack) > 0:
                print "Try to set_sudoku_case_dynamic with value " + str(index + 1)
            elif len(stack_list) < 9:
                stack = stack_list.pop()
                index = index - 1
            
    return True