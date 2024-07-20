from typing import Type

from trading_bot.strategies.base_class import StrategyBaseClass
from .ma_in_sequence import MaInSequenceClass
from .martingale import MartingaleClass
from .trailing_stop_orders import TrailingStopOrdersClass

def get_strategies(name: str) -> Type[StrategyBaseClass]:
    if name == "ma_in_sequence":
        return MaInSequenceClass
    elif name == "martingale":
        return MartingaleClass
    elif name == "trailing_stop_orders":
        return TrailingStopOrdersClass
    else:
        raise ValueError(f"Strategy {name} is not implemented")