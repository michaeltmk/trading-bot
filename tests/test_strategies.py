import trading_bot.strategies as strategies

def test_ma_in_sequence_buy_signal_no_order_opened():
    config = {
        "name": "ma_in_sequence",
        "id": 1,
    }
    strategy = strategies.get_strategies("ma_in_sequence")(config)
    input = {
        "indecators": {
            "lower_ma_trend": 2,
            "upper_ma_trend": 1,
            "wave_ma": 3,
            "killer_ma": 4,
            "enter_ma": 5,
        },
        "history": {
            "orders": [],
            "summary": {
            }
        },
        "current_action": {
        },
        "target": "EURUSD",
        "price": 1
    }
    action = strategy.calculate(input)
    assert action.action == "BUY"
    assert action.amount == 1000