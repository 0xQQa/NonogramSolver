from Board import Board
from SolvingAlgorithms import SolvingAlgorithms

class NonogramSolver:

    def __init__(self, solving_vector_x, solving_vector_y):
        
        self.dimension_y, self.dimension_x  = self.define_dimension(solving_vector_y, solving_vector_x)
        self.check_err(solving_vector_x, solving_vector_y)
        self.board = Board(self.dimension_x, self.dimension_y, solving_vector_x, solving_vector_y)   
        self.solv_algo = SolvingAlgorithms()

    def check_err(self, solving_vector_x, solving_vector_y, vector_x_dimension, vector_y_dimension):
        for val in solving_vector_x:
            if not isinstance(val, input) or sum(val) + len(val) - 1 > vector_x_dimension: raise Exception("Invalid vector value!")

        for val in solving_vector_x:
            if not isinstance(val, input) or sum(val) + len(val) - 1 > vector_y_dimension: raise Exception("Invalid vector value!")
             
    
    def define_dimension(self, solving_vector_y, solving_vector_x):
        return len(solving_vector_y), len(solving_vector_x)
        
    def show(self): 
        offset = len(self.board.solving_vector_y[0]) * 2 + 2
        minueses_amount = offset + self.board.dimension_y
        print('\n', '-' * minueses_amount, f"step no.{self.solv_algo.steps}", '-' * minueses_amount)

        for row in self.board.solving_vector_x:
            print(' ' * offset, end='[ ')
            for field in row: print(field, end=' ')
            print(']')

        for row_id in range(len(self.board.solving_vector_y)):
            print('[', *self.board.solving_vector_y[row_id], ']', end='')
            print(self.board.show_row(row_id))
       
    def try_show(self, show_step):      #fixme
        if show_step: self.board.show()
        print()             

    def solve(self, show_step=False):
        self.solv_algo.init_solv(self.board)
        #self.try_show(show_step)

        while self.board.changes_made:
            self.board.changes_made = False
            self.solv_algo.next_solv(self.board)
            #self.try_show(show_step)

        print(f"Solution {'founded' if self.board.is_finished() else 'not found'}!")

    def show_clean(self):
        self.board.show()