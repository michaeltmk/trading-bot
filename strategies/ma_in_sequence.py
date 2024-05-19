from pydantic import BaseModel
from . import *
from datetime import datetime as dt

class MaInSequenceConfigModel(BaseModel):
    id: int
    name: str = 'Jane Doe'

class MaInSequenceIndecatorsModel(BaseModel):
    lower_ma_trend: float
    upper_ma_trend: float
    wave_ma: float
    killer_ma: float
    basic_ma_shift: float

class MaInSequenceInputModel(StrategyInputBaseModel):
    indecators: MaInSequenceIndecatorsModel

class MaInSequenceClass(StrategyBaseClass):
    def __init__(self, config: dict):
        self.config = MaInSequenceConfigModel(**config)
        # define the strategy parameters
        self.indecators = {
            "H1": {"lower_ma_trend": {
                "indecator": "MA",
                "period": 144},
                "upper_ma_trend": {
                "indecator": "MA",
                "period": 169},
                "wave_ma": {
                "indecator": "MA",
                "period": 34},
                "killer_ma": {
                "indecator": "MA",
                "period": 12},
                "basic_ma_shift": {
                "indecator": "MA",
                "period": 1},
                }
        }
    

    def calculate(self, input: dict) -> StrategyActionBaseModel:
        # schema validation
        input = MaInSequenceInputModel(**input)
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
        if data.basic_ma_shift > data.killer_ma and data.killer_ma > data.wave_ma and data.wave_ma > data.lower_ma_trend and data.lower_ma_trend > data.upper_ma_trend:
            return StrategyActionBaseModel(
                action=ActionTypes.BUY,
                price=input.price,
                time=dt.now(),
                amount=1000                
            )
        elif data.basic_ma_shift < data.killer_ma and data.killer_ma < data.wave_ma and data.wave_ma < data.lower_ma_trend and data.lower_ma_trend < data.upper_ma_trend:
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