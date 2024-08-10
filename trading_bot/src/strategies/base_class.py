from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List, Optional
from enum import Enum

class ActionTypes(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
    CLOSE = "CLOSE"
    BUY_LIMIT = "BUY_LIMIT"
    SELL_LIMIT = "SELL_LIMIT"
    BUY_STOP = "BUY_STOP"
    SELL_STOP = "SELL_STOP"
    BUY_STOP_LIMIT = "BUY_STOP_LIMIT"
    SELL_STOP_LIMIT = "SELL_STOP_LIMIT"

class StrategyActionBaseModel(BaseModel):
    action: Optional[ActionTypes] = None
    price: float = 0
    time: datetime = datetime.now()
    amount: float = 0

class OrderSummaryBaseModel(BaseModel):
    long_order: Optional[bool] = None
    max_profit: Optional[float] = 0
    total_amount: Optional[float] = 0
    average_price: Optional[float] = 0

class StrategyHistoryBaseModel(BaseModel):
    orders: Optional[List[StrategyActionBaseModel]] = []
    summary: Optional[OrderSummaryBaseModel] = OrderSummaryBaseModel()


class StrategyConfigBaseModel(BaseModel):
    frequency_in_sec: int = 1

class StrategyIndecatorsBaseModel(BaseModel):
    pass # should be defined in the strategy class

class StrategyInputBaseModel(BaseModel):
    indecators: StrategyIndecatorsBaseModel # should be defined in the strategy class
    history: StrategyHistoryBaseModel
    decision_making: StrategyActionBaseModel
    target: str
    price: float

class StrategyBaseClass():
    config: StrategyConfigBaseModel
    def __init__(self, config):
        self.config = StrategyConfigBaseModel(**config)
        self.indecators = {} # should be defined in the strategy class

    def calculate(self, input: dict) -> StrategyActionBaseModel:
        input = StrategyInputBaseModel(**input)
        raise NotImplementedError("calculate method is not implemented")
    