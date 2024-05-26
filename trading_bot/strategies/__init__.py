from .ma_in_sequence import *
from .martingale import *
from .trailing_stop_orders import *

def get_strategies(name: str):
    if name == "ma_in_sequence":
        return MaInSequenceClass
    elif name == "martingale":
        return MartingaleClass
    elif name == "trailing_stop_orders":
        return TrailingStopOrdersClass
    else:
        raise ValueError(f"Strategy {name} is not implemented")