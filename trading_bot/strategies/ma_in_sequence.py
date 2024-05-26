from pydantic import BaseModel
from .base_class import *
from datetime import datetime as dt

class MaInSequenceConfigModel(StrategyConfigBaseModel):
    id: int
    name: str = 'Jane Doe'

class MaInSequenceIndecatorsModel(StrategyIndecatorsBaseModel):
    lower_ma_trend: float
    upper_ma_trend: float
    wave_ma: float
    killer_ma: float
    enter_ma: float

class MaInSequenceInputModel(StrategyInputBaseModel):
    indecators: MaInSequenceIndecatorsModel

class MaInSequenceClass(StrategyBaseClass):
    def __init__(self, config: dict):
        self.config = MaInSequenceConfigModel(**config)
        # define the strategy parameters
        self.indecators = [
                    {"indecator": "MA", "period": 144, "shift": 1, "name": "lower_ma_trend", "timeframe": "H1"},
                    {"indecator": "MA", "period": 169, "shift": 1, "name": "upper_ma_trend", "timeframe": "H1"},
                    {"indecator": "MA", "period": 34, "shift": 1, "name": "wave_ma", "timeframe": "H1"},
                    {"indecator": "MA", "period": 12, "shift": 1, "name": "killer_ma", "timeframe": "H1"},
                    {"indecator": "MA", "period": 3, "shift": 1, "name": "enter_ma", "timeframe": "M30"}
                ]

    

    def calculate(self, input_dict: dict) -> StrategyActionBaseModel:
        # schema validation
        input = MaInSequenceInputModel(**input_dict)
        data = input.indecators

        # this is a open order strategy, so we need to check if the order is already opened
        if input.history.summary.total_amount > 0:
            return StrategyActionBaseModel(
                action=ActionTypes.HOLD,
                price=input.price,
                time=dt.now(),
                amount=0                
            )
            
        # calculate the strategy
        if data.enter_ma > data.killer_ma and data.killer_ma > data.wave_ma and data.wave_ma > data.lower_ma_trend and data.lower_ma_trend > data.upper_ma_trend:
            return StrategyActionBaseModel(
                action=ActionTypes.BUY,
                price=input.price,
                time=dt.now(),
                amount=1000                
            )
        elif data.enter_ma < data.killer_ma and data.killer_ma < data.wave_ma and data.wave_ma < data.lower_ma_trend and data.lower_ma_trend < data.upper_ma_trend:
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