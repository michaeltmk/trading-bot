from trading_bot.bot import signal_generator
# from apscheduler import AsyncScheduler # for apscheduler 4
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytest
import asyncio
from trading_bot import utilities

@pytest.fixture
def anyio_backend():
    return 'asyncio'

async def _test_bot(anyio_backend):
    sg1_config = utilities.config_utilities.load_strategies_config('config/sg1_strategies_config.yaml')
    signal_generator_1 = signal_generator(sg1_config)

    async with AsyncScheduler() as scheduler:
        scheduler_1 = scheduler()
        scheduler_1.append(60, signal_generator_1)
        scheduler_1.run()

def test_signal_generator():
    sg1_config = utilities.config_utilities.load_strategies_config('config/sg1_strategies_config.yaml')
    signal_generator_1 = signal_generator(sg1_config)
    signal_generator_1.run({})
