import trading_bot.src.strategies as strategies
from trading_bot.src.strategies import StrategyBaseClass

def test_trailing_stop_orders_close_order_profit_taken():
    config = {
        "frequency_in_sec": 60,
        "stop_loss_in_fix_dollars": 0,
        "trailing_start_in_dollars": 1,
        "trailing_distance_in_dollars": 1,
        "breakeven_start_in_dollars": 0,
        "breakeven_distance_in_dollars": 0,
        "take_profit_in_dollars": 10
    }
    strategy: StrategyBaseClass = strategies.get_strategies("trailing_stop_orders")(config)
    input = {
        "indecators": {},
        "history": {
            "orders": [
                {
                    "type": "BUY",
                    "price": 1,
                    "stop_loss": 0,
                    "take_profit": 1
                }
            ],
            "summary": {
                "long_order": True,
                "max_profit": 10,
                "total_amount": 1,
                "average_price": 1
            },
        },
        "decision_making": {
            "action": "HOLD",
            "price": 10,
            "time": "2021-01-01T00:00:00",
            "amount": 1
        },
        "target": "EURUSD",
        "price": 10
    }
    action = strategy.calculate(input)
    assert action.action == "CLOSE"
