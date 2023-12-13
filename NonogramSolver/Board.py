from Point import Point


class Board:

    def __init__(self, dimension_horizontal: int, dimension_vertical: int, solving_vector_horizontal: list, solving_vector_vertical: list) -> None:
        self.dimension_horizontal, self.dimension_vertical = dimension_horizontal, dimension_vertical
        self.solving_vector_horizontal, self.solving_vector_vertical = solving_vector_horizontal, solving_vector_vertical  
        
        get_point_row = lambda: [Point() for _ in range(self.dimension_horizontal)]
        self.board_state = [get_point_row() for _ in range(self.dimension_vertical)]

    def get_points_left(self) -> int:
        return sum(map(lambda row: sum(map(lambda point: point.state == Point.UNK, row)), self.board_state))

    def get_init_points_left(self) -> int:
        return self.dimension_horizontal * self.dimension_vertical
    
    def is_resolved(self) -> bool:
        return self.get_points_left() == 0

    def __get_dimension_vertical(self, index: int) -> list:
        return list(map(lambda row: row[index], self.board_state))

    def __get_dimension_horizontal(self, index: int) -> list:
        return self.board_state[index]
    
    def __get_dimension_internal_values(self, index: int, get_dimension: callable) -> list:
        dimension = get_dimension(index)
        dimension = map(Point.get_state, dimension)
        return list(dimension)

    def get_dimension_vertical(self, index: int) -> list:
        return self.__get_dimension_internal_values(index, self.__get_dimension_vertical)

    def get_dimension_horizontal(self, index: int) -> list:
        return self.__get_dimension_internal_values(index, self.__get_dimension_horizontal)

    def __set_dimension_internal(self, index: int, valid_vector: list, get_dimension: callable) -> None:
        tmp_dimension = get_dimension(index)
        for point, new_state in zip(tmp_dimension, valid_vector):
            point.set_state(new_state)

    def set_dimension_vertical(self, index: int, valid_vector: list) -> None:
        self.__set_dimension_internal(index, valid_vector, self.__get_dimension_vertical)

    def set_dimension_horizontal(self, index: int, valid_vector: list) -> None:
        self.__set_dimension_internal(index, valid_vector, self.__get_dimension_horizontal)

    def __repr__(self) -> str:
        clean_str_row = lambda str_row: str(str_row).replace('\'', '').replace(',', '')[1:-1]
        make_str_row = lambda str_row: clean_str_row(list(map(str, str_row)))
        make_str_board = lambda str_board: str.join('\n' ,list(map(make_str_row, str_board)))
        return make_str_board(self.board_state)
