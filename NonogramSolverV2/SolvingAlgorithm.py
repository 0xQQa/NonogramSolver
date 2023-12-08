from Board import Board
from SolvingGenerator import SolvingGenerator
from timeit import default_timer as timer


class SolvingAlgorithm:

    def __init__(self, board: Board) -> None:
        self.steps = 0
        self.board = board
        self.solving_generator = SolvingGenerator()

    def resolve_one_dimension(self, dimension: int, solving_vector: list, set_dimension: callable, get_dimension_values: callable=lambda _: None) -> None:
        for idx, vector in enumerate(solving_vector):
            confident_solution = self.solving_generator.get_valid_vector(vector, dimension, get_dimension_values(idx))
            set_dimension(idx, confident_solution)

    def resolve_initial_state(self) -> None:
        self.steps += 1
        self.resolve_one_dimension(self.board.dimension_x, self.board.solving_vector_x, self.board.set_dimension_x)
        self.resolve_one_dimension(self.board.dimension_y, self.board.solving_vector_y, self.board.set_dimension_y)
        
    def resolve_next_state(self) -> None:
        self.steps += 1
        self.resolve_one_dimension(self.board.dimension_x, self.board.solving_vector_x, self.board.set_dimension_x, self.board.get_dimension_x_values)
        self.resolve_one_dimension(self.board.dimension_y, self.board.solving_vector_y, self.board.set_dimension_y, self.board.get_dimension_y_values)

    def try_resolve_nonogram(self) -> (bool, int, float):
        start = timer()
        self.resolve_initial_state()
        cur_points_left = self.board.get_points_left()
        if cur_points_left == self.board.get_init_points_left():
            end = timer()
            return False, self.steps, end - start
        
        prev_points_left = self.board.get_init_points_left()
        while cur_points_left < prev_points_left:
            prev_points_left = cur_points_left
            self.resolve_next_state()
            cur_points_left = self.board.get_points_left()

        end = timer()
        return self.board.is_resolved(), self.steps, end - start
