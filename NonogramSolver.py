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
        if same_x != 1 or same_y != 1: raise Exception("Invalid vector sizes!")
        if set_x.pop() != len(solving_vector_y): raise Exception("Invalid vectors proportions!")
    
    def define_dimension(self, solving_vector_y):
        return len(solving_vector_y)

    def solve_horizontally(self, index): 
        board_list = self.board.get_column(index)
        vector = self.board.get_vector_y(index)

        print(board_list)
        print(vector)
        
    def show(self): 
        offset = len(self.board.solving_vector_y[0]) * 2 + 2
        for row in self.board.solving_vector_x:
            print(' ' * offset, end='[ ')
            for field in row: print(field, end=' ')
            print(']')

        for row_id in range(len(self.board.solving_vector_y)):
            print('[', *self.board.solving_vector_y[row_id], ']', end='')
            print(self.board.show_row(row_id))

    def solve(self):
        self.solv_algo.init_solv(self.board)
        self.show()

if __name__ == "__main__": 
    solving_vector_x = [[0,0,0,0,2,0],
                        [1,5,2,5,1,2]]

    solving_vector_y = [[2,1], 
                        [1,3], 
                        [1,2], 
                        [0,3], 
                        [0,4], 
                        [0,1]]

    ns = NonogramSolver(solving_vector_x, solving_vector_y) 
    ns.solve()
     
    