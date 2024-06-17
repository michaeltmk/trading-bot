from . import strategies
import asyncio 
from apscheduler import AsyncScheduler

class data_fetcher:
    def __init__(self):
        pass

    def fetch(self):
        pass


class signal_generator:
    def __init__(self):
        self.strategies = []
        
    def append(self, strategy_name: str):
        self.strategies.append(strategies.get_strategies(strategy_name))

    def run(self):
        for strategy in self.strategies:
            # TODO: get input from exchange
            input_data = {}
            strategy.calculate(input_data)

# class scheduler:
#     def __init__(self):
#         self.signal_generators = []

#     def append(self, frequency: int, signal_generator: signal_generator):
#         self.signal_generators.append(
#                 {"frequency": frequency, 
#                 "signal_generator": signal_generator
#                 }
#             )

#     def run(self):
#         for signal_generator in self.signal_generators:
#             signal_generator["signal_generator"].run()


if __name__ == '__main__':
    signal_generator_1 = signal_generator()
    signal_generator_1.append('ma_in_sequence')
    signal_generator_1.append('trailing_stop_orders')

    async def bot_1():
        async with AsyncScheduler() as scheduler:
            scheduler.append(60, signal_generator_1)
            await scheduler.start_in_background()
    asyncio.run(bot_1())
