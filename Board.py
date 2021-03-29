class Board:

    def __init__(self, dimension, solving_vector_x, solving_vector_y):
        self.dimension = dimension
        self.board = [[0 for _ in range(dimension)] for _ in range(dimension)]    
        self.solving_vector_x = solving_vector_x
        self.solving_vector_y = solving_vector_y    
    
    def get_column(self, index):
        return list(map(lambda row: row[index], self.board))

    def get_row(self, index):
        return self.board[index]
        
    def set_hit(self, x, y):
        self.board[x][y] = 1

    def set_miss(self, x, y):
        self.board[x][y] = -1

    def get_vector_y(self, index): 
        return self.solving_vector_y[index]

    def get_vector_x(self, index): 
        return list(map(lambda row: row[index], self.solving_vector_x))

    def show_row(self, index):
        ret_str = ' '
        for field in self.board[index]:
            if field == 1: ret_str += ("■ ")
            elif field == -1: ret_str += ("⨯ ")
            else: ret_str += ("□ ")

        return ret_str

    def show(self):
        for index in range(self.dimension): print(self.show_row(index))

    def is_finished(self):
        for row in self.board:
            if 0 in row: return False
        
        return True
