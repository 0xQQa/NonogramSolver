from Board import Board

class LoadingPrompt:
    __LOADING_SIGNS = ['\\', '|', '/', '-']
    __LOADING_SIGNS_COUNT = len(__LOADING_SIGNS)

    def __init__(self) -> None:
        self.curr_loading_idx = 0
        self.loading_prompt = "\rLoading "

    def print_loading_line(self, board:Board) -> None:
        print(f"{self.loading_prompt} {self.__LOADING_SIGNS[self.curr_loading_idx]}")
        self.curr_loading_idx += 1
        self.curr_loading_idx %= self.__LOADING_SIGNS_COUNT
        print(board, end="\033[1A" * (board.dimension_vertical) + '\r')
     