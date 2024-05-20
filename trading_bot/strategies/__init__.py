from .ma_in_sequence import *
from .martingale import *

def get_strategies(name: str):
    if name == "ma_in_sequence":
        return MaInSequenceClass
    elif name == "martingale":
        return MartingaleClass
    else:
        raise ValueError(f"Strategy {name} is not implemented")