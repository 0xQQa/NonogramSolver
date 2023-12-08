from enum import Enum

class State(Enum):
    UNK     = 0
    HIT     = 1
    MISS    = -1

class Point:
    REPR_STATE_DICT = {State.MISS: 'x', State.UNK: '□', State.HIT: '■'}

    def __init__(self, state:State=State.UNK) -> None:
        self.state = state

    def set_state(self,  value:State) -> None:
        if self.state != State.UNK:
            return

        self.state = State(value)

    def get_state(self) -> int:
        return self.state.value

    def __repr__(self) -> str:
        return self.REPR_STATE_DICT[self.state]
    
    def __str__(self) -> str:
        return self.REPR_STATE_DICT[self.state]
    

if __name__ == "__main__":
    pass