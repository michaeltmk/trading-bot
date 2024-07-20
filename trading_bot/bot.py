from . import strategies
import asyncio 
# from apscheduler import AsyncScheduler # for apscheduler 4
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import List
class data_fetcher:
    def __init__(self):
        pass

    def fetch(self):
        pass


class signal_generator:
    def __init__(self):
        self.strategies: List[strategies.StrategyBaseClass]  = []
        
    def append(self, strategy_name: str, config: dict):
        self.strategies.append(strategies.get_strategies(strategy_name)(config))

    def run(self,strategies_inputs: dict):
        for strategy in self.strategies:
            # TODO: get input from exchange
            strategy_input = strategies_inputs[strategy.config.name]
            strategy.calculate(strategy_input)

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
    signal_generator_1.append('ma_in_sequence',{})
    signal_generator_1.append('trailing_stop_orders',{})

    async def bot_1():
        # async with AsyncScheduler() as scheduler:
        #     scheduler.append(60, signal_generator_1)
        #     await scheduler.start_in_background()
        scheduler = AsyncIOScheduler()
        scheduler.add_job(signal_generator_1, 'interval', seconds=3)
        scheduler.start()
        while True:
            await asyncio.sleep(1000)

    asyncio.run(bot_1())
