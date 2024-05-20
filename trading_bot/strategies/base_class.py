from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List, Optional
from enum import Enum

class ActionTypes(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
    CLOSE = "CLOSE"

class StrategyActionBaseModel(BaseModel):
    action: Optional[ActionTypes] = None
    price: float = 0
    time: datetime = datetime.now()
    amount: float = 0

class OrderSummaryBaseModel(BaseModel):
    long_order: Optional[bool] = None
    total_profit: Optional[float] = 0
    total_amount: Optional[float] = 0

class StrategyHistoryBaseModel(BaseModel):
    orders: Optional[List[StrategyActionBaseModel]] = []
    summary: Optional[OrderSummaryBaseModel] = OrderSummaryBaseModel()


class StrategyConfigBaseModel(BaseModel):
    pass # should be defined in the strategy class

class StrategyIndecatorsBaseModel(BaseModel):
    pass # should be defined in the strategy class

class StrategyInputBaseModel(BaseModel):
    indecators: StrategyIndecatorsBaseModel # should be defined in the strategy class
    history: StrategyHistoryBaseModel
    current_action: StrategyActionBaseModel
    target: str
    price: float

class StrategyBaseClass():
    def __init__(self, config):
        self.config = StrategyConfigBaseModel(**config)
        self.indecators = {} # should be defined in the strategy class

    def calculate(self, input: dict) -> StrategyActionBaseModel:
        input = StrategyInputBaseModel(**input)
        raise NotImplementedError("calculate method is not implemented")
    