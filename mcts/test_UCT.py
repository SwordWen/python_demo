import unittest
import sys
import math



from UCT import OXOState
from UCT import OXOStateEX

class TestOXOState(unittest.TestCase):  

    def test_OXOState_1(self):
        state = OXOState()
        print state.GetMoves()

class TestOXOStateEX(unittest.TestCase):  

    def test_OXOStateEx_1(self):
        board_size = 11
        win_length = 5
        state = OXOStateEX(board_size, win_length)
        self.assertEqual(len(state.GetMoves()), math.pow(board_size,2)) 

if __name__ == '__main__':
    unittest.main()