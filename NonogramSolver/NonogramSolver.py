from Board import Board
from SolvingAlgorithm import SolvingAlgorithm


class NonogramSolver:

    def __init__(self, solving_vector_horizontal: list, solving_vector_vertical: list) -> None:
        solving_vector_horizontal, solving_vector_vertical = solving_vector_horizontal, solving_vector_vertical
        dimension_horizontal, dimension_vertical = self.__parse_solving_vectors(solving_vector_horizontal, solving_vector_vertical)
        self.board_info = (dimension_horizontal, dimension_vertical, solving_vector_horizontal, solving_vector_vertical)

    def __parse_solving_vectors(self, solving_vector_horizontal: int, solving_vector_vertical: int) -> tuple[int, int] | Exception:
        count_dimension = lambda vecotr_list: sum(vecotr_list) + len(vecotr_list) - 1
        
        max_dimension_horizontal = max(map(count_dimension, solving_vector_horizontal))
        max_dimension_vertical = max(map(count_dimension, solving_vector_vertical))
        len_solving_vector_vertical = len(solving_vector_vertical) 
        len_solving_vector_horizontal = len(solving_vector_horizontal)

        if max_dimension_horizontal > len(solving_vector_vertical) or max_dimension_vertical > len(solving_vector_horizontal):
            raise Exception("Invalid vectors size!")
        
        return len_solving_vector_vertical, len_solving_vector_horizontal

    @staticmethod
    def get_output_str(board: Board, is_resolved: bool, steps: int, time: float) -> str:
        padding_size = board.dimension_horizontal * 2

        padding_str = "-" * padding_size
        resolving_result = f"\rNonogram was{'' if is_resolved else ' not'} resolved!".rjust(padding_size)
        nonogram_info = f"\rNonogram size {board.dimension_horizontal}x{board.dimension_vertical}".rjust(padding_size)
        solving_stats = f"\rTook {steps} steps and {time} s!".rjust(padding_size)

        return str.join('\n', (padding_str, resolving_result, nonogram_info, solving_stats, padding_str, str(board)))
      
    def try_resolve(self, / ,interactive_output: bool = False) -> (Board, bool, int, float):
        board = Board(*self.board_info)
        solving_algo = SolvingAlgorithm(board)

        solving_algo_results = solving_algo.try_resolve_nonogram(interactive_output)
        if interactive_output:
            solving_algo_results_str = self.get_output_str(board, *solving_algo_results)
            print(solving_algo_results_str)

        return board, *solving_algo_results
