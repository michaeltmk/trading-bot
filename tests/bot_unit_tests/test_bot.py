from trading_bot.bot import signal_generator
# from apscheduler import AsyncScheduler # for apscheduler 4
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytest
import asyncio

@pytest.fixture
def anyio_backend():
    return 'asyncio'

async def _test_bot(anyio_backend):
    signal_generator_1 = signal_generator()
    signal_generator_1.append('ma_in_sequence')
    signal_generator_1.append('trailing_stop_orders')

    async with AsyncScheduler() as scheduler:
        scheduler_1 = scheduler()
        scheduler_1.append(60, signal_generator_1)
        scheduler_1.run()

def test_main2():
    signal_generator_1 = signal_generator()
    signal_generator_1.append('ma_in_sequence')
    signal_generator_1.append('trailing_stop_orders')
    signal_generator_1.run()