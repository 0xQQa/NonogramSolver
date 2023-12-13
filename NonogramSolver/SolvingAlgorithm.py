from Board import Board
from SolvingGenerator import SolvingGenerator
from timeit import default_timer as timer
from LoadingPrompt import LoadingPrompt


class SolvingAlgorithm:

    def __init__(self, board: Board) -> None:
        self.steps = 0
        self.board = board
        self.solving_generator = SolvingGenerator(board)
        self.loading_prompt = LoadingPrompt()

    def __resolve_one_dimension(self, dimension: int, solving_vector: list, set_dimension: callable, get_dimension_values: callable=lambda _: None) -> None:
        for idx, vector in enumerate(solving_vector):
            confident_solution = self.solving_generator.get_valid_vector(vector, dimension, get_dimension_values(idx))
            set_dimension(idx, confident_solution)

    def __resolve_initial_state(self) -> None:
        self.steps += 1
        self.__resolve_one_dimension(self.board.dimension_horizontal, self.board.solving_vector_horizontal, self.board.set_dimension_horizontal)
        self.__resolve_one_dimension(self.board.dimension_vertical, self.board.solving_vector_vertical, self.board.set_dimension_vertical)
        
    def __resolve_next_state(self) -> None:
        self.steps += 1
        self.__resolve_one_dimension(self.board.dimension_horizontal, self.board.solving_vector_horizontal, self.board.set_dimension_horizontal, self.board.get_dimension_horizontal)
        self.__resolve_one_dimension(self.board.dimension_vertical, self.board.solving_vector_vertical, self.board.set_dimension_vertical, self.board.get_dimension_vertical)

    def try_resolve_nonogram(self, intertactive_output) -> (bool, int, float):
        start = timer()

        if intertactive_output:
            self.loading_prompt.print_loading_line(self.board)
        
        self.__resolve_initial_state()
        cur_points_left, init_point_left = self.board.get_points_left(), self.board.get_init_points_left()
        if cur_points_left == init_point_left:
            end = timer()
            return False, self.steps, end - start
        
        prev_points_left = init_point_left
        while cur_points_left < prev_points_left:
            if intertactive_output:
                self.loading_prompt.print_loading_line(self.board)

            prev_points_left = cur_points_left
            self.__resolve_next_state()
            cur_points_left = self.board.get_points_left()

        end = timer()
        return self.board.is_resolved(), self.steps, end - start
