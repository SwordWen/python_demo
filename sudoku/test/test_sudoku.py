import unittest
import sys
import math

import numpy as np

sys.path.append("../src")

from sudoku import check_row
from sudoku import get_cell_index
from sudoku import set_sudoku_number_with_random
from sudoku import set_sudoku_number
from sudoku import set_sudoku_number_dynamic
from sudoku import set_sudoku_case

class TestSudoku(unittest.TestCase):

    def test_check_row_1(self):
        matrix = np.zeros( (9,9) ,dtype=int)
        #print matrix
        #print "distance(1,1,0,0) = " + str(distance(1,1,0,0))
        self.assertEqual(check_row(matrix, 0), False)
        for i in range(9):
            matrix[0][i] = i + 1
        #print matrix
        self.assertEqual(check_row(matrix, 0), True)

    def test_get_cell_index(self):
        self.assertEqual(get_cell_index(0, 0), 0)
        self.assertEqual(get_cell_index(8, 8), 8)

    def test_set_sudoku_number_with_random(self):
        matrix = np.zeros( (9,9) ,dtype=int)
        set_sudoku_number_with_random(matrix, 1)
        print "set_sudoku_number_with_random:"
        print matrix

    def test_set_sudoku_number(self):
        matrix = np.zeros( (9,9) ,dtype=int)
        set_sudoku_number(matrix, 1)
        print "set_sudoku_number:"
        print matrix

    def test_set_sudoku_number_dynamic(self):
        matrix = np.zeros( (9,9) ,dtype=int)
        set_sudoku_number_dynamic(matrix, 1)
        print "set_sudoku_number_dynamic:"
        print matrix

    # def test_set_sudoku_case(self):
    #     matrix = np.zeros( (9,9) ,dtype=int)
    #     for i in range(1):
    #         matrix = np.zeros( (9,9) ,dtype=int)
    #         if True == set_sudoku_case(matrix):
    #             break
    #     for i in range(9):
    #         print matrix[i]
    #         self.assertEqual(check_row(matrix, i), True)




if __name__ == '__main__':
    unittest.main()