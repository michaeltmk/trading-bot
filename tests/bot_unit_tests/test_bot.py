from trading_bot.bot import signal_generator, scheduler

def test_bot():
    signal_generator_1 = signal_generator()
    signal_generator_1.append('ma_in_sequence')
    signal_generator_1.append('trailing_stop_orders')

    scheduler_1 = scheduler()
    scheduler_1.append(60, signal_generator_1)
    scheduler_1.run()