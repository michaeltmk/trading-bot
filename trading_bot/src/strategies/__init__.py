from typing import Type

from .base_class import StrategyBaseClass
from .base_class import StrategyConfigBaseModel
from .ma_in_sequence import MaInSequenceClass
from .ma_in_sequence import MaInSequenceConfigModel
from .martingale import MartingaleClass
from .martingale import MartingaleConfigModel
from .trailing_stop_orders import TrailingStopOrdersClass
from .trailing_stop_orders import TrailingStopOrdersConfigModel

def get_strategies(name: str) -> Type[StrategyBaseClass]:
    if name == "ma_in_sequence":
        return MaInSequenceClass
    elif name == "martingale":
        return MartingaleClass
    elif name == "trailing_stop_orders":
        return TrailingStopOrdersClass
    else:
        raise ValueError(f"Strategy {name} is not implemented")
    
def get_strategies_config_model(name: str) -> Type[StrategyConfigBaseModel]:
    strategy_class = get_strategies(name)
    return strategy_class.config