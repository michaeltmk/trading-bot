from .base_class import *
from datetime import datetime as dt

class TrailingStopOrdersConfigModel(StrategyConfigBaseModel):
    take_profit_in_dollars: float = 0
    trailing_start_in_dollars: float = 0
    trailing_distance_in_dollars: float = 0
    breakeven_start_in_dollars: float = 0
    breakeven_distance_in_dollars: float = 0
    stop_loss_in_fix_dollars: float = 0

class TrailingStopOrdersIndecatorsModel(StrategyIndecatorsBaseModel):
    pass

class TrailingStopOrdersInputModel(StrategyInputBaseModel):
    indecators: TrailingStopOrdersIndecatorsModel

class TrailingStopOrdersClass(StrategyBaseClass):
    config: TrailingStopOrdersConfigModel
    def __init__(self, config: dict):
        self.config = TrailingStopOrdersConfigModel(**config)
        # define the strategy parameters
        self.indecators = []

    

    def calculate(self, input_dict: dict) -> StrategyActionBaseModel:
        # schema validation
        input = TrailingStopOrdersInputModel(**input_dict)
        data = input.indecators

        # this is a close order strategy, so we need to check if the order is already opened
        if input.history.summary.total_amount == 0:
            return StrategyActionBaseModel(
                action=ActionTypes.HOLD,
                price=input.price,
                time=dt.now(),
                amount=0                
            )
            
        # calculate the strategy
        buy_price = input.history.summary.average_price
        current_price = input.price
        max_profit = input.history.summary.max_profit
        profit = current_price - buy_price if input.history.summary.long_order else buy_price - current_price
        if self.config.take_profit_in_dollars > 0 and profit >= self.config.take_profit_in_dollars:
            return StrategyActionBaseModel(
                action=ActionTypes.CLOSE,
                price=input.price,
                time=dt.now(),
                amount=input.history.summary.total_amount                
            )
        if self.config.stop_loss_in_fix_dollars > 0 and profit <= self.config.stop_loss_in_fix_dollars:
            return StrategyActionBaseModel(
                action=ActionTypes.CLOSE,
                price=input.price,
                time=dt.now(),
                amount=input.history.summary.total_amount                
            )
        # if input.history.summary.long_order:
        if profit > 0:
            if max_profit >= self.config.trailing_start_in_dollars:
                if max_profit - profit >= self.config.trailing_distance_in_dollars:
                    return StrategyActionBaseModel(
                        action=ActionTypes.CLOSE,
                        price=input.price,
                        time=dt.now(),
                        amount=input.history.summary.total_amount                
                    )
                else:
                    return StrategyActionBaseModel(
                        action=ActionTypes.HOLD,
                        price=input.price,
                        time=dt.now(),
                        amount=0                
                    )
            else:
                return StrategyActionBaseModel(
                    action=ActionTypes.HOLD,
                    price=input.price,
                    time=dt.now(),
                    amount=0                
                )
        else:
            if -profit >= self.config.breakeven_start_in_dollars:
                if -profit - self.config.breakeven_distance_in_dollars >= 0:
                    return StrategyActionBaseModel(
                        action=ActionTypes.CLOSE,
                        price=input.price,
                        time=dt.now(),
                        amount=input.history.summary.total_amount                
                    )
                else:
                    return StrategyActionBaseModel(
                        action=ActionTypes.HOLD,
                        price=input.price,
                        time=dt.now(),
                        amount=0                
                    )
            else:
                return StrategyActionBaseModel(
                    action=ActionTypes.HOLD,
                    price=input.price,
                    time=dt.now(),
                    amount=0                
                )