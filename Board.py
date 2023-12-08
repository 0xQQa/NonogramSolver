from Point import Point, State


class Board:

    def __init__(self, dimension_x: int, dimension_y: int, solving_vector_x: list, solving_vector_y: list) -> None:
        self.dimension_x, self.dimension_y = dimension_x, dimension_y
        self.solving_vector_x, self.solving_vector_y = solving_vector_x, solving_vector_y  
        
        get_point_row = lambda: [Point() for _ in range(self.dimension_x)]
        self.board_state = [get_point_row() for _ in range(self.dimension_y)]

    def get_points_left(self) -> int:
        return sum(map(lambda x: sum(map(lambda y: y.state == State.UNK, x)), self.board_state))

    def get_init_points_left(self) -> int:
        return self.dimension_x * self.dimension_y
    
    def is_resolved(self) -> bool:
        return self.get_points_left() == 0

    def get_dimension_y(self, index: int) -> list:
        return list(map(lambda row: row[index], self.board_state))

    def get_dimension_x(self, index: int) -> list:
        return self.board_state[index]
    
    def get_dimension_internal_values(self, index: int, get_dimension: callable) -> list:
        dimension = get_dimension(index)
        dimension = map(Point.get_state, dimension)
        return list(dimension)

    def get_dimension_y_values(self, index: int) -> list:
        return self.get_dimension_internal_values(index, self.get_dimension_y)

    def get_dimension_x_values(self, index: int) -> list:
        return self.get_dimension_internal_values(index, self.get_dimension_x)

    def set_dimension_internal(self, index: int, valid_vector: list, get_dimension: callable) -> None:
        tmp_dimension = get_dimension(index)
        for point, new_state in zip(tmp_dimension, valid_vector):
            point.set_state(new_state)

    def set_dimension_y(self, index: int, valid_vector: list) -> None:
        self.set_dimension_internal(index, valid_vector, self.get_dimension_y)

    def set_dimension_x(self, index: int, valid_vector: list) -> None:
        self.set_dimension_internal(index, valid_vector, self.get_dimension_x)

    def __repr__(self) -> str:
        clean_str_row = lambda str_row: str(str_row).replace('\'', '').replace(',', '')[1:-1]
        make_str_row = lambda str_row: clean_str_row(list(map(str, str_row)))
        make_str_board = lambda str_board: str.join('\n' ,list(map(make_str_row, str_board)))
        return make_str_board(self.board_state)
