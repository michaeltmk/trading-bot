import sys
from . import strategies
import asyncio 
# from apscheduler import AsyncScheduler # for apscheduler 4
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import List
from . import utilities
import loguru

class data_fetcher:
    def __init__(self):
        pass

    def fetch(self):
        pass


class signal_generator:
    def __init__(self, config: utilities.strategies_config_model):
        loguru.logger.info("Initializing signal generator")
        self.strategies: List[strategies.StrategyBaseClass]  = []
        for strategy in config.strategies:
            if strategy.enabled:
                loguru.logger.info(f"Appending strategy {strategy.name}")
                self.append(strategy.name, dict(strategy.config))
            else:
                loguru.logger.info(f"Skipping strategy {strategy.name}")

        
    def append(self, strategy_name: str, config: dict):
        self.strategies.append(strategies.get_strategies(strategy_name)(config))

    def run(self,strategies_inputs: dict):
        for strategy in self.strategies:
            strategy_input = strategies_inputs[strategy.config.name]
            strategy.calculate(strategy_input)

if __name__ == '__main__':
    run_forever = sys.argv[1] == 'run_forever'
    sg1_config = utilities.config_utilities.load_strategies_config('config/sg1_strategies_config.yaml')
    signal_generator_1 = signal_generator(sg1_config)
    if run_forever:
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
    else:
        # TODO: get input from data_fetcher
        signal_generator_1.run({
            "ma_in_sequence": {
                "price": 100,
                "history": {
                    "summary": {
                        "total_amount": 0,
                        "average_price": 0,
                        "max_profit": 0,
                        "long_order": False
                    }
                }
            },
            "trailing_stop_orders": {
                "price": 100,
                "history": {
                    "summary": {
                        "total_amount": 0,
                        "average_price": 0,
                        "max_profit": 0,
                        "long_order": False
                    }
                }
            }
        })
