class Board:

    def __init__(self, dimension_x, dimension_y, solving_vector_x, solving_vector_y):
        self.dimension_x, self.dimension_y = dimension_x, dimension_y
        self.board = [[0 for _ in range(dimension_x)] for _ in range(dimension_y)]    
        self.solving_vector_x = solving_vector_x
        self.solving_vector_y = solving_vector_y    
        self.changes_made = False
    
    def get_column(self, index):
        return list(map(lambda row: row[index], self.board))

    def get_row(self, index):
        return self.board[index]
        
    def set_hit(self, x, y):
        if self.board[x][y] == -1: raise Exception("Non hitabble!")
        if self.board[x][y] == 0:
            self.board[x][y] = 1
            self.changes_made = True
        
    def set_miss(self, x, y):
        if self.board[x][y] == 1: raise Exception("Non missable!")
        if self.board[x][y] == 0:
            self.board[x][y] = -1
            self.changes_made = True

    def get_vector_y(self, index): 
        return self.solving_vector_y[index]

    def get_vector_x(self, index): 
        return self.solving_vector_x[index]

    def show_row(self, index):
        ret_str = ' '
        for field in self.board[index]:
            if field == 1: ret_str += ("■ ")
            elif field == -1: ret_str += ("⨯ ")
            else: ret_str += ("□ ")

        return ret_str

    def show(self):
        for index in range(self.dimension_y): print(self.show_row(index))

    def is_finished(self):
        for row in self.board:
            if 0 in row: return False
        
        return True
