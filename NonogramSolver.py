from Board import Board
from SolvingAlgorithms import SolvingAlgorithms

class NonogramSolver:

    def __init__(self, solving_vector_x, solving_vector_y):
        self.check_err(solving_vector_x, solving_vector_y)
        self.dimension = self.define_dimension(solving_vector_y)
        self.board = Board(self.dimension, solving_vector_x, solving_vector_y)   
        self.solv_algo = SolvingAlgorithms()

    def check_err(self, solving_vector_x, solving_vector_y):
        set_x, set_y  = set(map(len, solving_vector_x)), set(map(len, solving_vector_y))
        same_x, same_y = len(set_x), len(set_y)
        #x_miuses = 

        if same_x != 1 or same_y != 1: raise Exception("Invalid inside vector sizes!")
        if set_x.pop() != len(solving_vector_y): raise Exception("Invalid vectors proportions!")
    
    def define_dimension(self, solving_vector_y):
        return len(solving_vector_y)
        
    def show(self): 
        offset = len(self.board.solving_vector_y[0]) * 2 + 2
        minueses_amount = offset + self.board.dimension
        print('\n', '-' * minueses_amount, f"step no.{self.solv_algo.steps}", '-' * minueses_amount)

        for row in self.board.solving_vector_x:
            print(' ' * offset, end='[ ')
            for field in row: print(field, end=' ')
            print(']')

        for row_id in range(len(self.board.solving_vector_y)):
            print('[', *self.board.solving_vector_y[row_id], ']', end='')
            print(self.board.show_row(row_id))
       
    def solve(self, show_step=False):
        self.solv_algo.init_solv(self.board)
        if show_step: self.show()

        while not self.board.is_finished():
            self.solv_algo.next_solv(self.board)
            if show_step: self.show()    

    def show_clean(self):
        self.board.show()