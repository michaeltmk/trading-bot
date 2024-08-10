from .base_class import *
from datetime import datetime as dt

class MartingaleConfigModel(StrategyConfigBaseModel):
    FirstEntryLotsSize: float
    LotExponent: float
    Level1PipsStep: float
    Level2PipsStep: float
    Level3PipsStep: float
    Level4PipsStep: float
    Level5PipsStep: float
    Level6PipsStep: float
    Level7PipsStep: float
    SLInLevel: float
    TotalLevels: float

class MartingaleIndecatorsModel(StrategyIndecatorsBaseModel):
    pass # no indecators for this strategy

class MartingaleInputModel(StrategyInputBaseModel):
    indecators: MartingaleIndecatorsModel

class MartingaleClass(StrategyBaseClass):
    config: MartingaleConfigModel
    def __init__(self, config: dict):
        self.config = MartingaleConfigModel(**config)
        # define the strategy parameters
        self.indecators = {}
    

    def calculate(self, input_dict: dict) -> StrategyActionBaseModel:
        # schema validation
        input = MartingaleInputModel(**input_dict)
        
        # this is a open second order strategy, so we need to check if the first order is already opened
        if input.history.orders.len() == 0:
            return StrategyActionBaseModel(
                action=ActionTypes.HOLD,
                price=input.price,
                time=dt.now(),
                amount=0                
            )
        # if orders excess the total levels, close all orders
        if input.history.orders.len() > self.config.TotalLevels:
            return StrategyActionBaseModel(
                action=ActionTypes.CLOSE,
                price=input.price,
                time=dt.now(),
                amount=0                
            )
        
        # calculate the strategy
        if input.price < input.decision_making.price and input.decision_making.action == ActionTypes.BUY:
            return StrategyActionBaseModel(
                action=ActionTypes.BUY,
                price=input.price,
                time=dt.now(),
                amount=1000                
            )
        elif input.price > input.decision_making.price and input.decision_making.action == ActionTypes.SELL:
            return StrategyActionBaseModel(
                action=ActionTypes.SELL,
                price=input.price,
                time=dt.now(),
                amount=1000                
            )
        else:
            return StrategyActionBaseModel(
                action=ActionTypes.HOLD,
                price=input.price,
                time=dt.now(),
                amount=0                
            )