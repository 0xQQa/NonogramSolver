from Board import Board
from SolvingAlgorithm import SolvingAlgorithm


class NonogramSolver:

    def __init__(self, solving_vector_horizontal: list, solving_vector_vertical: list) -> None:
        dimension_horizontal, dimension_vertical = self.__parse_solving_vectors(solving_vector_horizontal, solving_vector_vertical)
        self.board = Board(dimension_horizontal, dimension_vertical, solving_vector_horizontal, solving_vector_vertical)   
        self.solving_algo = SolvingAlgorithm(self.board)

    def __parse_solving_vectors(self, solving_vector_horizontal: int, solving_vector_vertical: int) -> tuple[int, int] | Exception:
        count_dimension = lambda vecotr_list: sum(vecotr_list) + len(vecotr_list) - 1
        
        max_dimension_horizontal = max(map(count_dimension, solving_vector_horizontal))
        max_dimension_vertical = max(map(count_dimension, solving_vector_vertical))
        len_solving_vector_vertical = len(solving_vector_vertical) 
        len_solving_vector_horizontal = len(solving_vector_horizontal)

        if max_dimension_horizontal > len(solving_vector_vertical) or max_dimension_vertical > len(solving_vector_horizontal):
            raise Exception("Invalid vectors size!")
        
        return len_solving_vector_vertical, len_solving_vector_horizontal

    def try_resolve(self, intertactive_output:bool = True) -> (bool, int, float):
        valid, steps, time = self.solving_algo.try_resolve_nonogram(intertactive_output)
        if intertactive_output:
            padding_size = self.board.dimension_horizontal * 2
            print("-" * padding_size)
            print(f"\rNonogram was{'' if valid else ' not'} resolved!".rjust(padding_size))
            print(f"\rNonogram size {self.board.dimension_horizontal}x{self.board.dimension_vertical}".rjust(padding_size))
            print(f"\rTook {steps} steps and {time} s!".rjust(padding_size))
            print("-" * padding_size)
            print(self.board)

        return valid, steps, time
