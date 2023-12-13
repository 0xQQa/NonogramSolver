from typing import Final


class Point:
    MISS:               Final[int] = -1
    HIT:                Final[int] = 1
    UNK:                Final[int] = 0
    __REPR_STATE_DICT:  dict = {MISS: ' ', UNK: '�', HIT: '■'}

    def __init__(self, state:int=0) -> None:
        self.state = state

    def set_state(self,  value:int) -> None:
        if self.state != Point.UNK:
            return
        
        self.state = value

    def get_state(self) -> int:
        return self.state

    def __repr__(self) -> str:
        return self.__REPR_STATE_DICT[self.state]
    
    def __str__(self) -> str:
        return self.__REPR_STATE_DICT[self.state]
    