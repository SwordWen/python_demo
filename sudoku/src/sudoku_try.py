'''
Created on 2014-2-8

@author: swordw
'''

import random
#Horizontal
#Vertical

class Sudoku(object):
    def __init__(self,max_row=9):
        self.row_count=max_row
        self.sudoku_list=[[0]*max_row for i in range(max_row)]
        
    def print_sudoku(self):
        for row in self.sudoku_list:
            print row   
    
    def multi_sequence(self,num):
        total = 1
        for i in range(num):            
            total = total * (i+1)
        return total
                    
                
    def calc_sudoku_possibilty(self):
        total = 1
        for i in range(self.row_count):            
            total = total * self.multi_sequence(i+1)
            print "calc_sudoku_possibilty:"+str(total)
        return total
                

def print_sudoku():
    sudoku = Sudoku(9)
    sudoku.print_sudoku()
    print sudoku.multi_sequence(9)
    print sudoku.calc_sudoku_possibilty()
   

def main():
    print random.randrange(1, 9, 1)
    print_sudoku()
    #print random.randint(1, 9)
    print("sudoku")

if __name__ == "__main__":
    main()