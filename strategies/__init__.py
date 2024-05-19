from indecators import IndecatorTypes
from . import *
from pydentic import BaseModel
from datetime import datetime

class ActionTypes():
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
    CLOSE = "CLOSE"

class StrategyActionBaseModel(BaseModel):
    action: ActionTypes
    price: float
    time: datetime
    amount: float

class OrderSummaryBaseModel(BaseModel):
    long_order: bool
    total_profit: float
    total_amount: float

class StrategyHistoryBaseModel(BaseModel):
    orders: list[StrategyActionBaseModel]
    summary: OrderSummaryBaseModel


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
    