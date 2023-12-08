from Board import Board
from SolvingAlgorithm import SolvingAlgorithm
from os import get_terminal_size

class NonogramSolver:

    def __init__(self, solving_vector_x: list, solving_vector_y: list) -> None:
        dimension_x, dimension_y = self.parse_solving_vectors(solving_vector_x, solving_vector_y)
        self.board = Board(dimension_x, dimension_y, solving_vector_x, solving_vector_y)   
        self.solving_algo = SolvingAlgorithm(self.board)

    def parse_solving_vectors(self, solving_vector_x: int, solving_vector_y: int) -> tuple[int, int] | Exception:
        parse_dimension = lambda x: sum(x) + len(x) - 1
        
        max_dimension_x = max(map(parse_dimension, solving_vector_x))
        max_dimension_y = max(map(parse_dimension, solving_vector_y))

        if max_dimension_x > len(solving_vector_y) or max_dimension_y > len(solving_vector_x):
            raise Exception("todo")
        
        return len(solving_vector_y), len(solving_vector_x)

    def try_resolve(self) -> None:
        valid, steps, time = self.solving_algo.try_resolve_nonogram()
        print(f"Nonogram was{'' if valid else ' not'} resolved!")
        print(f"Took {steps} steps and {time} s!")
        print("-" * self.board.dimension_y * 2)


if __name__ == "__main__":
    #print(SolvingGenerator().get_initial_valid_vector([4,4], 10))
    def t_1():
        solving_vector_x = [[6,6,7],
                            [6,4,5,1],
                            [4,1,3,5,3],
                            [3,2,4,4],
                            [2,1,3],
                            [1,2,4],
                            [2,2,1,6],
                            [2,6,3],
                            [2,12],
                            [2,12],
                            [2,7],
                            [2,2,8],
                            [2,1,4,5],
                            [2,1,3,3],
                            [2,3,1,2],
                            [2,9],
                            [1,1,1,2,2],
                            [2,2,1,2],
                            [2,1,1,1],
                            [2,2,3],
                            [3,3],
                            [2,2,2],
                            [2,1,4],
                            [2,2],
                            [6]]

        solving_vector_y = [[7],
                            [11],
                            [3,3],
                            [3,3],
                            [4,2],
                            [3,2],
                            [2,1,2],
                            [3,6,1],
                            [2,2,1,2],
                            [1,1,6,1],
                            [2,2,1,2],
                            [3,2,2,2],
                            [3,2,4,1,1],
                            [2,4,1,1,2,2,1],
                            [2,12,2,1],
                            [1,1,15,1],
                            [1,2,2,6,2,1],
                            [5,5,1,1],
                            [4,5,3],
                            [3,6,2],
                            [3,1,5,1],
                            [2,1,2,2,2],
                            [1,5,1,2],
                            [1,5,1,2],
                            [7,1,2]]
        return solving_vector_x, solving_vector_y

    solving_vector_y,solving_vector_x = t_1()
    asd = NonogramSolver(solving_vector_x,solving_vector_y)
    asd.try_resolve()
    print(asd.board)
  
    


